# Creating my first game
 # It is an adenture game

from turtle import left

print("Hello, Welcome to my first game")
name = input("What's your name? ")
age = int(input("What's your age? "))

health = 10

print("Hello", name , "you are", age , "years old... ")

if age >= 16 :
    print("You are old enough to play")

    want_to_play = input("Do you wanna play? ").lower()
    if want_to_play == 'yes' :
        print("We are starting , you have", health , "health")
        print("Lets play! ")
    
        left_or_right = input("Your choice, you wanna go right or left (right/left) ")
        if left_or_right == 'left' :
            ans = input("Nice you follow the path and you reached to lake , you wanna swim  across it or move around from it (across/around) " )

            if ans == 'around' :
                print("You went around and reached the other side of lake ")
            elif ans == 'across' :
                print("you crossed the lake but bitten by fish and lost 5 health")
                health -= 5

                ans = input("You notice theres a river and a house ... where you'd go (river/house)")
                if ans == 'house' :
                    print("you went into house and house master dosn't like you and you loose 5 health")
                    health -= 5
                    
                    if health <= 0 :
                        print("You know have 0 health and you have lost")
                    else:
                        print("you survived and have won.... ")
                
                else:
                    print("You fell into river and lost...")
         
        else:
            print("you fell from it and lost .... ")
    
    else:
        print("See you later")
else:
    print("You are not enough to play... ")
