'''
Kuberan JS Miniworld internship Task : Level 1 
Personal Random Quote generator 
'''
import random

Moti = [" When you have a dream, you've got to grab it and never let go " , " Nothing is impossible " , " There is nothing impossible to they who will try " , " The bad news is time flies " , " Life has got all those twists and turns "]
succ = [" Success is not final, failure is not fatal: It is the courage to continue that counts " , " Success is not in what you have, but who you are " , " Success is not the key to happiness. Happiness is the key to success " , " Success is walking from failure to failure with no loss of enthusiasm" , " Success is not about the destination, it's about the journey "]
Love = [" Love all, trust a few, do wrong to none " , "You call it madness, but I call it love " , " We can only learn to love by loving " , " A life lived in love will never be dull " , " Life is the flower for which love is the honey " ]
Life = [" For every minute you are angry, you lose 60 seconds of happiness " , " Go the extra mile, there's no one on it " , " Humility is not thinking less of yourself, it's thinking of yourself less " , " Human nature is like water " , " Life is in ourselves and not in the external " ]

quotes = [Moti,succ,Love,Life]

name = input("Enter your name : ") #getting name from user

while(True):
    print("\n1.Motivation\n2.Success\n3.Love\n4.Life\n0-Exit\n")
    choice = int(input(("Select a category : "))) # getting choice from user 
    
    if (choice == 0 ):
        print("Thank you "+name)
        break #breaking the loop if exit is chosen
    
    else :
        print("Here's a Quote for you "+name)
        print(quotes[choice-1][random.randint(0,4)]) # printing a random quote from selected category
        print()

#Source for quotes : www.parade.com