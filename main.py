import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    if guesses>6:
        print("You have reached the maximum number of guesses.")
        break
    a=int(input("guess the number : "))
    if(a<n):
        print("please enter higher number  ")
    elif(a>n):
        print("please enter lower number  ")
    else:
        print("congratulations! you have guessed the number correctly")
    if guesses==3 and a!=n:
        if(n%2==0):
            print("Hint: the number is even")
        else:
            print("Hint: the number is odd")
if(guesses==1):
        print(" Amazing!,your score is 100")
elif guesses==2:
        print("excellent!,your score is 80")
elif guesses==3:
        print(" good job,your score is 60")
elif guesses==4:
        print(" good,your score is 40")
elif guesses==5:
        print("your score is 20")
elif guesses==6:
        print("your score is 5")
else:
        print("oops!,try again")
        print("your score is 0, please try again")
if(a==n):
    print(f"you have guessed the {n} number in {guesses} guesses")
else:
    print(f"the number was {n}, better luck next time!")
    
