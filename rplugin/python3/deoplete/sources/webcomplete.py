from .base import Base
import deoplete.util
from os.path import dirname, abspath, join, pardir
from subprocess import check_output


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'webcomplete'
        self.kind = 'keyword'
        self.mark = '[web]'
        self.rank = 4
        filedir = dirname(abspath(__file__))
        projectdir = abspath(join(filedir, pardir, pardir, pardir, pardir))
        self.__script = join(projectdir, 'sh', 'webcomplete')

    def gather_candidates(self, context):
        candidates = check_output([self.__script]).decode('utf-8').splitlines()
        return [{'word': word} for word in candidates]
