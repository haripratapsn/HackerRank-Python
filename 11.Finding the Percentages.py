# The provided code stub will read a dictionary containing key/value pairs of name:[marks] for a list of students.Print the average of the marks array for the student name provided. Showing 2 places after the decimal.

# Example 
# marks  key:value Pair
# 'alpha':[20,30,40]
# 'beta':[20,30,40]
# query_name='beta'
# the query_name is 'beta' . beta's average score (30 + 50 + 70)/3 =50.0

# Input Format 
# The first line contains the integer n, the number of students; records. 
# The next n lines contain the names and marks obtained by a student , each value separated by a space, The final line contains query_name the name of a student to query.

# Output Format 
# Print one line THe average of the marks obtained by the particular student correct to 2 decimal places
# 

# Input
# 1
# Krishna 67 68 69
# Output

# 26.50 
# 


def get_average(student_marks):
    for name,scores in student_marks.items():
        if name==query_name:
            for score in scores:
                total=score+total
            average=float(total/len(scores))
    print(f'{average:.2f}')

if __name__ == '__main__':
    n=int(input('Enter the number of Students :'))
    student_marks={}
    for _ in range(n):
        name,*line =input('Enter Name: ').split()
        scores=list(map,float,line)
        student_marks[name]=scores
    query_name=input("Enter the query name: ")
    get_average(student_marks)




# students_records={'alpha':[20,30,40],'beta':[20,30,40],'gama':[50,50,70],'Teta':[50,60,50]}
# query_name=input('Enter The name :')
# total=0
# for name,scores in students_records.items():
#     if name==query_name:
#         for score in scores:
#             total=score+total
#         average=float(total/len(scores))
# print(f'{average:.2f}')

