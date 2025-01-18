num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, int (num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not an armstrong number") 
            break
        else:
            print(f"{num} is not an armstrong number")
        #else:
            #print(f"{num} is an armstrong number")