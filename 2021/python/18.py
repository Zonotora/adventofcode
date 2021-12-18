# flake8: noqa

from python import *
import math

aoc = AdventOfCode("2021", "18", "Snailfish", new)


class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


    def __repr__(self):
        return f"[{self.left},{self.right}]"
    

    @staticmethod
    def add(node1, node2):
        root = Node()
        node1.parent = root
        node2.parent = root
        root.left = node1
        root.right = node2
        return root


    def reduce(self):
        while True:
            while self.explode(0): 
                continue
            if not self.split():
                break
        return self

    def rightmost(self, value):
        parent = self.parent
        if parent is None:
            return

        if parent.left == self:
            parent.rightmost(value)
        else:
            if isinstance(parent.left, Node):
                node = Node.rightmost_(parent.left)
                node.right += value
            else:
                parent.left += value

    @staticmethod
    def rightmost_(node):
        if isinstance(node.right, Node):
            return Node.rightmost_(node.right)
        return node

    def leftmost(self, value):
        parent = self.parent
        if parent is None:
            return

        if parent.right == self:
            parent.leftmost(value)
        else:
            if isinstance(parent.right, Node):
                node = Node.leftmost_(parent.right)
                node.left += value
            else:
                parent.right += value

    @staticmethod
    def leftmost_(node):
        if isinstance(node.left, Node):
            return Node.leftmost_(node.left)
        return node

    def explode(self, depth):
        changes = False
        if not isinstance(self.left, Node) and not isinstance(self.right, Node) and depth >= 4:
            # find neighbours
            self.rightmost(self.left) 
            self.leftmost(self.right)
            if self.parent.left == self:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return True

        if isinstance(self.left, Node): 
            changes = changes or self.left.explode(depth + 1)

        if isinstance(self.right, Node): 
            changes = changes or self.right.explode(depth + 1)

        return changes
    
    def split(self):
        if not isinstance(self.left, Node): 
            if self.left >= 10:
                node = Node.split_(self.left)
                node.parent = self
                self.left = node
                return True

        if isinstance(self.left, Node): 
            if self.left.split():
                return True

        if not isinstance(self.right, Node): 
            if self.right >= 10:
                node = Node.split_(self.right)
                node.parent = self
                self.right = node
                return True

        if isinstance(self.right, Node): 
            if self.right.split():
                return True
        
        return False


    @staticmethod
    def split_(node):
        v = node / 2
        new_node = Node()
        new_node.left = math.floor(v)
        new_node.right = math.ceil(v)
        return new_node


    def magnitude(self):
        left, right = 0, 0
        if isinstance(self.left, Node):
            left = self.left.magnitude()
        else:
            left =  self.left
        if isinstance(self.right, Node):
            right = self.right.magnitude()
        else:
            right = self.right

        return 3 * left + 2 * right
        


def parse(s):
    root = None
    node = None
    for c in s:
        if c == "[":
            if root is None:
                root = Node()
                node = root
            else:
                new_node = Node()
                new_node.parent = node
                if node.left is None:
                    node.left = new_node
                    node = node.left
                else:
                    node.right = new_node
                    node = node.right
        elif c == "]":
            node = node.parent
        elif c == ",":
            continue
        else:
            if node.left is None:
                node.left = int(c)
            else:
                node.right = int(c)

    return root


@aoc.part(1)
def part1(items):
    nodes = [None] * len(items)
    for i, item in enumerate(items):
        node = parse(item)
        nodes[i] = node

    for i in range(1, len(nodes)):
        supernode = Node.add(nodes[i-1], nodes[i])
        nodes[i] = supernode.reduce()
    return supernode.magnitude()


@aoc.part(2)
def part2(items):
    nodes = [None] * len(items)
    for i, item in enumerate(items):
        node = parse(item)
        nodes[i] = node

    ans = 0
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue
            n1 = parse(items[i]) 
            n2 = parse(items[j]) 
            a = Node.add(n1, n2).reduce().magnitude()
            ans = max(a, ans)
    return ans  

if __name__ == "__main__":
    aoc.solve()
