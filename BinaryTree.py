from Tree import Tree

class BinaryTree(Tree):
    
    def left(self, p):
        
        self.without_error()
        
    def right(self, p):
        
        self.without_error()
        
    def sibling(self, p):
        
        parent = self.parent(p)

        if parent is None:
            return None
        else:
            
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self, p):
        
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)