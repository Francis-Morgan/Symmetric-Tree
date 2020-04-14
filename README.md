# Symmetric-Tree
**Task**: [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

**About task**: Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [8,12,12,14,10,10,14,15,13,11,9,9,11,13,15] is symmetric:

![](https://github.com/Francis-Morgan/Symmetric-Tree/blob/master/symetric%20tree/example.png)
   
## Solution idea

We're gonna do a paralel round of the branches of the tree. 
We compare the values, and if they match, we go further, if not, we return False.
Logically, we'll be comparing elements that are symmetrical to the center. That is, the extreme left and the extreme right, and so on.  

## Code explanation 

[There](https://github.com/Francis-Morgan/Symmetric-Tree/blob/master/Symetric_tree.py) you can see program.

Firstly, we check a root of binary tree. If it has the None type - return True, because it tree is empty.
```python
     if root is None:
         return True
```         
If our binary tree isn't empty - call a function **_check_** and pass it on to the sub-tree roots as parameters.
```python
    return check(root.left,root.right)
```    
This is function:
```python
    def check(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return check(left.left, right.right) and check(left.right,right.left)
```
Now let's get to the function.

First condition checks nodes. If root our isn't have descendants, we will return True. We've reached the leaves of the tree.

Second condition helps us check the size of the two subtrees. If they have not the same depth, the function will return False.

With 3 conditions we check the node values. If they haven't the same values, return False.

If the last condition is fulfilled, we will recursively call the function until we come across leaves or different elements.

## How does the program work by example

![](https://github.com/Francis-Morgan/Symmetric-Tree/blob/master/symetric%20tree/example2.png) 

Our program return False. Function **__check__** will be called recursively until it reaches the wrong nodes and falls into this condition:
```python
 elif left.val != right.val:
                return False

```
Then, as the stack is released, the False value will return.

## Input/Output

![](https://github.com/Francis-Morgan/Symmetric-Tree/blob/master/symetric%20tree/output.PNG)

## Test program

![](https://github.com/Francis-Morgan/Symmetric-Tree/blob/master/symetric%20tree/Complexity.PNG)
