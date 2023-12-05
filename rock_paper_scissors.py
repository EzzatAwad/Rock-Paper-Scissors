import random

user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
pc=random.choice (['r','p','s'])

print("User played:"+user)
print("Pc played:"+pc)

if user==pc:
    print("It,s a tie!")
elif (user=='p' and pc=='r') or (user=='r' and pc=='s') or (user=='s' and pc=='p'):
    print("You won!")
else:
    print("You lose!")