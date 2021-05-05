# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:07:41 2020

@author: hrith
"""
'''
        1
    2      3
      6  4      5


'''


class Node:
    def __init__(self,key):
        self.left=None
        self.right = None
        self.info = key
        self.dis = 0
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(5)
root.right.left = Node(4)
root.left.right = Node(6)

def top(root):
    if(root == None):
        return
    q = []
    x = dict()
    dis = 0
    root.dis = dis
    q.append(root)
    while(len(q)):
        root = q[0]
        dis = root.dis
        if dis not in x:
            x[dis] = root.info
        if(root.left):
            root.left.dis = dis -1
            q.append(root.left)
        if(root.right):
            root.right.dis = dis +1
            q.append(root.right)
        q.pop(0)
        #print(m)
    for i in sorted(x):
        print(x[i],end=" ")
top(root)