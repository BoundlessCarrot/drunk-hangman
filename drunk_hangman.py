import re
import os
	
def hangman(word, ruleset):
	#define the gamespace
	length = len(word)
	gamespace = []
	incorrectGuesses = ""
	gamestring = ""
	n = 0
	
	#initialize the gamespace
	for letter in word:
		gamespace.append('_')
	
	#game logic loop
	while n <= 10:
		for z in gamespace:
			print(z, end=' ')
			gamestring += z
		
		print()
		
		print((', ').join(incorrectGuesses) + '     ({}/10) [incorrect] guesses used'.format(n))
		
		guessedletter = input("Guess a letter: ").casefold()
		
		#weird edge cases that should be checked first
		
		#this one specifically doesn't work, idk why
		if guessedletter in incorrectGuesses:
			print("You already guessed that letter!")
			guessedletter = input("Guess a letter: ").casefold()
			
		if guessedletter.isalpha() == False:
			print("That's not even a letter! You're either really fucked at the moment or just dumb.")
			continue
		
		#midgame cases
		if guessedletter in word:
			indices = [m.start() for m in re.finditer(guessedletter, word)]
			
			for x in indices:
				try:
					gamespace[x] = guessedletter.upper()
				except IndexError:
					continue
			
			print("Good guess!\n")
		
		elif guessedletter not in word:
			print("\nSorry, that's incorrect! Take a sip.")
			incorrectGuesses += guessedletter.upper()
			n += 1
		
		else:
			print("This is an unexpected behavior or an edge case. If you see this tell me in person or put an issue up on github")
			continue
		
		#endgame cases
		if guessedletter == word or gamestring == word:
			if ruleset == True:
				spacesleft = [a for a in gamespace if a == '_']
				print("Congrats! You guessed the word with {} spaces left over. Whoever put the word up has to take {} sips!".format(len(spacesleft), len(spacesleft)))
				return
			else:
				guessesleft = 10 - n
				print("Congrats! You guessed the word with {} guesses left over. Whoever put the word up has to take {} sips!".format(guessesleft, guessesleft))
				return
		elif n == 10:
			print("Womp womp, you're out of guesses! The word was {}. Everyone guessing, DRINK!".format(word.upper()))
			return

if __name__ == '__main__':
	#game setup
	r = input('Do you want to use spaces left over or guesses left over as a drinking metric? (spaces/guesses): ').casefold()
	
	if r == 'spaces'.casefold():
		ruleset = True
	elif r == 'guesses'.casefold():
		ruleset = False
	else:
		r = input('Something went wrong. Do you want to use spaces left over or guesses left over as a drinking metric? (spaces/guesses): ').casefold()
	
	#game initialization
	guessedWord = input("Input a word to be guessed: ").casefold()
	os.system('clear')
	hangman(guessedWord, ruleset)
	
	playAgain = input("Do you want to play again? (y/n): ").casefold()
	
	while(playAgain == 'y'):
		guessedWord = input("Input a word to be guessed: ").casefold()
		os.system('clear')
		hangman(guessedWord, ruleset)
		playAgain = input("Do you want to play again? (y/n): ").casefold()
	
	#post game	
	print('Hope you had fun (got drunk) playing Drunk Hangman!')
	print("Some credits go to Jordan Streete, but most go to my good friends at the pre-game for the 2019 Jacobs Alumni party.")