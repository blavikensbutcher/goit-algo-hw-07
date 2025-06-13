class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

#TASK 1
#TASK 1
#TASK 1
#TASK 1
# Max value is always the right one
def find_max_value(root):
    if root is None:
        return None
    if root.right is None:
        return root.val
    return find_max_value(root.right)

#TASK 2
#TASK 2
#TASK 2
#TASK 2
# Min value is always the left one
def find_min_value(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return find_min_value(root.left)

#TASK 3
#TASK 3
#TASK 3
#TASK 3

def find_sum(root):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)
    
    

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 12)
root = insert(root, 33)
root = insert(root, 55)
root = insert(root, 101)



max_value = find_max_value(root)
print(f'Max value of binary tree: {max_value}')

min_value = find_min_value(root)
print(f'Max value of binary tree: {min_value}')

sum = find_sum(root)

print(f'Sum of all values: {sum}')