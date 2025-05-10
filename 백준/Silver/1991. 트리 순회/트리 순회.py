N = int(input().strip())

tree = {}

for _ in range(N):
    parent, left, right = input().strip().split()
    tree[parent] = (left,right)

def preorder(node):
    if node == ".":
        return
    print(node,end='')
    preorder(tree[node][0]) #왼
    preorder(tree[node][1]) #오

def inorder(node):
    if node == ".":
        return
    
    inorder(tree[node][0]) #왼
    print(node,end='') #부
    inorder(tree[node][1]) #오

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])#왼
    postorder(tree[node][1])#오
    print(node,end='')#부

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()



