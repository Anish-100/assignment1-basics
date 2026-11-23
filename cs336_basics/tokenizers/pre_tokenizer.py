import regex as re
from collections.abc import Iterable

PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""


def pre_tokenize(words)-> Iterable:
    ''' Uses regex to pre-tokenize words'''
    return re.finditer(PAT, words)
