from main import *

# reading input
state = []

for i in xrange(0, HEIGHT):
    line = raw_input()
    state.append(line.split(' '))

player = raw_input()

# tests
node = Node(0, state, 1)

node.populate_children()

for child in node.children.values():
    print child.value
