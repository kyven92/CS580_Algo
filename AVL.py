# AVL tree implementation in Python


import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key,root_index=1,root_node=None,out_list=[]):

        inserted = False
        # root_node=None
        if root_index==1:
            root_node = root


        # Find the correct location and insert the node
        if not root:
            inserted = True

            return inserted,TreeNode(key)
        elif key < root.key:
            inserted,root.left = self.insert_node(root.left, key,root_index+1,root_node,out_list)
            
        else:
            inserted,root.right = self.insert_node(root.right, key,root_index+1,root_node,out_list)
            

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
       
        if inserted :
            # print("##### Before")
            self.printLevelOrder(root_node,[float('inf')]*32)
            # self.printHelper(root_node,"",True)

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return inserted,self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return inserted,self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return inserted,self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return inserted,self.leftRotate(root)
        

        return False,root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
    

    def height(self,node): 
        if node is None: 
            return 0 
        else : 
            # Compute the height of each subtree  
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 

            #Use the larger one 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1

    # Function to  print level order traversal of tree 
    def printLevelOrder(self,root,out_list): 
        h = self.height(root)
        root_index =1 
        for i in range(1, h+1): 
            self.printGivenLevel(root, i,out_list,root_index) 
        print(f"{out_list}",end="$")


    # Print nodes at a given level 
    def printGivenLevel(self,root , level,out_list,level_index): 
        if root is None: 
            return
        if level == 1: 
            # print(f"{root.key} at index {level_index}")
            # out_list.append(root.key)
            out_list[level_index-1]=root.key
            # print(f"$$$$### AVL List after adding: {root.key} \n{out_list}")


        elif level > 1 : 
            self.printGivenLevel(root.left , level-1,out_list,(level_index)*2) 
            self.printGivenLevel(root.right , level-1,out_list,2*(level_index)+1) 


myTree = AVLTree()
root = None
# nums = [33, 13, 52, 9, 21, 61, 8, 11]
nums = [3,14,27,31,39,42,55,70,74,81,85,93,98]


for index,num in enumerate(nums):
    # if index!=0:
    print(f"Adding Element {num} ",end="$")
    out_list=[float('inf')]*32
    inserted,root = myTree.insert_node(root, num,out_list=out_list)
    # print(f"### After: ")
    # myTree.printHelper(root,"",True)
    # if index!=0:
    myTree.printLevelOrder(root,out_list)
    print("\n")

    # print("#### END")
myTree.printHelper(root, " ", True)
# myTree.printLevelOrder(root,out_list)


# key = 13
# root = myTree.delete_node(root, key)
# print("After Deletion: ")
# myTree.printHelper(root, "", True)