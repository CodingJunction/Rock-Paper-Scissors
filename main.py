import random
print("""Welcome to the Rock, Paper and Scissors game
Enter 0 for Rock
Enter 1 for Paper
Enter 2 for Scissors
The first one to score 5 points wins""")
user_point=0
computer_point=0


while user_point<5 and computer_point<5:
    a=int(input('Enter your choice\n'))
    c=random.randint(0,2)
    if a == 0:
        print("""Your choice is Rock
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
        """)
    elif a==1:
        print("""Your choice is Paper
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
        """)
    elif a==2:
        print("""Your choice is Scissors
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/           
        """)
    else:
        print('Wrong Choice, Enter again')
        continue

    if c == 0:
        print("""Computer choice is Rock
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
        """)
    elif c==1:
        print("""Computer choice is Paper
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
        """)
    elif c==2:
        print("""Computer choice is Scissors
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/           
        """)
    
    






    if a==0:
        if c==1:
            print('Computer Wins 🎉')
            computer_point+=1
        elif c==2:
            print('User Wins 🎉')
            user_point+=1
        else:
            print('Draw, play again')
    elif a==1:
        if c==0:
            print('User Wins 🎉')
            user_point+=1
        elif c==1:
            print('Draw, play again')
        else:
            print('Computer Wins 🎉')
            computer_point+=1
    else:
        if c==0:
            print('Computer Wins 🎉')
            computer_point+=1
        elif c==1:
            print('User Wins 🎉')
            user_point+=1
        else:
            print('Draw, play again')
print()
print('Final Score Board')
print('User: ',user_point)
print('Computer: ',computer_point)
print()
if user_point==5:
    print('''🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
The final victory belongs to the : USER
🎉🎉🎉🎉🎉🎉Congratulations🎉🎉🎉🎉🎉🎉
    ''')
if computer_point==5:
    print('''🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
The final victory belongs to the : COMPUTER
🎉🎉🎉🎉🎉🎉Congratulations🎉🎉🎉🎉🎉🎉
    ''')




