import random

def compare(comp_guess, user_guess):
    cowbull = [0,0]
    
    for i in range(len(comp_guess)):
        if comp_guess[i] == user_guess[i]:
            cowbull[0] +=1
        else:
            if comp_guess[i] in user_guess:
                cowbull[1] += 1
    return cowbull

if __name__=='__main__':
    playing = True
    
    print('if your guess is exit the game will end\n')

    while playing:
        user_guess = input('Enter 4-digit guess: ')
        if user_guess == 'exit':
            print('cowbull shut down..')
            break
        num = str(random.randint(1000,9999))
        result = compare(num, user_guess)
        print(num)
        print(str(result[0]) + "cows," + str(result[1]) +" bulls")

        if result[1] == 4:
            playing = False
            print('You win!!!')
            print(str(result[0]) + "cows," + str(result[1]) +" bulls")
        else:
            print('Try Again')
