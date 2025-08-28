# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    my_list=[]
    
    
for i in range(N):
    action=input().split()
    
    if action[0]=="insert":
        my_list.insert(int(action[1]),int(action[2]))
    
    elif action[0]=='print':
        print(my_list)
                
    elif action[0]=="remove":
        my_list.remove(int(action[1]))

    elif action[0]=="append":
        my_list.append(int(action[1]))
        
    elif action[0]=="sort":
        my_list.sort()
    
    elif action[0]=="reverse":
        my_list.reverse()
        
    elif action[0]=="pop":
        my_list.pop()
        
    
    