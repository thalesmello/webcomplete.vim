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
        self.__last_process = MockProcess()
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
            self.__last_process.terminate()
            process = Popen([self.__script], stdout=PIPE)
            self.__last_process = process

        if self.__last_process.poll() is not None:
            self.print('here')
            context['is_async'] = False
            stdoutdata, _ = self.__last_process.communicate()
            candidates = stdoutdata.decode('utf-8').splitlines()
            return [{'word': word} for word in candidates]

        return []

    def _is_same_context(self, input):
        return self.__last_input and input.starts_with(self.__last_input)
