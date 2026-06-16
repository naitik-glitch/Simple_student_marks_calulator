
def marks_input():
	english = input("Enter your English marks : ")
	hindi = input("Enter your Hindi marks : ")
	math = input("Enter your Math marks : ")
	science = input("Enter your Science marks : ")
	social_science = input("Enter your Social Science marks : ")
	get_raw_marks = [english,hindi,math,science,social_science]
	return get_raw_marks
						
	 
def validate_input(get_raw_marks):
	english,hindi,math,science,social_science = get_raw_marks
	try:
		english = float(english) 
		hindi= float(hindi)
		math =float(math) 
		science=float(science)
		social_science=float(social_science)
		l_marks = [english,hindi,math,science,social_science]
		return l_marks
	except:
		print("Invalid : Input")
		return "Invalid : Input"
						


def check_marks(l_marks):
							 if l_marks !="Invalid : Input":
							 								for items in l_marks:
							 									if items>100 or items <0:
							 										return "Type marks from 0 to 100"
							 								else:
							 									return l_marks							 			
							 else:
							 	return ("Invalid : Input")
			

						
def calculate_marks(l_marks):
	
	total_marks = sum(l_marks)
	total_sub = len(l_marks)
	avg_marks = total_marks/total_sub
	max_marks = 100* total_sub
	percentage = (total_marks/max_marks)*100
	calc_marks =[total_marks,avg_marks,percentage]
	return calc_marks
	
def print_marks(l_marks,calc_marks):
	english,hindi,math,science,social_science = l_marks
	total_marks,avg_marks,percentage =calc_marks
							
	print(f"English : {english}\nHindi : {hindi}\nMath :{math}\nScience : {science}\nSocial Science : {social_science}")	
	print(f"Total Marks : {total_marks}\nAverage Marks : {avg_marks}\nPercentage : {percentage}%")
	
def get_valid_marks():
	get_raw_marks = marks_input()
	l_marks=validate_input(get_raw_marks)
	return l_marks							 

def calc_print(l_marks):
	calc_marks = calculate_marks(l_marks)
	print_marks(l_marks,calc_marks)	


l_marks=get_valid_marks()
report = check_marks(l_marks)


if report == "Type marks from 0 to 100": 
			print("Invaild Input : Type marks from 0 to 100")
		
elif report == "Invalid : Input" :
			while report == "Invalid : Input":
				l_marks=get_valid_marks()
				report =check_marks(l_marks)
				try:
					calc_print(l_marks)
				except:
					report =="Type marks from 0 to 100"
				
					
else:
		calc_print(l_marks)		 
		
user_choice = input("Type 'Exit' to exit the game and 'Go' to continue : ").lower()

while user_choice == "go":
	l_marks = get_valid_marks()
	report = check_marks(l_marks)
	if report == "Type marks from 0 to 100": 
			print("Invaild Input : Type marks from 0 to 100")
	elif report == "Invalid : Input":
				while report == "Invalid : Input":
					l_marks=get_valid_marks()
					report =check_marks(l_marks)
					try:
						calc_print(l_marks)
					except:
						report =="Type marks from 0 to 100"
	else:
		calc_print(l_marks)	
	user_choice = input("Type 'Exit' to exit the game and 'Go' to continue : ").lower()

	
