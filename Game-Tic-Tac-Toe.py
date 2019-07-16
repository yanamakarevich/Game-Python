import random
import sys
print(
"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:/dMMMMMMMddMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMhmMMMMMMMMMMMMMMMMN+    -yNMMMMmyMMMMNhs+:-.````..-/+sdNMMMMMMMMMMMmhM
MMMMMMMMm-  /hMMMMMMMMMMMMMh.       `+dMMNsMdo-                   -odMMMMMMMMhdM
MMMMMMNo      .omMMMMMMMMm/            hMM+-                         -yMMMMMMymM
MMMMMh.          :yNMMMMs`           -dMMM:                            -mMMMMyNM
MMMN/              `+dh.            oMMMMM+                             `dMMMsMM
MMMMh/`                           -dMMMMMMy            .                 `mMNyMM
MMMMMMNs-                        oMMMMMMMMd        `+hNMMMNh/             /MdhMM
MMMMMMMMMmo.                   -dMMMMMMMMMN       .mMMMMMMMMMy            `MhdMM
MMMMMMMMMMMMh/`                `oNMMMMMMMMM.      hMMMMMMMMMMM.            NyNMM
MMMMMMMMMMMMMMs                   /dMMMMMMM:      dMMMMMMMMMMN`           `NsNMM
MMMMMMMMMMMMm:                      -yMMMMMo      .mMMMMMMMMN:            :MsMMM
MMMMMMMMMMNo                          .sNMMy        /ymNNmy/`             hmyMMM
MMMMMMMMMy.           `.                `oNm                             +MddMMM
MMMMMMMd:            +NMh/`              sN                             oMMhmMMM
MMMMMN+            -dMMMMMMh/`          /NMM-                         .hMMMyNMMM
MMMMMd:          `yMMMMMMMMMMNy/      -dMMMM/                       `oNMMMMsNMMM
MMMMMMMd:       +NMMMMMMMMMMMMMMNy: `yMMMMMMo                     :yMMMMMMNsMMMM
MMMMMMMMMh:   -dMMMMMMMMMMMMMMMMMMMmNMMMMhysd++:.            .:ohNMMMMMMMMmhMMMM
MMMMMMMMMMMh:sMMMMMMMMMMMMMMMMMMNNmmddhhhsssyhMMMMmdhhhhhhdmNMMMMMMMMMMmmmhdMMMM
MMMMMMMMMNNNmmmddddddddddddddddddmmmNNNNNmmmmddddddddddddddddddmmmNNNMNyhdymMMMM
MMMMNdddddmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmddddhdhNMMMM
""")
array=[["-","-","-"],["-","-","-"],["-","-","-"]]
eaqle=[0,1]
numForComp=[1,2,3,4,5,6,7,8,9]

def picture():
    print(array[0][0],"|",array[0][1],"|",array[0][2])
    print(array[1][0],"|",array[1][1],"|",array[1][2])
    print(array[2][0],"|",array[2][1],"|",array[2][2])
    print()
    print("__________\n")
    
def option():
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print()

def computer():
    print("Мой ход.\n")
    print("1 - Давай")
    ok=int(input())
    if ok==1:
        numC=random.choice(numForComp)
        if numC==1:
            array[0][0]="O"    
        if numC==2:
            array[0][1]="O"   
        if numC==3:
            array[0][2]="O"    
        if numC==4:
            array[1][0]="O"    
        if numC==5:
            array[1][1]="O"   
        if numC==6:
            array[1][2]="O"    
        if numC==7:
            array[2][0]="O"   
        if numC==8:
            array[2][1]="O"    
        if numC==9:
            array[2][2]="O" 
    numForComp.remove(numC)
    picture()   
    
def people():
    print("Твой ход.\n")
    option()
    numP=int(input())
    if numP==1:
        array[0][0]="X"    
    if numP==2:
        array[0][1]="X"     
    if numP==3:
        array[0][2]="X"    
    if numP==4:
        array[1][0]="X"    
    if numP==5:
        array[1][1]="X"   
    if numP==6:
        array[1][2]="X"   
    if numP==7:
        array[2][0]="X"    
    if numP==8:
        array[2][1]="X"    
    if numP==9:
        array[2][2]="X"
    numForComp.remove(numP)
    picture()
    


print("Кто начнет? Подкинем монетку.")

print("0 - Орёл, 1 - Решка")
eaqleTails=int(input())
a=random.choice(eaqle)
if eaqleTails==a:
    for i in range(10):
        if i%2!=0:
            people()
            if ["X","X","X"] in array or ["O","O","O"] in array or array[0][0]=="O" and array[1][0]=="O" and array[2][0]=="O" or array[0][1]=="O" and array[1][1]=="O" and array[2][1]=="O" or array[0][2]=="O" and array[1][2]=="O" and array[2][2]=="O" or  array[0][0]=="X" and array[1][0]=="X" and array[2][0]=="X" or array[0][1]=="X" and array[1][1]=="X" and array[2][1]=="X" or array[0][2]=="X" and array[1][2]=="X" and array[2][2]=="X" or array[0][0]=="X" and array[1][1]=="X" and array[2][2]=="X" or array[0][0]=="O" and array[1][1]=="O" and array[2][2]=="O" or array[0][2]=="X" and array[1][1]=="X" and array[2][0]=="X" or array[0][2]=="O" and array[1][1]=="O" and array[2][0]=="O":
                print("Поздравляю! Победа за вами!")
                break
        elif i%2==0:
            computer()
            if ["X","X","X"] in array or ["O","O","O"] in array or array[0][0]=="O" and array[1][0]=="O" and array[2][0]=="O" or array[0][1]=="O" and array[1][1]=="O" and array[2][1]=="O" or array[0][2]=="O" and array[1][2]=="O" and array[2][2]=="O" or  array[0][0]=="X" and array[1][0]=="X" and array[2][0]=="X" or array[0][1]=="X" and array[1][1]=="X" and array[2][1]=="X" or array[0][2]=="X" and array[1][2]=="X" and array[2][2]=="X" or array[0][0]=="X" and array[1][1]=="X" and array[2][2]=="X" or array[0][0]=="O" and array[1][1]=="O" and array[2][2]=="O" or array[0][2]=="X" and array[1][1]=="X" and array[2][0]=="X" or array[0][2]=="O" and array[1][1]=="O" and array[2][0]=="O":
                print("Увы и ах. Компьютер вас сделал.")
                break
        elif numForComp==0:
            print("Ничья!")
            break
else:
    for i in range(10):
        if i%2==0:
            people()
            if ["X","X","X"] in array or ["O","O","O"] in array or array[0][0]=="O" and array[1][0]=="O" and array[2][0]=="O" or array[0][1]=="O" and array[1][1]=="O" and array[2][1]=="O" or array[0][2]=="O" and array[1][2]=="O" and array[2][2]=="O" or  array[0][0]=="X" and array[1][0]=="X" and array[2][0]=="X" or array[0][1]=="X" and array[1][1]=="X" and array[2][1]=="X" or array[0][2]=="X" and array[1][2]=="X" and array[2][2]=="X" or array[0][0]=="X" and array[1][1]=="X" and array[2][2]=="X" or array[0][0]=="O" and array[1][1]=="O" and array[2][2]=="O" or array[0][2]=="X" and array[1][1]=="X" and array[2][0]=="X" or array[0][2]=="O" and array[1][1]=="O" and array[2][0]=="O":
                print("Поздравляю! Победа за вами!")
                break
        elif i%2!=0:
            computer()
            if ["X","X","X"] in array or ["O","O","O"] in array or array[0][0]=="O" and array[1][0]=="O" and array[2][0]=="O" or array[0][1]=="O" and array[1][1]=="O" and array[2][1]=="O" or array[0][2]=="O" and array[1][2]=="O" and array[2][2]=="O" or  array[0][0]=="X" and array[1][0]=="X" and array[2][0]=="X" or array[0][1]=="X" and array[1][1]=="X" and array[2][1]=="X" or array[0][2]=="X" and array[1][2]=="X" and array[2][2]=="X" or array[0][0]=="X" and array[1][1]=="X" and array[2][2]=="X" or array[0][0]=="O" and array[1][1]=="O" and array[2][2]=="O" or array[0][2]=="X" and array[1][1]=="X" and array[2][0]=="X" or array[0][2]=="O" and array[1][1]=="O" and array[2][0]=="O":
                print("Увы и ах. Компьютер вас сделал.")
                break
        elif numForComp==0:
            print("Ничья!")
            break

    
