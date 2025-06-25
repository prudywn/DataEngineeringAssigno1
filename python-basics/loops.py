for i in range(1,11):
    print(i)

#Use a while loop to print numbers until the user enters stop.
while True:
    user_input = input("Enter a number: ")
    if user_input == "stop":
        break
    else:
        print(user_input)


for i in range(1,20):
    if i % 2 == 0:
        print(i)
    else:
        continue

#break - stops loop execution
#continue - skips to the next iteration
""" Challenge
Write a guessing game that asks the user to guess a secret number between 1 and 10.

Give feedback (too high / too low)
Use a while loop """

print('--------START OF THE GAME--------')

num = int(input('Enter the lucky number to win: '))
while num < 11:
    if num < 3:
        print('Too Low')
        break
    elif num > 7:
        print('Too High')
        break
    elif num == 5:
        print('WINNER!!!')
        break
    else:
        print('Better luck next time!')
        break






