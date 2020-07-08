
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
	positionbracket = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
			opening_brackets_stack.append(next)
			positionbracket.append(i)




		if next in ")]}":
			# Process closing bracket, write your code here
			if len(opening_brackets_stack) == 0:
				return ("Index of the first unmatched closing bracket is: "+ str(i))


			else:
				previous_bracket = opening_brackets_stack[-1]
				opening_brackets_stack.pop()
				positionbracket.pop()
				if not  (are_matching(previous_bracket,next)) :
					return ("Index of the first unmatched closing bracket is: "+str(i))



    if len(opening_brackets_stack) != 0:
       return ("Index of first unmatched opening bracket is: " + str(positionbracket[0]))


    else:
		return ("Success") ####

def main():
     text = input()
     mismatch = find_mismatch(text)
    # Printing answer, write your code here
     print(mismatch)

if __name__ == "__main__":
    main()
