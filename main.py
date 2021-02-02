def countA(w):
    count = 0
    for i in range(len(w)):
        if w == "a":
            count = count + i
    
    return count 

print(countA("lucas"))