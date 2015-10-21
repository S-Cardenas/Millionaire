from Levels import *
import time

#Print the instructions for the users
def print_instructions():
	print "RULES"
	print "-----------------------------------------------------------------------------"
	print "1) There are 10 multiple choice questions. You must select the right answer."
	print "2) If you select the wrong answer the game is over."
	print "3) You have three life lines. They are as follows:"
	print "			50:50 ........ Eliminate 2 wrong answers."
	print "			Phone a friend...............uhhhh well.... call someone."
	print "			Ask the audience............... no audience. Sry. (Call another"
	print "			friend maybe)."
	print "4) Answer all the questions correctly and win $1,000,000.00"
	print "Good Luck :)"
	print "-----------------------------------------------------------------------------"
	
#Defines the available lifelines	
def all_lifelines():
	list = ['50:50', 'Phone a friend', 'Ask the audience']
	return list
	
#Returns the question to be asked along with possible answers
def ask_question(turn):
	key = {1: level_1, 2: level_2, 3: level_3, 4: level_4, 5: level_5, 6: level_6, 7: level_7, 8: level_8,
			9: level_9, 10: level_10}
	
	Q, choices, ans =  key[turn]()
	
	#Prints the question
	print Q
	
	#Shows the multiple choices
	for key, value in choices.iteritems():
		print key, ':', value
	print "\n"	
	#return the correct answer
	return Q, choices, ans

#Returns the result of the lifeline that was used	
def use_lifeline(Response, choices, ans):
	#Remove 2 wrong answers
	if Response == "50:50":
		ans_key = 0
		i = 0
		for key, value in choices.iteritems():
			if choices[key] == ans: 
				ans_key = key
				break
			else:
				i += 1
					
		indices = range(0,4)
		indices.remove(i)
		remove = random.sample(indices, 2)
		letter_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
		
		for num in remove:
			choices[letter_key[num]] = ' '
		
		#Shows the multiple choices
		for key, value in choices.iteritems():
			print key, ':', value
		
		return choices
		
	elif Response == 'Phone a friend':
		print "Go head. Call a friend."
		print "You have 30 seconds."
		print "Starting now."
		print "Don't cheat ;)"
		
		#Begin 30 seconds in which you may call your friend
		seconds = 30

		startTime = time.time()
		finishTime = startTime + seconds

		# Begin loop until current system time is greater than
		#finish time
		while time.time() < finishTime:

		  # show loop is running
		  print "."

		  # wait for one second
		  time.sleep(1)

		print "Time is up!"
		print "Hang up and select an answer :)"
		
		return choices
		
	else:
		print "Ask the audience or use google to look up your answer."
		print "You have 30 seconds."
		print "Starting now."
		
		#Begin 30 seconds in which you may call your friend
		seconds = 30

		startTime = time.time()
		finishTime = startTime + seconds

		# Begin loop until current system time is greater than
		# finish time
		while time.time() < finishTime:

		  # show loop is running
		  print "."

		  # wait for one second
		  time.sleep(1)

		print "Time is up!"
		print "Hang up and select an answer :)"
		
		return choices
	
def exit_game():
	quit()	