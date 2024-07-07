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




#INCOMPLETE 3
email_entered = input("Enter your email here ")
sign = "@"
domain = "gmail.com"

email_adress = email_entered + sign + domain
no_sign = sign
no_domain = domain
if sign not in email_entered:
    print(email_entered + sign + domain)
else:
    print(f"{email_entered}{domain}")
if domain not in email_entered:
    email_entered.insert("@")
    print(email_entered + no_domain)
else:
    print(email_entered)


email_entered.replace()
