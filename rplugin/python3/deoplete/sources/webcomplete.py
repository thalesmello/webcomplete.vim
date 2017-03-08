from .base import Base
import deoplete.util
from os.path import dirname, abspath, join, pardir
from subprocess import Popen, PIPE


class MockProcess(object):
    def terminate(self):
        pass


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.__last_input = None
        self.__cache = None
        self.__process = MockProcess()
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
            self.__process.terminate()
            process = Popen([self.__script], stdout=PIPE)
            self.__process = process
            self.__last_input = context['input']
            self.__cache = None

        if self.__cache:
            return self.__cache

        if self.__process.poll() is not None:
            context['is_async'] = False
            stdoutdata, _ = self.__process.communicate()
            candidates = stdoutdata.decode('utf-8').splitlines()
            self.__cache = candidates

            return [{'word': word} for word in candidates]

        return ['']

    def _is_same_context(self, input):
        return self.__last_input and input.startswith(self.__last_input)
