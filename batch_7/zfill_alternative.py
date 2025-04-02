#ask for number from 0-1000
number = int(input("Enter a number from 0-1000"))
if number < 1000:
    print("Not a valid number.")
    exit()
#count how many zeros u need to fill
zero_fill = 6 - len(number)
#combine the number of zeros and the number input
#print result