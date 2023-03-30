# guessing game project



secret_word = "horse"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


#ako guess !=(nije) secret_word and(i) not(nije) out_of guesses
while guess != secret_word and not(out_of_guesses):
    #ako guess_count manji od guess_limit
    if guess_count < guess_limit:
     #guess = unos
     guess = input ("Enter guess: ")
     #guess count +=(plus variable(guess)) + 1 
     guess_count += 1

    else:
       out_of_guesses = True 

if out_of_guesses:
   print("too bad , try again")
   
else:
   print("great, you win")