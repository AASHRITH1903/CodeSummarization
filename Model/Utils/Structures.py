class Node:
    def __init__(self, id:int):
        self.id = id
        self.children = []
        self.label = None
        self.emb = None
        self.h = None
        self.c = None
        self.out = None
    
    def add_children(self, children):
        
        self.children.extend(children)
    
    def add_child(self, child):

        self.children.append(child)
        