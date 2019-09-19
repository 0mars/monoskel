from __future__ import annotations

import weakref
from _weakref import ReferenceType
from dataclasses import dataclass, field
from typing import List

@dataclass
class Graph:
    map: dict[int, Node] = field(default_factory=lambda: {})

    def add_node(self, data: int):
        self.map[data] = Node(data=data)

    def remove_node(self, id: int):
        self.map.pop(id)

    def find(self, id: int) -> Node:
        return self.map[id]

    def connect(self, id: int, to_id: int):
        from_node = self.find(id)
        to_node = self.find(to_id)
        from_node.add_edge(to_node)


@dataclass
class Node:
    data: int
    edges: List[ReferenceType] = field(default_factory=lambda: [])

    def add_edge(self, node: Node):
        self.edges.append(weakref.ref(node))

    def get_edges(self):
        return [edge for edge in self.edges if edge() is not None]


g = Graph()

g.add_node(1)
g.add_node(2)
g.add_node(4)

g.connect(1, 2)
g.connect(1, 4)

n1 = g.find(1)

print(n1.get_edges())

for ref in n1.get_edges():
    print(ref())

g.remove_node(2)

print(n1.get_edges())

for ref in n1.get_edges():
    print(ref())
