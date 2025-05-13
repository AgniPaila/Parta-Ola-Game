#Agni Paila

from random import randint
from random import choice
x=int(input('please input number of players:'))
if x < 2:
    print("The game starts with at least 2 players")
    exit()
y=int(input('please input number of beans per player:'))
if y < 1:
    print("Each player should have at least 1 bean at the beginning")
    exit()
lst=['put one' , 'put two' , 'everyone puts one' , 'take one' , 'take two' , 'take them all']
pot=x                            
playersCounter=x 
round=1                               
players=x
g=0
beansList=list(range(0,x))         #lista me ta fasolia pou exei o kathe paikths
for j in range(0,x,1):
    beansList[j]=y-1               #o kathe paikths sthn arxh tou paixnidiou exei 1 fasoli ligotero epeidh ebale ena sto kentro
rp=randint(1,x)
print('round ', round,' begins: ',lst[2])
print('current state:')
print('pot:', pot)
for i in range(0,x,1):
    print('player' , i+1 ,'\'s budget:' ,beansList[i])
while playersCounter>1:                            #oi paiktes parapanw apo enan
    spin=choice(lst)        
    round+=1
    while pot>0 and g!=-17:
        if beansList[rp-1] < 0:
            rp += 1
            if rp > x:
                rp = 1
            continue
        if spin==lst[0]:
            if beansList[rp-1]==0:          #rp-1 epidh to metrhma stis theseis ksekiaei apo 0 enw oi paiktes ksekinan apo to 1
                beansList[rp-1]=-1
                playersCounter -= 1
            else:
                pot+=1
                beansList[rp-1]-=1
        elif spin==lst[1]:   
            if beansList[rp-1]==0:
                beansList[rp-1]=-1
                playersCounter-=1
            elif beansList[rp-1]==1:
                pot=pot+1
                beansList[rp-1]=-1
                playersCounter-=1
            else:
                pot=pot+2
                beansList[rp-1]-=2
        elif spin==lst[2]:
            for l in range(0,players,1):     
                if beansList[l]>=0:
                    if beansList[l]==0:
                        beansList[l]=-1
                        playersCounter-=1
                    else:
                        beansList[l]-=1
                        pot+=1
        elif spin==lst[3]:
            if pot!=0:
                beansList[rp-1]+=1
                pot-=1
            if pot ==0:
                break
        elif spin==lst[4]:
            takeAmount=min(2,pot)
            beansList[rp-1]+=takeAmount
            pot-=takeAmount
            if pot==0:
                break         
        elif spin==lst[5]:
            beansList[rp-1]+=pot
            pot=0   
        print('\nplayer' , rp , 'spinned:' ,spin)
        print('current state:')
        print('pot:', pot)
        for k in range(0,players,1):   
            if beansList[k]<0:
                print('player ',k+1, 'is eliminated')    
            else:
                print('player' , k+1 ,'\'s budget:' ,beansList[k])
            
        spin=choice(lst)
        rp+=1
        if rp>x:
            rp=1
        if playersCounter==1:       
            for z in range(0,players,1):
                if beansList[z]>0:
                    winner=z+1
                    print('Game finished! Player',winner,'wins')
                g=-17
            break
    if g==-17:
        break
    print('-----------------------------------------')
    for j in range(0,players,1):
        if beansList[j]>=0:          
            if beansList[j]==0:
                beansList[j]=-1
                playersCounter-=1
            else:
                beansList[j]-=1
                pot+=1
    if playersCounter==1:        
        for z in range(0,players,1):
            if beansList[z]>0:
                winner=z+1
                print('Game finished! Player',winner,'wins')
                g=-17
        break
    print('round ', round,' begins: ',lst[2])
    print('current state:')
    print('pot:', pot)
    for o in range(0,players,1):
        if beansList[o]<0:
            print('player ',o+1, 'is eliminated')
        else:
            print('player' , o+1 ,'\'s budget:' ,beansList[o])
