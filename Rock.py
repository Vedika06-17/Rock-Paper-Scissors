import random
print("What do you choose??")
x=int(input("0 for rock,1 for paper or 2 for Scissors"))
L=["Rock","Paper","Scissor"]
y=random.randint(0,2)
print(f"Computer choose:{int(y)}")
if x==y:
    print("Its a draw")
elif x>y and x<=2:
    print("You won!!")
elif x==0 and y==2:
    print("You won!!")
elif y==0 and x==2:
    print("You lose!")
elif x<y:
    print("You lose!!")
elif x<0:
    print("You typed invalid numberr.")
else:
    print("You typed wrong number.You lose!!")