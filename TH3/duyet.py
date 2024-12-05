from collections import deque


def nonrecur_dfs(adj_list, start):
    visited = [False] * len(adj_list)   #Create a list to mark visited vertex
    stack = []                          #stack to implement non-recur method
    
    res = []                       #traversed verties
    stack.append(start)
    
    #while there are still something in the stack
    while stack:
        curr = stack.pop()          #take the last one
        if not visited[curr]:      
            visited[curr] = True 
            res.append(curr)     
            
            for adj_vertex in reversed(adj_list[curr]):
                if not visited[adj_vertex]:
                    stack.append(adj_vertex)
    return res


def recur_dfs(adj_list, start, visited=None):
    if visited is None:
        visited = [False] * len(adj_list)

    res = []
    
    visited[start] = True
    res.append(start)

    for adj in adj_list[start]:
        if not visited[adj]:
            res.extend(recur_dfs(adj_list, adj, visited))
            
    return res


def bfs(adj_list, start):
    #set up
    visited = [False] * len(adj_list)
    res = []
    queue = []
    
    queue.append(start)
    
    while len(queue) > 0:
        curr = queue.pop(0)
        
        if not visited[curr]:
            res.append(curr)
            visited[curr] = True
            for adj_vertex in adj_list[curr]:
                if not visited[adj_vertex]:
                    queue.append(adj_vertex)
        
    return res
    
    
if __name__ == "__main__":
    
    adj_list_dgraph = [
        [2, 3, 1],
        [3, 4],
        [5],
        [2, 5, 6],
        [3, 6],
        [],
        [5]
    ]

    print("----depth first search----")
    print(nonrecur_dfs(adj_list_dgraph, 0))
    print(recur_dfs(adj_list_dgraph, 0))


    print("----breath first search----")
    print(bfs(adj_list_dgraph, 0))