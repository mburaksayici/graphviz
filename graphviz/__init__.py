# graphviz - create dot, save, render, view

"""Assemble DOT source code and render it with Graphviz.

>>> dot = Digraph(comment='The Round Table')

>>> dot.node('A', 'King Arthur')
>>> dot.node('B', 'Sir Bedevere the Wise')
>>> dot.node('L', 'Sir Lancelot the Brave')

>>> dot.edges(['AB', 'AL'])

>>> dot.edge('B', 'L', constraint='false')

>>> print(dot)  #doctest: +NORMALIZE_WHITESPACE
// The Round Table
digraph {
    A [label="King Arthur"]
    B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
"""

from .dot import Graph, Digraph
from .files import Source
from .lang import escape, nohtml
from .backend import (render, pipe, version, view,
                      ENGINES, FORMATS, RENDERERS, FORMATTERS,
                      ExecutableNotFound, RequiredArgumentError)

__all__ = [
    'Graph', 'Digraph',
    'Source',
    'escape', 'nohtml',
    'render', 'pipe', 'version', 'view',
    'ENGINES', 'FORMATS', 'RENDERERS', 'FORMATTERS',
    'ExecutableNotFound', 'RequiredArgumentError',
    'set_default_engine', 'set_default_format',
]

__title__ = 'graphviz'
__version__ = '0.15.1.dev0'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'MIT, see LICENSE.txt'
__copyright__ = 'Copyright (c) 2013-2020 Sebastian Bank'

#: Set of known layout commands used for rendering (``'dot'``, ``'neato'``, ...)
ENGINES = ENGINES

#: Set of known output formats for rendering (``'pdf'``, ``'png'``, ...)
FORMATS = FORMATS

#: Set of known output formatters for rendering (``'cairo'``, ``'gd'``, ...)
FORMATTERS = FORMATTERS

#: Set of known output renderers for rendering (``'cairo'``, ``'gd'``, ...)
RENDERERS = RENDERERS

ExecutableNotFound = ExecutableNotFound

RequiredArgumentError = RequiredArgumentError


def set_default_engine(engine):
    if engine not in ENGINES:
        raise ValueError('unknown engine: %r' % engine)

    from .files import Base

    old_default_engine = Base._engine
    Base._engine = engine
    return old_default_engine


def set_default_format(format):
    if format not in FORMATS:
        raise ValueError('unknown format: %r' % format)

    from .files import Base

    old_default_format = Base._format
    Base._format = format
    return old_default_format
