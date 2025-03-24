def busq_bina(S, target, low, high):
    
    if low > high:
        return False
    else:
        mid = (low + high)//2
        
        if S[mid] == target:
            return True
        elif target < S[mid]:
            return busq_bina(S, target, low, mid-1)
        else:
            return busq_bina(S, target, mid+1, high)
        
nume = [1,2,3]

if busq_bina(nume, 4, 0, len(nume)-1):
    print('si')
else:
    print('no')