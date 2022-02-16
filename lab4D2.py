def myFunc(num,num2):
    if num < 0 and num2 < 0:
        if num < num2:
            Nnums = range(num, num2+1)
            for numbers in Nnums:
                print(numbers)
    else:
        print("The numbers should be negative")

myFunc(-15,-4)
   


