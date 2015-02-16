# -*- coding: utf-8 -*-

from pyload.plugin.internal.DeadCrypter import DeadCrypter, create_getInfo


class FilesonicCom(DeadCrypter):
    __name__    = "FilesonicCom"
    __type__    = "crypter"
    __version__ = "0.12"

    __pattern__ = r'http://(?:www\.)?filesonic\.com/folder/\w+'

    __description__ = """Filesonic.com folder decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


getInfo = create_getInfo(FilesonicCom)
