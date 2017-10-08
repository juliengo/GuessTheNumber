import random
def guess_the_number_game ():
        

    secret_number= random.randint(1, 20)
    print ("Choose a number between 1-20")
    guess =0
    number= -10
    while secret_number!= number:
        
        number= int(input())
        if (number< secret_number):
            print ("oops, it's a bit higher")
        elif (number> secret_number):
            print ("yikes, that's a little high")
        else:
            return ("that's correct!! Congrats! you won!")
        guess+=1
        print ("Try again")
guess_the_number_game()
    
