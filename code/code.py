def factorial(number):
    for n in range(1, number):
        numberx = number/n
        if numberx > 1:
            n = n + 1
            continue
        elif numberx == 1:
            return(n)
            break
        else:
            return("NONE")
            break
            
print(factorial(6))
    
