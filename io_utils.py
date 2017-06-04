import os


def read_text(filename):
    path = os.sep.join(["texts", filename])
    with open(path) as f:
        text = f.read()
    return text
