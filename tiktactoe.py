def sum(a,b,c):
    return a+b+c

def printboard(xstate,ostate):
    zero='x' if xstate[0] else ('o' if ostate[0] else 0)
    one='x' if xstate[1] else ('o' if ostate[1] else 1)
    two='x' if xstate[2] else ('o' if ostate[2] else 2)
    three='x' if xstate[3] else ('o' if ostate[3] else 3)
    four='x' if xstate[4] else ('o' if ostate[4] else 4)
    five='x' if xstate[5] else ('o' if ostate[5] else 5)
    six='x' if xstate[6] else ('o' if ostate[6] else 6)
    seven='x' if xstate[7] else ('o' if ostate[7] else 7)
    eight='x' if xstate[8] else ('o' if ostate[8] else 8)
    print(f"{zero}|{one}|{two}")
    print(f"-|-|-")
    print(f"{three}|{four}|{five}")
    print(f"-|-|-")
    print(f"{six}|{seven}|{eight}")

def fnwinner(xstate,ostate):
    MatchWinner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in MatchWinner:
        if(sum(xstate[i[0]],xstate[i[1]],xstate[i[2]])==3):
            print("Winner is x")
            return 1
            
        elif(sum(ostate[i[0]],ostate[i[1]],ostate[i[2]])==3):
            print("Winner is o")
            return 0
            
    return -1
    
if(__name__=="__main__"):
    xstate=[0,0,0,0,0,0,0,0,0]
    ostate=[0,0,0,0,0,0,0,0,0]
    print("Welcome Players")
    turn=1
    while(True):
        printboard(xstate,ostate)
        if(turn==1):
            print("x's chance")
            place=int(input("Enter the position to place x:"))
            xstate[place]=1
        else:
            print("o's chance")
            place=int(input("Enter the position to place o:"))
            ostate[place]=1
        winner=fnwinner(xstate,ostate)
        if(winner!=-1):
            print("Match over")
            break
        
        turn=1-turn

        
