"""
USAGE: `python markov.py gettysburg.txt`
"""

import sys
import random


def open_and_read_file(filepath):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(filepath) as f:
        text = f.read()
    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")
       
    Each bigram will be a key in chains:
   
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'juanita'), ('there', 'mary')]
    
    Each item in chains is a list of all possible following words:
         
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    # To set a stop point, append None to the end of our word list.

    words.append(None)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    return chains


def make_text(chains):
    """Returns text from chains."""

    key = random.choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = random.choice(chains[key])

    #   Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = random.choice(chains[key])

    return " ".join(words)


if __name__ == '__main__':
    # Read the specified file into a string
    input_text = open_and_read_file(sys.argv[1])

    # Get a Markov chain & generate random text
    chains = make_chains(input_text)
    random_text = make_text(chains)
    print(random_text)
