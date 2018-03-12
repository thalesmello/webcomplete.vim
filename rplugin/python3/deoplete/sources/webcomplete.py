'''Web completion of words for Neovim
This plugin works with Neovim and Deoplete, allowing you to
complete words from your Chrome instance in your editor.'''

from os.path import dirname, abspath, join, pardir
from subprocess import run, PIPE
from .base import Base
import deoplete.util


def log(msg):
    from datetime import datetime
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S,%f")
    with open('/tmp/deoplete-webcomplete.log', 'a') as file_:
        file_.write('%s %s\n' % (timestamp, msg))


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.__last_input = None
        self.__cache = None

        self.name = 'webcomplete'
        self.kind = 'keyword'
        self.mark = '[web]'
        self.rank = 4
        filedir = dirname(abspath(__file__))
        projectdir = abspath(join(filedir, pardir, pardir, pardir, pardir))
        self.__script = join(projectdir, 'sh', 'webcomplete')

    def gather_candidates(self, context):
        # context['is_async'] = True

        if not self._is_same_context(context['input']):
            log('Reset cache: %s' % context['input'])
            self.__last_input = context['input']
            self.__cache = None

        if self.__cache is not None:
            return self.__cache

        output = run(self.__script.split(), shell=True, stdout=PIPE).stdout
        candidates = output.decode('utf-8').splitlines()
        self.__cache = [{'word': word} for word in candidates]

        return self.__cache

    def _is_same_context(self, input):
        return self.__last_input and input.startswith(self.__last_input)
