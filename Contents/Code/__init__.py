import time

from Framework.api.logkit import LogKit
from Framework.api.networkkit import HTTPKit
from Framework.api.parsekit import XMLKit

global Log
Log = Log  # type: LogKit
global HTTP
HTTP = HTTP  # type: HTTPKit
global XML
XML = XML  # type: XMLKit

base_url = 'http://127.0.0.1:32400'
sleep_seconds = 5


# noinspection PyPep8Naming
def Start():
    Log.Info('Sleep for %d seconds' % sleep_seconds)
    time.sleep(sleep_seconds)

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
