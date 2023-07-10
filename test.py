from lark import Lark
from lark.visitors import Interpreter
from lark.tree import Tree
from pathlib import Path

parser = Lark(Path('grammar.lark').read_text())

parsed_tree = parser.parse(Path('test.egc').read_text())

class Inter(Interpreter):
    def __init__(self):
        self._variables = dict()
        self._output = str()

    def expression(self, tree):
        if any([isinstance(child, Tree) for child in tree.children]):
            return self.visit_children(tree)
        else:
            return str(eval(''.join([str(self._variables[child.value]) if child.type == 'ID' else child.value for child in tree.children])))

    def while_loop(self, tree):
        result = list()
        while eval(self.visit(tree.children[0])):
            result += self.visit(tree.children[1])
        return result
    
    def code_block(self, tree):
        return self.visit_children(tree)

    def func_call(self, tree):
        pass

    def gcode(self, tree):
        if any([isinstance(child, Tree) for child in tree.children]):
            return ''.join(self.visit_children(tree))
        else:
            return ''.join([str(self._variables[child.value]) if child.type == 'ID' else child.value for child in tree.children])
    
    def variable_declaration(self, tree):
        self._variables[tree.children[0].value] = eval(tree.children[1].value)
    def variable_mutation(self, tree):
        var_id = tree.children[0].value
        operation = tree.children[1].value
        val = self.visit(tree.children[2]) if isinstance(tree.children[2], Tree) else tree.children[2].value
        if operation == "=": self._variables[var_id] = eval(val)
        elif operation == "+=": self._variables[var_id] += eval(val)
        elif operation == "-=": self._variables[var_id] -= eval(val)

print(parsed_tree.pretty())

i = Inter()
vis_res = i.visit(parsed_tree)
lines = list()

for i in vis_res:
    if isinstance(i, str): lines += [i]
    if isinstance(i, list): lines += filter(None, i)

print('\nresult:')
print(*lines, sep='\n')
