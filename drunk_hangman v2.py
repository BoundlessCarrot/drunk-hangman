#guess counter and endgame checker don't work. Desperately needs to be refactored/simplfied

import re
import os
	
class Hangman:
#	gamespace = []
#	incorrectGuesses = ""
#	gamestring = ""
#	bool ruleset
	
	def __init__(self, word, ruleset):
		self.gamespace = ['_' for letter in word]
		self.word = word
		self.ruleset = ruleset
		self.incorrectGuesses = ""
		self.gamestring = ""						

	def midGameCases(self, guessedletter, n):
		#midgame cases
		if guessedletter in self.word:
			indices = [m.start() for m in re.finditer(guessedletter, self.word)]
			
			for x in indices:
				try:
					self.gamespace[x] = guessedletter.upper()
				except IndexError:
					continue
			
			print("Good guess! Whoever put up the word, take {} sip(s)!\n".format(len(indices)))
			return True
		
		elif guessedletter not in self.word:
			print("Sorry, that's incorrect! Take a sip.\n")
			self.incorrectGuesses += guessedletter.upper()
			n += 1
			return False
		
		else:
			print("This is an unexpected behavior or an edge case. If you see this tell me in person or put an issue up on github")
	
	def endGameCases(self, guessedletter, n):
		#endgame cases
		if guessedletter == self.word or self.gamestring == self.word:
			if ruleset == True:
				spacesleft = [a for a in self.gamespace if a == '_']
				print("Congrats! You guessed the word with {} spaces left over. Whoever put the word up has to take {} sip(s)!".format(len(spacesleft), len(spacesleft)))
				return True
			else:
				guessesleft = 10 - n
				print("Congrats! You guessed the word with {} guesses left over. Whoever put the word up has to take {} sip(s)!".format(guessesleft, guessesleft))
				return True
		elif n == 10:
			print("Womp womp, you're out of guesses! The word was {}. Everyone guessing, DRINK!".format(word.upper()))
			return False

	def gameLogic(self):
			n = 0
			
			#game logic loop
			while n <= 10:
				for z in self.gamespace: 
#					print(z, end=' ')
					self.gamestring += str(z)
				print()
				print((', ').join(self.incorrectGuesses) + '     ({}/10) [incorrect] guesses used\n'.format(n))
				guessedletter = input("Guess a letter: ").casefold()
				
				#weird edge cases that should be checked first
				
				#this one specifically doesn't work, idk why
				if guessedletter in self.incorrectGuesses:
					print("You already guessed that letter!\n")
					guessedletter = input("Guess a letter: ").casefold()
					
				if guessedletter.isalpha() == False:
					print("That's not even a letter! You're either really fucked at the moment or just dumb.")
					continue
				
				val1 = self.endGameCases(guessedletter, n)
				val2 = self.midGameCases(guessedletter, n)
				
				if val1 == False:
					break
				if val2 == False:
					continue


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
	print()
	hang = Hangman(guessedWord, ruleset)
	hang.gameLogic()
	
	playAgain = input("Do you want to play again? (y/n): ").casefold()
	
	while(playAgain == 'y'):
		del hang
		guessedWord = input("Input a word to be guessed: ").casefold()
		os.system('clear')
		print()
		hang = Hangman(guessedWord, ruleset)
		hang.gameLogic()
		playAgain = input("Do you want to play again? (y/n): ").casefold()
	
	#post game	
	print('Hope you had fun (got drunk) playing Drunk Hangman!')
	print("Some credits go to Jordan Streete, but most go to my good friends at the pre-game for the 2019 Jacobs Alumni party.")