#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

n = input("enter a number: ")
n = float(n)

if n==int(n):
    print("this number is an integer")
else:
    print("this number is not an integer")

