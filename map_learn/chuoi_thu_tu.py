



container = dict();

str = "Hello, my name is Nam. I am 20 years old. I am a student. I am studying at the University of Science, VNU-HCM. I am in the second year. I am studying Computer Science. I am interested in programming. I am learning Python. I am learning about data structures and algorithms. I am learning about the map data structure. I am learning about the map data structure implementation. I am learning about the map data structure implementation using Python. I am learning about the map data structure implementation using Python programming language."

words = list(str)

for word in words:
    if word in container:
        container[word] += 1
    else:
        container[word] = 1
        
print(container)