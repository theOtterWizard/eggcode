from lark import Lark, Transformer
from pathlib import Path

grammar = Path('grammar.lark').read_text()

parser = Lark(grammar)

tree = parser.parse(Path('test.egc').read_text())

#class TreeToGcodeTree(Transformer):
    #def __init__(self):
        #self.variables = dict()
        #self.output = str()
    #def variable_declaration(self, items):
        #self.variable
