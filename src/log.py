# encoding: utf-8
#
# Copyright © 2013 deanishe@deanishe.net.
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2013-11-03
#

"""
"""

from __future__ import print_function

import logging

from settings import Settings

_handler = None

def logger(name=u''):
    global _handler
    if not _handler:
        s = Settings()
        if s[u'logging']:
            _handler = logging.FileHandler(filename=s.log_path,
                                           encoding=u'utf-8',
                                           delay=True)
            _handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
        else:
            _handler = logging.NullHandler()
    log = logging.getLogger(name)
    log.addHandler(_handler)
    log.setLevel(logging.DEBUG)
    return log
