def to_dec(binary):
    binary = binary[::-1]
    l = len(binary) - 1
    dec = 0

    while True:
        if l < 0:
            break
        dec += (int(binary[l]) * (2 ** l))
        l -= 1
    
    return dec * 17

def to_bin(dec):
    binary_arr = []
    
    while True:
        if dec < 2:
            binary_arr.append(dec)
            break
        
        binary_arr.append(dec % 2)
        dec //= 2
    
    return binary_arr[::-1]

def f():
    n = str(input())
    dec = to_dec(n)
    binary_arr = to_bin(dec)
    print(*binary_arr, sep='')

f()