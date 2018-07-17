# -*- coding: utf-8 -*-

import vim
from ncm2 import Ncm2Source, getLogger
import re
from os.path import expanduser, expandvars
import subprocess

from os.path import dirname, abspath, join, pardir, expandvars, expanduser
from subprocess import check_output, PIPE
from threading import Thread, Event

logger = getLogger(__name__)


def log(msg):
    from datetime import datetime
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S,%f")
    with open('/tmp/ncm2-webcomplete.log', 'a') as file_:
        file_.write('%s %s\n' % (timestamp, msg))


class Source(Ncm2Source):
    def __init__(self, nvim):
        super(Source, self).__init__(nvim)
        # self.executable_look = nvim.call('executable', 'look')
        # filedir = dirname(abspath(__file__))
        # projectdir = abspath(join(filedir, pardir))
        # join(projectdir, 'sh', 'webcomplete')
        self.__script = expanduser(expandvars('~/.local/bin/bt words'))
        # log('script: %s' % self.__script)

    def on_complete(self, ctx):

        # query = ctx['base']
        #
        # if not self.executable_look:
        #     return

        try:
            # log('ctx: %s' % ctx)
            matches = self._get_matches()
            # log('matches: %s' % matches)
            self.complete(ctx, ctx['startccol'], matches)
        except subprocess.CalledProcessError as e:
            log('error: %s' % e)
            return

    def _get_matches(self):
        output = check_output(self.__script, shell=True)
        candidates = output.decode('utf-8', errors='ignore').splitlines()
        return [{'word': word} for word in candidates]


source = Source(vim)

on_complete = source.on_complete
