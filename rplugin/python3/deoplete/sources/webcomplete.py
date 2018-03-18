'''Web completion of words for Neovim
This plugin works with Neovim and Deoplete, allowing you to
complete words from your Chrome instance in your editor.'''

from os.path import dirname, abspath, join, pardir, expandvars, expanduser
from subprocess import check_output, PIPE
from threading import Thread, Event

from .base import Base
import deoplete.util


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
        self.__refresh = Event()
        self.__thread = Thread(target=self.background_thread, daemon=True)
        self.__thread.start()

    def on_init(self, context):
        vars = context['vars']

        self.__script = expandvars(expanduser(
            vars.get('deoplete#sources#webcomplete#script', self.__script)))

    def background_thread(self):
        while True:
            self.__refresh.wait()
            self.__refresh.clear()
            output = check_output(self.__script, shell=True)
            candidates = output.decode('utf-8').splitlines()
            self.__cache = [{'word': word} for word in candidates]

    def gather_candidates(self, context):
        if not self._is_same_context(context['input']):
            self.__last_input = context['input']
            # The input has changed, notify background thread to fetch new words
            self.__refresh.set()

        if self.__cache is not None:
            # Return what we have now, though results may be a bit outdated
            context['is_async'] = False
            return self.__cache

        context['is_async'] = True
        return []

    def _is_same_context(self, input):
        return self.__last_input and input.startswith(self.__last_input)
