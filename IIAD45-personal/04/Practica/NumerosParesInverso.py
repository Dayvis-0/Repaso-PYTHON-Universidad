def num_pare_inv(n, s=0):
    
    if n > 0:
        num_pare_inv(n-1, s+2)
        print(s)
    
num_pare_inv(2)