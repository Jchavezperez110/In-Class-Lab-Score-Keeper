#CIS WEEK 12
#LIST EXAMPLES

#OLD SCHOOL 
#ONE EXAMPLE PER DAY

day1 = 72
day2 = 68
day3 = 105
day4 = 22
day5 = -50

#A list is a collection of items in a particular order. 
# Lists are mutable, meaning you can change their content without changing their identity.
temps = [72, 68, 105, 22, -50]

print(temps) #print the whole list
print(temps[0]) #print the first item in the list
print(temps[4]) #print the last item in the list
temps[1] = 77 #change the second item in the list
print(temps) #print the whole list again to see the change

print(len(temps)) #print the length of the list
print()
print()
print("===============================")


NUM_SCORES = 5

scores = [] #create an empty list
for i in range(NUM_SCORES): 
    score = int(input("Enter a score: ")) #get a score from the user
    scores.append(score) #add the score to the list

#print the scores back with their quiz number
#i counts positions from 0, people count from 1, so we add 1 to i when printing
for i in range(len(scores)):
    print("Quiz", i + 1, "score:", scores[i]) #print the quiz number and the score

print()
print()
print("===============================")

#Example 3: Process the array
total = 0
for score in scores:
    total = total + score
average = total / len(scores)

highest = scores[0]
lowest = scores [0]
for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print("Total:", total)
print("Average:", format(average, ".2f"))
print("Highest:", highest)
print("Lowest:", lowest)
