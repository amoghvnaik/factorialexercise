def factorial(number):
    for n in range(1, number):
        number = number/n
        if number > 1:
            n = n + 1
            continue
        elif number == 1:
            return(n)
            break
        else:
            return("NONE")
            break
            
print(factorial(119))
    
