from .base import Base
import deoplete.util
from os.path import dirname, abspath, join, pardir
from subprocess import run, PIPE


class MockProcess(object):
    def terminate(self):
        pass


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
        context['is_async'] = True

        if not self._is_same_context(context['input']):
            self.__last_input = context['input']
            self.__cache = None

        context['is_async'] = False
        if self.__cache is not None:
            return self.__cache
        else:
            candidates = run(self.__script.split(), shell=True, stdout=PIPE).stdout.decode('utf-8').splitlines()
            self.__cache = [{'word': word} for word in candidates]

            return self.__cache

        return []

    def _is_same_context(self, input):
        return self.__last_input and input.startswith(self.__last_input)
