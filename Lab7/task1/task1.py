############################# Task 1 #################################
######################################################################
#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task1/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

t=list(map(int,inp.readline().split()))  

parent=[0]*(t[0]+1)
size=[0]*(t[0]+1)

def make_set(vertex):
    parent[vertex]=vertex
    size[vertex]=1

def find_parent(vertex):
    if parent[vertex]==vertex:
        return vertex
    parent[vertex] = find_parent(parent[vertex])
    return parent[vertex]

def union_set(x,y):
    x=find_parent(x)
    y=find_parent(y)
    if x!=y:
        if size[x]<size[y]:
            temp=x
            x=y
            y=temp

        parent[y]=x
        size[x]+=size[y]
    out.write(str(size[x])+"\n")

for size in union_set(parent, t):
    print(size)



