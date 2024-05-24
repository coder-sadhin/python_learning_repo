#Convert the 0 into a number so we can add scores
score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to Quiz night! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name))

#Question1
print("""What is the term for ‘Maori’ language?
1. Te Rex 
2. Hangi 
3. Hongu 
4. Te Reo""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("""What is the Maori term for ‘tribe’ or ‘mob’?
1. Mihi 
2. Iwi 
3. Awi 
4. Hapu""")

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question3
print("""What is the term for the formal welcome, where two individuals press their nose together?
1. Hongi 
2. Haka 
3. Hangi 
4. Huka""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question4
print("""Who is the ‘demi-god’ or the ‘great creator’ who fished NZ out from the sea?
1. Zeus
2. Hercules
3. Maui
4. Maori""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question5
print("""What is the name for the traditional Maori method of cooking?
1. Roast
2. Hangi
3. Hongi
4. Bake""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing {}, goodbye!".format(name))