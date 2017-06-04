import os
import markov
import frontmatter
from abc import abstractmethod
from dictmerge import dictmerge

class TextMaker():

    def __init__(self):
        self._meta = dict()

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def make_text(self):
        pass


class MarkovMaker(TextMaker):

    def train(self, filepath):
        file = frontmatter.load(filepath)
        filename = filepath.split(os.sep)[-1]
        self._meta["source"] = dictmerge(file.metadata, filename=filename)
        self.chains = markov.make_chains(file.content)

    def make_text(self, return_meta=False):
        if not hasattr(self, "chains") or not hasattr(self, "_meta"):
            raise RuntimeError("`train` must be called before `make_text`.")

        text = markov.make_text(self.chains)
        if return_meta:
            meta = self._meta
            return (text, meta)
        return text
