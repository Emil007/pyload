# -*- coding: utf-8 -*-

from pyload.network.RequestFactory import getURL
from pyload.plugin.internal.MultiHoster import MultiHoster
from pyload.utils import json_loads


class MyfastfileCom(MultiHoster):
    __name__    = "MyfastfileCom"
    __type__    = "hook"
    __version__ = "0.02"


    __config__ = [("hosterListMode", "all;listed;unlisted", "Use for hosters (if supported)", "all"),
                ("hosterList", "str", "Hoster list (comma separated)", ""),
                ("unloadFailing", "bool", "Revert to standard download if download fails", False),
                ("interval", "int", "Reload interval in hours (0 to disable)", 24)]

    __description__ = """Myfastfile.com hook plugin"""
    __license__     = "GPLv3"
    __authors__     = [("stickell", "l.stickell@yahoo.it")]



    def getHoster(self):
        json_data = getURL("http://myfastfile.com/api.php", get={'hosts': ""}, decode=True)
        self.logDebug("JSON data", json_data)
        json_data = json_loads(json_data)

        return json_data['hosts']
