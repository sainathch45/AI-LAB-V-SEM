graph={
    'P':['S','R','Q'],
    'Q':{'P','R'},
    'R':['P','Q','T'],
    'T':['R'],
    'S':['P']
}
visited=[]
queqe=[]
def bfs(visited,graph,node):
    visited.append(node)
    queqe.append(node)
    while queqe:
        m=queqe.pop(0)
        print(m,end=" ")
        for i  in graph[m]:
            if i not in visited:
                visited.append(i)
                queqe.append(i)
print("Following is the breadth first search:")
bfs(visited,graph,'P')
