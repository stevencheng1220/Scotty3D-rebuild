# Helper function to add edges to the graph
def add_edge(graph, start, end):
    if start not in graph:
        graph[start] = {"out": [], "in": []}
    if end not in graph:
        graph[end] = {"out": [], "in": []}
    graph[start]["out"].append(end)
    graph[end]["in"].append(start)


# Read the .dot file and create a directed graph from it
def read_dot_file(file_path):
    graph = {}
    with open(file_path, "r") as file:
        for line in file:
            if "->" in line:  # This line denotes an edge
                parts = line.split("->")
                start = parts[0].strip().strip('"')
                end = parts[1].strip().strip('";\n')
                add_edge(graph, start, end)
    return graph


# List nodes by in-degree
def list_nodes_by_indegree(graph):
    return sorted(graph.items(), key=lambda item: len(item[1]["in"]))


# Main function
def main():
    file_path = "/Users/stevencheng/MyStuff/CodingProjects/Scotty3D-rebuild/src/file_deps.dot"  # Change this to your .dot file path
    graph = read_dot_file(file_path)
    sorted_nodes = list_nodes_by_indegree(graph)

    # Print nodes and their in-degree
    for node, edges in sorted_nodes:
        print(f"Node: {node}, In-Degree: {len(edges['in'])}")


if __name__ == "__main__":
    main()
