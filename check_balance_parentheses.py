"""
Write a program which checks if a string has balanced parenthesis.
A balanced parenthesis string starts with an opening character ((, [, {), 
ends with a matching closing character (), ], } respectively), and has only other
matching parenthesis in between.
"""
open_list = ["[","{","("] 
close_list = ["]","}",")"] 

# Function to check parentheses 
def check(myStr): 
	stack = [] 
	for i in myStr: 
		if i in open_list: 
			stack.append(i) 
		elif i in close_list: 
			pos = close_list.index(i) 
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])): 
				stack.pop() 
			else: 
				return "Unbalanced"
	if len(stack) == 0: 
		return "Balanced"

# Driver code 
string = "{[]{()}}"
print(string,"->", check(string)) 

string = "[{}{})(]"
print(string,"->", check(string)) 
