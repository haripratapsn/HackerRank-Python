#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
#  Input Format

# The first line contains n . The second line contains an array A[]  of  integers each separated by a space.

# Output Format

# Print the runner-up score.

def runner_up(array_students):
    array_students = list(array_students)
    array_students.sort(reverse=True)
    for score in range(len(array_students)):
        if array_students[score] != array_students[score + 1]:
            runner_up = array_students[score + 1]
            break
        else:
            continue
    print(runner_up)
            
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)


        
    
