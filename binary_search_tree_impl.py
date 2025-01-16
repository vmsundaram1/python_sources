
class Node:
 
 # type=0 is for representing operator, type=1 is for representing value

 def __init__(self, type=0, val=None, left=None, right=None):
  self.type=type
  self.val=val
  self.left=left
  self.right=right

 def __str__(self):
  left_str,right_str='',''
  if self.left:
   left_str=self.left.__str__()
  if self.right:
   right_str=self.right.__str__()  

  return f"{self.type}:{self.val} --> ({left_str} < > {right_str})"

 def __strOne__(self,indent=''):
  left_str,right_str='',''
  
  if self.left:
   left_str=indent+self.left.__strOne__(indent+'		')
  if self.right:
   right_str=indent + self.right.__strOne__(indent+'		')

  return "%s%s --> \n %s \n %s" % (indent,self.val,left_str,right_str)


 def evaluate(self):
  type=self.type
  val=self.val
  if(type==1):
   return val
  else:
   l,r=None,None
   if self.left:
    l=self.left.evaluate()
    print(l)
   if self.right:
    r=self.right.evaluate()
   if(val=='*'):
    print(l*r)
    return l*r
   elif(val=='/'):
    return l/r
   elif(val=='+'):
    return l+r
   elif(val=='-'):
    return l-r
   elif(val=='^'):
    return l**r

 def insert(self,node):
  if( node.val < self.val):
   if(self.left==None):
    print("I am in direct left")
    self.left=node
   else:
    print("I am in the internal left")
    self.left.insert(node)
  else:
   if(self.right==None):
    print("I am in direct right")
    self.right=node
   else:
    print("I am in internal right")
    self.right.insert(node)

 def find(self,val):
  if(self.val==val):
   return self
  elif(val < self.val):
   if(self.left==None):
    return None
   else:
     return self.left.find(val)
  else:
    if(self.right==None):
     return None
    else:
     return self.right.find(val)

# Function Definition to delete the Node of a Binary Tree

def delete_deepest_node(root,del_Node):
 print("The value of deletion node is",del_Node.val)
 queue=[root]

 while queue:
  curr_node = queue.pop(0)
  if(curr_node == del_Node):
   curr_node=None
   del del_Node
   return 

  if curr_node.right:
   if(curr_node.right == del_Node):
     curr_node.right=None
     del del_Node
     return 
   queue.append(curr_node.right)
   
  if curr_node.left:
   if(curr_node.left == del_Node):
     curr_node.left=None
     del del_Node
     return 
   queue.append(curr_node.left)

# Function to delete the node with the given key

def deletion(root,key):
 if root is None:
  return None
 
 if root.left is None and root.right is None:
  if root.val==key:
   return None
  else:
   return root
 
 queue = [root]
 curr_node=None
 keyNode=None
 
# T0 find the deepest node for replacing the To-be deleted node

 while queue:
  curr_node = queue.pop(0)

  print(curr_node.val)
  
  if curr_node.val == key:
   print(key,curr_node.val)
   keyNode = curr_node
  
  if curr_node.left:
   queue.append(curr_node.left)

  if curr_node.right:
   queue.append(curr_node.right)

#  Move the data from Deepest Node to keyNode once keyNode is found

 if keyNode is not None:

  x = curr_node.val

  print("Deepest Node value on the right is", x)

  print("Before",keyNode.val)

  keyNode.val = x

  print("After",keyNode.val)

  delete_deepest_node(root,curr_node)

 return root

def inorder(curr):
 if curr is None:
  return
 inorder(curr.left)
 print(curr.val, end=" ")
 inorder(curr.right)


class BST:
 
 def __init__(self):
  self.root=None

 def insert(self,val):
  n = Node(1,val)
  if self.root==None:
   self.root=n
  else:
   self.root.insert(n)

 def find(self,val):
  if self.root==None:
   return None
  else:
   self.root.find(val)
  
 def delete_node(self,root,key):
  if self.root==None:
   return None
  else:
   self.root=deletion(root, key) 
   return self.root

# Main Program Starts

# For Evaluating an Expression

#_2 = Node(type=1,val=2)
#_3 = Node(type=1,val=3)
#_mul= Node(type=0,val='*',left=_2,right=_3)
#_4 = Node(type=1, val=4)

#tree = Node(type=0,val='+',left=_mul,right=_4)

# For forming a tree elements of integers and inserting an element

_2=Node(type=1,val=2)
_3=Node(type=1,val=3)

tree=Node(type=1,val=4, left=_2, right=_3)

print(tree.__str__())
print(tree.__strOne__())


# Evaluate an Expression using Binary Tree Method

c=tree.evaluate()

print("The value of expression evaluates using Binary Tree is",c)


# Create new Nodes and Insert them into tree appropriately

_5 = Node(type=1,val=5)
_4 = Node(type=1,val=1)
_temp=Node(type=1,val=3)
_temp1=Node(type=1,val=0)
_temp2=Node(type=1,val=7)
_tempp=Node(type=1,val=1)

tree.insert(_5)
#tree.insert(_4)
#tree.insert(_temp)

#tree.insert(_temp2)
#tree.insert(_temp1)
#tree.insert(_temp)
#tree.insert(_tempp)
#tree.insert(_temp1)
#print(tree.__strOne__())

n = tree.find(1)
if(n!=None):
 print("Found the node with val",n.val)
 print(n.__strOne__())
else:
 print("Could not Find the node with val")

check_val=9
n = tree.find(check_val)

if(n!=None):
 print("Found the node with val",n.val)
 print(n.__strOne__())
else:
 print("Could not Find the node with val")

obj_bst = BST()

obj_bst.insert(30)

obj_bst.insert(check_val)
obj_bst.insert(check_val*2)
obj_bst.insert(check_val*3)

print("ROOT is",obj_bst.root)
print("The BST tree is",obj_bst.root.__strOne__())


    # Construct the binary tree
    #       10         
    #      /  \       
    #    11    9
    #   / \   / \     
    #  7  12 15  8     
 

root = Node(1,10)
root.left = Node(1,11)
root.right = Node(1,9)
root.left.left = Node(1,7)
root.left.right = Node(1,12)
root.right.left = Node(1,15)
root.right.right = Node(1,8)

inorder(root)


key = 11
root = obj_bst.delete_node(root,key) 

inorder(root)




