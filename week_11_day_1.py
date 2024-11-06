# Group members; Esteban Galvan & Lance Espino
# problem 1: student grade categorization
#ask the user to enter a list of student scores one by one using a while loop that will keep accepting scores until a negative value is applied
#use nested if statements for scores, 100-90 will print "excellent", 89-70 will print "good", 69-50 will print "pass", 50 and below will print "fail"
#the loop stops if the user enters a negative number, in which the values they entered will be printed

score = int(input("what is your score? (put a negative value to quit)"))
#getting the user's score
while not score <= -1:
    print(f"your score is {score}")
    score = int(input("what is your score? (enter a negative value to quit)"))    
#the while loop that uses the score entered
    #the nested if statements for the score entered
    if score >= 90: 
        print("Excellent!")
    elif score >= 69: 
        print("Good")
    elif score >= 50:
        print("Pass")
    elif score <=49:
        print("FAIL!")

#the list that contains the values inputed
scores = []
for i in range(str((scores))):
    if score != -1:
        scores.append(score)
    elif score <= -1:
        print(f"The following are the scores your entered:")
    for score in scores:
        print(score)
#will print out the scores that were inputed by the user
print("negative value entered, I assume you're quitting.")
#the statement used when the user enters a negative number





# problem 2: Even and Odd Counter with Conditions
# ask the user for a starting and ending number
# use a for loop to iterate from the starting to ending number, inside the loop: use nested if to check if the number is both even and greater than 10.
# if true, count it as a "special even" number. if it's odd and less than 20, count it as "special odd" number.
# print the counts for both "special even" and "special odd" numbers.

starting_number = int(input("Enter a starting number: ")) # this asks the user for a starting number
ending_number = int(input("Enter an ending number: ")) # this asks the user for an ending number

for number in range(starting_number, ending_number): # this for loop iterates from the starting and ending numbers
    if (number % 2) == 0 and number > 10: # this checks if the number is both even and greater than 10, marking the number as "special even"
        print(f"{number} is a special even number")
    elif (number % 2) != 0 and number < 20: # this checks if the number is both odd and less than 20, marking the number as "special odd"
        print(f"{number} is special odd number")