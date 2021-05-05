# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:22:05 2020

@author: hrith
"""
'''
                        top
                        
                        1
                    2        3
                4      5 8      9
                            11      10
                
'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key




class P:
    def __init__(self):
        self.l = 0
        self.r = 0
    
    
    def level(self, root):
        if root:
            if(root.left != None and self.l >= 0):
                self.l = self.l + 1
                self.level(root.left)
            
            print(root.val)
            self.l = self.l - 1
            
            if(root.right != None and self.l < 0):
                self.l = self.l -1
                self.level(root.right)
            
        
    
    
    def top(self,root):
        if root:
            if(root.left):
                root.left.right = None
                self.top(root.left)
            if(root.right):
                root.right.left = None
                self.top(root.right)

    def pre(self,root):
        if root:
            print(root.val)
            self.pre(root.left)
            self.pre(root.right)
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
a = P()
#a.top(root)
#a.pre(root)
a.level(root)