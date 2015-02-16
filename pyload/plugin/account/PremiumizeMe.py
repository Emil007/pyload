# -*- coding: utf-8 -*-

from pyload.plugin.Account import Account

from pyload.utils import json_loads


class PremiumizeMe(Account):
    __name__    = "PremiumizeMe"
    __type__    = "account"
    __version__ = "0.11"

    __description__ = """Premiumize.me account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Florian Franzen", "FlorianFranzen@gmail.com")]


    def loadAccountInfo(self, user, req):
        # Get user data from premiumize.me
        status = self.getAccountStatus(user, req)
        self.logDebug(status)

        # Parse account info
        account_info = {"validuntil": float(status['result']['expires']),
                        "trafficleft": max(0, status['result']['trafficleft_bytes'])}

        if status['result']['type'] == 'free':
            account_info['premium'] = False

        return account_info


    def login(self, user, data, req):
        # Get user data from premiumize.me
        status = self.getAccountStatus(user, req)

        # Check if user and password are valid
        if status['status'] != 200:
            self.wrongPassword()


    def getAccountStatus(self, user, req):
        # Use premiumize.me API v1 (see https://secure.premiumize.me/?show=api)
        # to retrieve account info and return the parsed json answer
        answer = req.load("https://api.premiumize.me/pm-api/v1.php",
                           get={'method'       : "accountstatus",
                                'params[login]': user,
                                'params[pass]' : self.accounts[user]['password']})
        return json_loads(answer)
