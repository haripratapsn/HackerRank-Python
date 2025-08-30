# Here is the exact text in the provided photo:

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description
# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string

# int max_width: the width to wrap to

# Returns

# string: a single string with newline characters ('\n') where the breaks should be

# Input Format

# The first line contains a string, string.
# The second line contains the width, max_width

#Method 1
# import textwrap

# def wrap(string, max_width):
#     wrapped=textwrap.fill(string,max_width)
#     return wrapped

# if __name__ == '__main__':
#     string, max_width = input("Enter the string : "), int(input("Enter the max width: "))
#     result = wrap(string, max_width)
#     print(result)


#Method 2
import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        chunk=string[i:i+max_width]
        if len(chunk)==max_width:
            print(chunk)
        else:
            return chunk
    
if __name__ == '__main__':
    string, max_width = input("Enter the string : "), int(input("Enter the max width: "))
    result = wrap(string, max_width)
    print(result)











# string="ABCDEFGHIJKLIMNOQRSTUVWXYZ hari"
# max_width=4
# wrapped =textwrap.wrap(string,max_width)
# fill=textwrap.fill(string,max_width)
# split=string.split()
# print(wrapped)
# print(fill)
# print(split)