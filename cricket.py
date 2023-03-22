import random
import time
print("Welcome to Cricket with PC")
player1 = input("Enter the name of Player : \n")
print("OnGoing match", player1,"V/S PC\n" )
time.sleep(1)
print("Game start in \n")
print("3...\n")
time.sleep(1)
print("2...\n")
time.sleep(1)
print("1...\n")
time.sleep(1)
Toss = ['H','T']
while True:
    toss_choose = input("Choose Heads(H) or Tails(T) : \n")
    if toss_choose == 'H' or toss_choose == 'T':
        break
    else:
        print("Wrong choice\n")    

toss_selected = random.choice(Toss)
print("Coin in the air\n")
time.sleep(2)
print("THE RESULT IS ",toss_selected)
if toss_choose == toss_selected:
    print(player1, " won the toss\n")
    d=1
else:
    print("PC won the toss\n")
    d=0    
time.sleep(2)
Play = ['B','BO']
if d == 1:
    while True:
        player1_choice = input("Choose between Batting(B) or Bowling(BO) : ")
        if player1_choice == 'B' or player1_choice == 'BO':
            break
        else:
            print("Wrong choice")
    
    if player1_choice == 'B':
        print(player1 , " chose to bat first")
        s=1
    else:
        print(player1 , " chose to bowl first")
        s=2    
else:
    PC_choice = random.choice(Play)
    if PC_choice == 'B':
        print("PC chose to bat first")
        s=3
    else:
        print("PC chose to bowl first")
        s=4 
time.sleep(3)
print("Now before you start the game\n")
time.sleep(1)
print("You must know the instructions\n")
time.sleep(1)
print("So here are the instructions: \n" )
time.sleep(1)
print("1. You have to choose a number between 1,2,3,4,5,6\n")
time.sleep(1)
print("2. If the other player makes the same choice then you are out\n")
time.sleep(1)
print("3. Else the score will be added\n")
time.sleep(1)
print("4. The results will be based like a real cricket match is judged\n")
time.sleep(1)
print("5. Now you are ready to play the game so lets go..(*IT INCLUDES UNLIMITED BALLS)\n")
time.sleep(2)
f=0
end1 = 0
end2=0
Target1=0
Target2=0
f1=0
Player1_score=0
PC_score = 0

if d==0 and s==3: #pc won and chose to bat
    print("PC is Batting\n")
    print(player1 , " is bowling\n")
    while end1 != 1:
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end1 = 1
            print("PC chose ",PC_run)
            
            print("The PC out , Now ",player1 , " will bat")
            print("The target is ", PC_score +1,"\n" )
            
        else:
            PC_score = PC_score + PC_run
            Target1  = PC_score + 1 
            print("PC chose ",PC_run)
            print("The total score for PC is ", PC_score)
            
        
             
    print("Now ",player1  ," is Batting")
    print("PC is Bowling\n")        
    while end2!=1:
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end2 = 1
            print("PC chose ",PC_run)
            print("Sorry But you are out")
               
        else:
            Player1_score = Player1_score + Player1_run
            print("PC chose ",PC_run)
            print("The total score for" ,player1,"is", Player1_score)
            
        if Player1_score>Target1:
            break         
        

if d==1  and s==2: #player won and chose to bowl
    print("PC is Batting")
    print(player1 , " is bowling")
    while end1 != 1 :
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end1 = 1
            print("PC chose ",PC_run)
        
            print("PC is out , Now ",player1 , " will bat")
            print("The target is ", PC_score+1,"\n" )
           
        else:
            PC_score = PC_score + PC_run
            Target1  = PC_score + 1
            print("PC chose ",PC_run)
            print("The total score for PC is ", PC_score)
            
    print("Now ",player1  ," is Batting")
    print("PC is Bowling\n")        
    while end2!=1 :
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end2 =1
            print("PC chose ",PC_run)
            print("Sorry But you are out")
        else:
            Player1_score = Player1_score + Player1_run
            print("PC chose ",PC_run)
            print("The total score for", player1," is ", Player1_score)
        if Player1_score>Target1:
            break               


if d==0 and s==4: #pc won and chose to bowl
    print("PC is Bowling")
    print(player1  ," is Batting")
    while end1 != 1 :
    
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end1 = 1
            print("PC chose ",PC_run)
            print("Sorry But you are out , Now PC will bat")
            print("The target is ", Player1_score+1,"\n" )
        else:
            Player1_score = Player1_score + Player1_run
            Target2  = Player1_score + 1
            print("PC chose ",PC_run)
            print("The total score for", player1  ,"is ", Player1_score)
             
    print("Now PC is Batting")
    print(player1 , " is bowling\n")
    while end2 != 1 :
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end2 = 1
            print("PC chose ",PC_run)
            print("PC is  out")
            
        else:
            PC_score = PC_score + PC_run
            Target1  = PC_score
            print("PC chose ",PC_run)
            print("The total score for PC is ", PC_score)
        if PC_score>Target2:
            break      



if d==1  and s==1: # player won and chose to bat
    print(player1  ," is Batting")
    print("PC is Bowling")
    while end1 != 1 :
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end1 = 1
            print("PC chose ",PC_run)
            print("Sorry But you are out , Now ",player1 , " will bat")
            print("The target is ", Player1_score+1,"\n" )
        else:
            Player1_score = Player1_score + Player1_run
            Target2  = Player1_score + 1 
            print("PC chose ",PC_run)
            print("The total score for", player1  ,"is ", Player1_score)
             
    print("Now PC is Batting")
    print(player1 , " is bowling\n")
    while end2 != 1 :
        
        Player1_run = int(input("Choose a number between 1 to 6: "))
        PC_run = random.randint(1,6)
        if Player1_run == PC_run:
            end2 = 1
            print("PC chose ",PC_run)
            print("PC is out")
            
        else:
            PC_score = PC_score + PC_run
            Target1  = PC_score
            print("PC chose ",PC_run)
            print("The total score for PC is ", PC_score)
        if PC_score>Target2:
            break

print("\nThe match is OVER")
time.sleep(2)       
if Target1 == Target2:
    print("\nIT IS a TIE")
if Target1 > Target2:
    print("\nPC WON")
if Target1 < Target2:
    print(player1 ," WON")
