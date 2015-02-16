# -*- coding: utf-8 -*-

import re

from pyload.plugin.Captcha import Captcha


class SolveMedia(Captcha):
    __name__    = "SolveMedia"
    __type__    = "captcha"
    __version__ = "0.06"

    __description__ = """SolveMedia captcha service plugin"""
    __license__     = "GPLv3"
    __authors__     = [("pyLoad Team", "admin@pyload.org")]


    KEY_PATTERN = r'api\.solvemedia\.com/papi/challenge\.(?:no)?script\?k=(.+?)["\']'


    def challenge(self, key=None):
        if not key:
            if self.detect_key():
                key = self.key
            else:
                errmsg = _("SolveMedia key not found")
                self.plugin.fail(errmsg)
                raise TypeError(errmsg)

        html = self.plugin.req.load("http://api.solvemedia.com/papi/challenge.noscript", get={'k': key})
        try:
            challenge = re.search(r'<input type=hidden name="adcopy_challenge" id="adcopy_challenge" value="([^"]+)">',
                                  html).group(1)
            server    = "http://api.solvemedia.com/papi/media"
        except Exception:
            errmsg = _("SolveMedia challenge pattern not found")
            self.plugin.error(errmsg)
            raise ValueError(errmsg)

        self.plugin.logDebug("SolveMedia challenge: %s" % challenge)

        return challenge, self.result(server, challenge)


    def result(self, server, challenge):
        result = self.plugin.decryptCaptcha(server, get={'c': challenge}, imgtype="gif")

        self.plugin.logDebug("SolveMedia result: %s" % result)

        return result
