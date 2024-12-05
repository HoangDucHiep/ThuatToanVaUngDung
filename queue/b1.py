from queue import queue

def str_seq(str, n):
    q = queue()
    for i in str:
        q.enqueue(i)
        
    for i in range(n):
        q.enqueue(q.dequeue())
    
    res = ""
    while not q.isEmpty():
        res += q.dequeue()
    return res

#main
print(str_seq("abcdef", 2))
