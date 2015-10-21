from Millionaire import *


def main():
	
	# setup game
	# alternate turns
	# check if win or end
	# quit
	
	print_instructions()
	available_lifelines = all_lifelines()
	possible_answers = ['A', 'B', 'C', 'D']
	turn = 1
	
	
	while turn != 11:
		 
		#Ask the user a question and define the answer
		print "Questions #: ", turn
		print "------------------"
		Q, choices, ans = ask_question(turn)
		 
		while len(available_lifelines) != 0:
			
			print "The available lifelines are:"
			
			for lifeline in available_lifelines:
				print lifeline
			print "\n"
			
			try: 
				Response = str(raw_input("Please select an answer or use a lifeline: \n"))
				if Response in possible_answers:
					if choices[Response] == ans:
						print "Correct!!"
						turn += 1
						break
					else:
						print "Wrong answer :("
						print "Thanks for playing with us."
						exit_game()
				elif Response in available_lifelines:
					choices = use_lifeline(Response, choices, ans)
					available_lifelines.remove(Response)
					
			except Exception as e:	
				print "This is not a valid choice. Please enter A, B, C, or D."
			
		
		if len(available_lifelines) == 0:
			print "There are no more available lifelines."
			
			while True:
				try:
					Response = str(raw_input("Please select an answer or use a lifeline: "))
					if choices[Response] == ans:
						print "Correct!!"
						turn += 1
						break
					else:
						print "Wrong answer :("
						print "Thanks for playing with us."
						exit_game()
						
				except Exception as e:
					print "This is not a valid choice. Please enter A, B, C, or D."
			
	print "Congratualtions, you won $1,000,000.00!!"
	exit_game()


if __name__ == "__main__":
	main()		