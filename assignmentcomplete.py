# Assignment 1
# write a code to determine idf a number is divisible by 5 or not

number_given = int(input("Write a number and check if it is divisible by 5, also if would have a remainder "))

check, check_2, check_3 = number_given/5, number_given//5, number_given % 5
if number_given >= 5:
    print(f"The number you inputed ({number_given}), is divisible by five with an answer of ({check})")
    print(f"Moreover it can only be divided by 5 ({check_2}) times with a remainder of ({check_3})")
else:
    print(f'This number is not divisible by 5 becauce ({number_given}) is less than 5 ')



#Assignment 2
#when a user enters his name ddetermine if it starts with a Capital letter or not

name = input('Enter your name here please')
first_letter = (name[0])
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if first_letter in capital_letters:
    print(f'The first letter of your name does start with a Capital letter, {first_letter} is a capital letter')
else:
    print(f'The first letter of your name does not start with a Capital letter, {first_letter} is not a capital letter but a small one')



#Assignment 4

essay = input("Enter your essay:") 
print(essay)
print(essay.replace(" ", ""))
essay_count = len(essay.replace(" ","")) 
number_of_words = essay_count // 6
print(f"The number of words in your essay is {number_of_words} ")

Assignment 3

#input @ if a user does not input it
email_entered = input("Enter your email here ")
sign, domain = "@", "gmail.com"

email_adress = email_entered + sign 
if sign not in email_entered:
    print(email_entered [:-9] + sign + email_entered[-9:])
else:
    print(email_entered)

# Make a quiz with 10 questions is users ansewr it correctly add 1 to ther score

print('Welcome to quiz 101. Here you will be quizzed with different questions from python programming')
print('To get a score answer the question by selecting the correct awswer in the given option A - D.  Good luck')
total_score = 0
question_1 = ('Question 1: String concatenation is a way of combining two strings together using (A) force (b)gun (C)symbol (D)magnets')
question_2 = ('Question_2:Arithmetic operators are used for performing what? (A)music (B)Arithmetic subtraction (C)Arithmetic combination(D)Arithmetic operations ')
question_3 = ('Question 3: The + sign when combining is used for which of these? (A)float (B)string (C)int (D)none of the above')
question_4 = ('Question _4: In lay mans terms a variable is a storage box that stores what? (A)value (B)dollars (C)pounds (D)love ')
question_5 = ('Question_5: When taking numbers it is important to convert the users input into (A)integers (B)string (C)float (D)none of the above')
question_6 = ('Question 6:Which of these is wrong: (A)index is lower with 1 (B)Index is higher with 1 (C)position is higher than index with 1 (D)all are wrong ')
question_7 = ('Question 7: Which of these is a curly braces: (A){ } (B)[ ] (C)( ) (D)¢')
question_8 = ('Question 8: Converting from one data type to another is called (A) converting. (B)concatenation (C)transpose (D)casting')
question_9 = ('Question 9: The variable to which operations are performed is called (A)operators (B)Operater (C)casting (D)operands ')
question_10 = ('Question 10: What are used to combine conditional statements (A)Logical operators (B)bitwise (C)modulus (D)operands')
print(question_1)
student_answer = input('enter your answer between A - D  ')
answer_1 = ['C', 'c'] 
if student_answer in answer_1:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_2)
student_answer = input('enter your answer between A - D  ')
answer_2 = ['D', 'd'] 
if student_answer in answer_2:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)

print(question_3)
student_answer = input('enter your answer between A - D  ')
answer_3 = ['B', 'b'] 
if student_answer in answer_3:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_4)
student_answer = input('enter your answer between A - D  ')
answer_4 = ['A', 'a'] 
if student_answer in answer_4:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_5)
student_answer = input('enter your answer between A - D  ')
answer_5 = ['A', 'a'] 
if student_answer in answer_5:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_6)
student_answer = input('enter your answer between A - D  ')
answer_6 = ['B', 'b'] 
if student_answer in answer_6:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_7)
student_answer = input('enter your answer between A - D  ')
answer_7 = ['A', 'a'] 
if student_answer in answer_7:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)

print(question_8)
student_answer = input('enter your answer between A - D  ')
answer_8 = ['D', 'd'] 
if student_answer in answer_8:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_9)
student_answer = input('enter your answer between A - D  ')
answer_9 = ['D', 'd'] 
if student_answer in answer_9:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your score is now ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your score is still', total_score)
	
print(question_10)
student_answer = input('enter your answer between A - D  ')
answer_10 = ['A', 'a'] 
if student_answer in answer_10:
	total_score = total_score + 1
	print('You are correct, 1 has been added to your score. Your total score from the queetions given is ', total_score)
else:
	print('You are wrong, you have 0 added marks to your score. Your total score from the questions given is', total_score)
if total_score < 5:
	print(f'Do better next time your score ({total_score}) is too low ')
else:
	print('You have done well by getting a score higher than average')


