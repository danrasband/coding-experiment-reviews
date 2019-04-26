# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
class Node: 
       
    def __init__(self): 
        self.children = [None]*26
  
        self.isLeaf = False
  
class Trie: 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self):  
        return Node() 
  
    def charIndex(self,ch):
        return ord(ch)-ord('a') 
  
  
    def insert(self,key): 
          
        
        now = self.root 
        length = len(key) 
        for i in range(length): 
            index = self.charIndex(key[i]) 
   
            if not now.children[index]: 
                now.children[index] = self.getNode() 
            now = now.children[index] 
  
        now.isLeaf = True

def count(root):
    ans =0
    for child in root.children:
        if child!=None:
            ans+=1

    return ans

def find(root):
    ind=0
    for child in root.children:
        if child!=None:
            return ind
        ind+=1

def solution(root):
    now = root
    found=''

    while count(root)==1:
        found = char(find(root)+65)

        root = root.children[0]

    return found
    
    