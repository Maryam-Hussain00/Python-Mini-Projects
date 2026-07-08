password="Python123"
print("Note: You have 3 attemots!")
print("#Hint: Python & 1st 3 prime numbers.#")
guess=input("Guess the password: ")
attempts=3
for i in range(0,attempts):
    if(guess==password):
        print("Correct password")
        break
    elif(guess!=password and i<2):
        guess=input("Wrong guess try again!")
    if(guess!=password and i==2):
        print("Wrong guess. Your password is locked.")
