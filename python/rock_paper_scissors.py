import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

loose=0
win=0 
while True:
    user_choice=int(input("Enter a number between 1 and 3 (1->Rock, 2->Paper, 3->Scissors): "))

    while user_choice not in (1, 2, 3):
        user_choice=int(input("Wrong Input. Please enter a number between 1 and 3 (1->Rock, 2->Paper, 3->Scissors): "))

    comp_choice=random.randint(1,3)
    while comp_choice == user_choice:
        comp_choice=random.randint(1,3)

    if (user_choice == 1 and comp_choice == 2) or (user_choice == 3 and comp_choice == 1) or (user_choice == 2 and comp_choice == 3):
        print("You loose!")
        loose+=1
    
    else:
        print("You WIN!")
        win+=1

    ans=input("Press any key to continue and X to cancel? ").lower
    print(ans)

    if ans == 'x':
        break

print("Thank you for participating. You have won", win, "times and lost ", loose, "times.")