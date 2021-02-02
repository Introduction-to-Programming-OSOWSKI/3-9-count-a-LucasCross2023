def countA(w):
    count = 0
    for i in range(len(w)):
        if w[i] == "a":
            count =  i
    
    return count 

print(countA("rat"))