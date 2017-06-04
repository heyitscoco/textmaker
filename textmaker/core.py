import os
import markov
from abc import abstractmethod
from dictmerge import dictmerge

class TextMaker():

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def make_text(self):
        pass


class MarkovMaker(TextMaker):

    def __init__(self):
        self._meta = dict()

    def train(self, filepath, **src_meta):
        with open(filepath) as f:
            text = f.read()
        filename = filepath.split(os.sep)[-1]
        self._meta["source"] = dictmerge({
            "filename": filename,
            "length": len(text)
        }, src_meta)
        self.chains = markov.make_chains(text)

    def make_text(self, return_meta=False):
        if not hasattr(self, "chains"):
            raise RuntimeError("`train` must be called before `make_text`.")

        text = markov.make_text(self.chains)
        if return_meta:
            meta = self._meta
            return (text, meta)
        return text
