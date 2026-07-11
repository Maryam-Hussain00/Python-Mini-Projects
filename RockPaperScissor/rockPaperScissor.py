# Rock Paper Scissor game
turn1=input("Player No.1 Its your turn, Shoot! ").lower()
turn2=input("Player No.2 Its your turn, Shoot! ").lower()

r = "rock"
p = "paper"
s = "scissor"

if turn1 not in [r,p,s] or turn2 not in [r,p,s]:
    print("Invalid Input!")

elif turn1 == r and turn2 == p:
    print("Player No. 2 wins")

elif turn1 == p and turn2 == s:
    print("Player No. 2 wins")

elif turn1 == s and turn2 == r:
    print("Player No. 2 wins")

elif turn1 == s and turn2 == p:
    print("Player No. 1 wins")

elif turn1 == p and turn2 == r:
    print("Player No. 1 wins")

elif turn1 == r and turn2 == s:
    print("Player No. 1 wins")

else:
    print("Draw")