import os

def uso_disc(path):
    
    total = os.path.getsize(path)
    
    if os.path.isdir(path):
        
        for file in os.listdir(path):
            child = os.path.join(path, file)
            total += uso_disc(child)
            
    return total

