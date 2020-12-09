import time

import schedule
from Framework.api import ThreadKit
from Framework.api.logkit import LogKit
from Framework.api.networkkit import HTTPKit
from Framework.api.parsekit import XMLKit
from Framework.api.runtimekit import PrefsKit

global Log
Log = Log  # type: LogKit
global Prefs
Prefs = Prefs  # type: PrefsKit
global HTTP
HTTP = HTTP  # type: HTTPKit
global XML
XML = XML  # type: XMLKit
global Thread
Thread = Thread  # type: ThreadKit

base_url = 'http://127.0.0.1:32400'
refresh_time = ''
job = None


# noinspection PyUnresolvedReferences
@handler('/video/tv_guide_refresher', 'TV Guide Refresher')
def main_menu():
    pass


# noinspection PyPep8Naming
def Start():
    Log.Info('Create scheduler thread')
    # noinspection PyTypeChecker
    Thread.Create(scheduler_thread)
    schedule_job()


def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_job():
    global refresh_time
    new_refresh_time = Prefs['refresh_time']
    if refresh_time == new_refresh_time:
        return
    refresh_time = new_refresh_time
    Log.Info('Set refresh time to: ' + refresh_time)

    global job
    if job is not None:
        Log.Info('Cancel the existing job')
        schedule.cancel_job(job)
        job = None
    Log.Info('Schedule the job at refresh time')
    job = schedule.every().day.at(refresh_time).do(refresh_dvrs)


def refresh_dvrs():
    Log.Info('Running the scheduled job')
    dvrs = get_dvrs()
    dvr_count = 0 if dvrs is None else len(dvrs)
    Log.Info('Found %d DVRs' % dvr_count)

    if dvr_count == 0:
        return

    for dvr in dvrs:
        refresh_dvr(dvr)


def get_dvrs():
    response = HTTP.Request(base_url + '/livetv/dvrs', immediate=True)
    media_container = XML.ObjectFromString(response.content)
    return media_container.find('Dvr')


def refresh_dvr(dvr):
    key = dvr.get('key')
    Log.Info('Refresh program guide for DVR %s' % key)
    HTTP.Request(base_url + '/livetv/dvrs/' + key + '/reloadGuide', immediate=True, method='POST')


# noinspection PyPep8Naming
def ValidatePrefs():
    schedule_job()
