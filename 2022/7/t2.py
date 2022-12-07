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


def populate_tree(commands):
    root = Node(dir=True)
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


class Solution:
    def __init__(self) -> None:
        self.res = 0
        self.props = {'dir', 'size', 'parent', 'path'}
        self.SIZE_LIMIT = 100000
        self.current_min = 70_000_000
        self.path = '/'

    def calculate_size(self, node):
        if not node: return 0
        if node.root['size']: return node.root['size']
        size = 0
        for prop in node.root.keys() - self.props:
            child = node.root[prop]
            if child.root['dir']:
                size += self.calculate_size(child)
            else:
                size += child.root['size']

        node.root['size'] = size
        if size < self.SIZE_LIMIT:
            self.res += size
        return size

    def find_node_to_delete(self, node):
        if not node: return
        if node['dir']:
            if self.current_min > node['size'] >= s.need:
                self.current_min = node['size']
                self.path = node['path']

            for prop in node.keys() - self.props:
                child = node[prop]
                self.find_node_to_delete(child.root)


input_filename = 'text.txt'
s = Solution()
with open(input_filename) as f_:
    commands = f_.readlines()
head = populate_tree(commands=commands)
s.calculate_size(head)
print(head.root['size'])
s.need = head.root['size'] - 40_000_000
print(s.need)
print('Sum of folder sizes:', s.res)
s.find_node_to_delete(head.root)
print('Folder to delete(size):', s.path, s.current_min)
