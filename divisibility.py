def divis(n):
    if n==2:
        print ('A number is divisible by 2 if the last digit is 2, 4, 6 or 8.')
    elif n==3:
        print ('A number is divisible by 3 if the sum of the digits is a multiple of 3.')
    elif n==4:
        print ('A number is divisible by 4 if the last 2 digits together are divisible by 4.')
    elif n==5:
        print ('A number is divisible by 5 if the last digit is 0 or 5.')
    elif n==6:
        print ('A number is divisible by 6 if it is divisible by 3 and 2.')
    elif n==7:
        print ('A number is divisible by 7 if you take the last digit, double it, and subtract it from the remaining number, if the resulting number is divisible by 7.')
    elif n==8:
        print ('A number is divisible by 8 if the last 3 digits together are divisible by 8.')
    elif n==9:
        print ('A number is divisible by 9 if the sum of the digits are divisible by 9.')
    elif n==10:
        print ('A number is divisible by 10 if the last digit is 0.')
    elif n==11:
        print ('A number is divisible by 11 if when you take the last digit and subtract it from the remaining number, if that is a multiple of 11.')
    elif n==12:
        print ('A number is divisible by 12 if it is divisible by 3 and 4.')
divis(1)
divis(2)
divis(3)
divis(4)
divis(5)
divis(6)
divis(7)
divis(8)
divis(9)
divis(10)
divis(11)
divis(12)
import random
while True:
    x=random.randrange(1,999)
    print ('The number is ' + str(x) + ' ')
    for n in range(1,13):
        print('Is the number above divisible by '+str(n)+'?')
        inp=input('')
        print(inp)
        if x%n==0:
            if inp=='y':
                print ('Correct!')
            elif inp=='n':
                print ('Incorect')
                divis(n)
            else:
                print('Invalid input. Continuing.')
        elif x%n>0:
            if inp=='y':
                print ('Incorrect.')
                divis(n)
            elif inp=='n':
                print('Correct!')
            else:
                print('Invalid input. Continuing.')
    doneinput=input('If done, press "CTRL+D". Otherwise, press enter.')
