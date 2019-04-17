import textwrap

from nltk import compat
from nltk.tree import Tree
from nltk.util import LazyMap, LazyConcatenation
from nltk.tag import map_tag
from nltk.grammar import DependencyGrammar
from nltk.parse import (DependencyGraph, ProjectiveDependencyParser, NonprojectiveDependencyParser)


from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

class ConllCorpusReader(CorpusReader):

  ID = 'id'
  FORM = 'form'
  LEMMA = 'lemma'
  UPOS = 'upos'
  XPOS = 'xpos'
  FEATS = 'feats'
  HEAD = 'head'
  DEPREL = 'deprel'
  DEPS = 'deps'

  COLUMN = (ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS)
