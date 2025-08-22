#Given the names and grades for each student in a class of N  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

def get_second_lowest(records):
    scores=[]
    second_lowest_name=[]
    for students in records:
        scores.append(students[1])
            
    sorted_scores=sorted(set(scores))
    second_lowest=sorted_scores[1]
    
    for students in records:
        if students[1]==second_lowest:
            second_lowest_name.append(students[0])
    second_lowest_name=sorted(second_lowest_name)
    
    for name in second_lowest_name:
        print(name)

records=[]
for _ in range(5):
    name = input("Enter Your Name:")
    score = float(input("Enter Score:"))
    records.append([name,score])
get_second_lowest(records)
