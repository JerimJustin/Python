print("Simple Calculator")
print("Operations")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Square")
print("6.Cube")
cond = True

while(cond==True):
    ch = int(input("Select operation number:"))
    if (ch == 1):
        inputvals = input("Enter the numbers to be added: ")
        nums = list(map(int,inputvals.split(" ")))
        total = 0
        for num in nums:
            total+=num
        print("Sum =",total)
        
    elif (ch == 2):
         inputvals = input("Enter the numbers to be subtracted: ")
         nums = list(map(int,inputvals.split(" ")))
         nums.sort()
         nums.reverse()
         dif = nums[0]
         for i in range(1,len(nums)):
             dif -=nums[i]
         print("Difference =",dif)
         
    elif (ch == 3):
        inputvals = input("Enter the numbers to be multiplied: ")
        nums = list(map(int,inputvals.split(" ")))
        prod = 1
        for num in nums:
            prod *= num
        print("Product =",prod)
        
    elif (ch == 4):
        print("1.Proper Division")
        print("2.Fractional Division")
        ch = int(input("Enter the choice: "))
        if (ch == 1):
             inputvals = input("Enter the numbers to be Divided: ")
             nums = list(map(int,inputvals.split(" ")))
             nums.sort()
             nums.reverse()
             quot = nums[0]
             for i in range(1,len(nums)):
                 quot /= nums[i]
             print("Quotient =",quot)
        elif (ch == 2):
            num1 = int(input("Enter the Divident: "))
            num2 = int(input("Enter the Divisor: "))
            quot = num1/num2
            print("Quotient =",quot)
        else:
            print("Invalid Choice")
            
    elif (ch == 5):
        num = int(input("Enter the number to be squared: "))
        sq = num**2
        print("Square of",num,"=",sq)

    elif (ch == 6):
        num = int(input("Enter the number to be cubed: "))
        cb = num**3
        print("Cube of",num,"=",cb)
        
    else:
        print("Invalid Selection")
    ch2 = input("Do you want to continue?(Y/Q) ")
    if (ch2=="Y" or ch2=="y" or ch2=="YES" or ch2=="Yes" or ch2=="yes"):
        cond = True
    else:
        cond = False
        print("Program Completed")
        
