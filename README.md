# TV Guide Refresher

A Plex plugin for refreshing TV program guide periodically.

## Background

The guide refresh functionality in "DVR Settings" of Plex Media Server has never been working since forever. So it has
to be implemented independently, for which TV Guide Refresher, as a Plex plugin, is created.

## Installation

Download [the latest release](https://github.com/williamthegrey/tv-guide-refresher/releases/latest) of TV Guide
Refresher, and unzip it to a directory named "tv-guide-refresher.bundle".

Find the "Plug-ins" directory of your Plex Media Server installation
following [these instructions](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/), and put
the "tv-guide-refresher.bundle" directory into it.

Restart your Plex Media Server.

## Usage

Log in to your Plex Media Server and go to "Manage > Plugins".

Locate the TV Guide Refresher plugin, and click the gear icon. In the TV Guide Refresher Settings dialog, input the
Refresh Time as you wish, and click Save.

Now the Plex Media Server will refresh the TV guide at the specified time every day. 