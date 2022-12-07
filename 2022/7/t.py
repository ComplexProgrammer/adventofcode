from os import name


class Node:
    def __init__(self, size=0, parent=None, dir=False, path='/', **kwargs) -> None:
        self.root = {
            'size': size,
            'parent': parent,
            'dir': dir,
            'path': path,
            **kwargs,
        }

    def __repr__(self) -> str:
        return self.root['path']


class Trie:
    def __init__(self) -> None:
        self.root = Node(dir=True)


class Solution:
    def __init__(self) -> None:
        self.res = 0
        self.props = {'dir', 'size', 'parent', 'path'}
        self.SIZE_LIMIT = 100000

    def populate_tree(self, commands):
        root = Trie().root
        for command in commands:
            inp = command.split()
            if inp[0] == '$':
                cmd = inp[1]
                if cmd == 'cd':
                    path = inp[-1]
                    if path == '..':
                        node = node.root['parent']
                    elif path == '/':
                        node = root
                    else:
                        node = node.root[path]
            else:
                if inp[0] == 'dir':
                    node.root[inp[1]] = Node(
                        size=0, parent=node, dir=True, path=inp[1]
                    )
                else:
                    node.root[inp[1]] = Node(
                        size=int(inp[0]), parent=node, dir=False, path=inp[1]
                    )
        return root

    def calculate_size(self, node):
        if not node: return 0
        if node.root['size']: return node.root['size']
        size = 0
        for prop in node.root.keys() - self.props:
            child = node.root[prop]
            print(child.root)
            if child.root['dir']:
                size += self.calculate_size(child)
            else:
                size += child.root['size']
        print(size)
        node.root['size'] = size
        if size < self.SIZE_LIMIT:
            self.res += size
        return size


input_filename = 'text.txt'
s = Solution()
with open(input_filename) as f_:
    commands = f_.readlines()
print(commands)
head = s.populate_tree(commands=commands)
print(head)
s.calculate_size(head)
print(s.res)