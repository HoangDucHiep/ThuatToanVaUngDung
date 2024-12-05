from queue import queue

def is_palindrome(str):
    str = str.lower()
    arr = list(str)
    q = queue();
    
    for i in arr:
        q.enqueue(i)
    
    while q.size() > 1:
        for i in range(q.size() - 1):
            q.enqueue(q.dequeue())
        
        a = q.dequeue()
        b = q.dequeue()
        if a != b:
            print("Not a palindrome")
            return False
            
    print("Is a palindrome")
    

is_palindrome("asdfgfd")
