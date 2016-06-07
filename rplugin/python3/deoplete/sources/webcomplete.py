from .base import Base

import deoplete.util


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'webcomplete'
        self.kind = 'keyword'
        self.mark = '[web]'
        self.rank = 4

    def gather_candidates(self, context):
        return [{'word': word} for word in
                self.vim.call('webcomplete#gather_candidates')]
