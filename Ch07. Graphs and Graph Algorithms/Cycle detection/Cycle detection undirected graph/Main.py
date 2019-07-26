from Graph import Graph

graph = Graph()

vertices = ["a", "b", "c", "d"]
for vertex in vertices:
    graph.add_vertex(vertex)


graph.add_edge("a", "b")
graph.add_edge("b", "c")
graph.add_edge("c", "d")
graph.add_edge("d", "b")

graph.dfs("a")

print(graph.print_path("c"))






