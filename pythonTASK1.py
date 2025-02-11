
#1. program to add two numbers...........
num1 = 15
num2 = 12
sum = num1 + num2
print("Sum of", num1, "and", num2 , "is", sum)

 #-----------------------------------

# 2.program of odd and even numbers.......
# Taking user input
number = int(input("Enter a number : "))

# Condition checking

# if the number is divisible by 2, then even
# else number is odd
if number%2==0:
  print(number, "is even.")
else:
  print(number, "is odd.")

  #-----------------------------------
  
# 3. program of factorial calculation.....

n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
    	factorial=factorial *i
print("Factorial of the given number is: ", factorial)

  #-----------------------------------

# 4. program of fibonacci series.....
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

        #-------------------------------------

# 5. program to reverse a string....

#  Reverse a string    
# using  slice syntax   
# reverse(str) Function to reverse a string   
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "JavaTpoint"  
print ("The original string  is : ",s)   
print ("The reversed string  is : ",reverse(s))

   #-------------------------------------

# 6. program of palindrome check...

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("True")
else:
    print("False")

      #---------------------------------------------
# 7. program for leap year check.....

def is_leap_year_modulo(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example
year_to_check = 2024
result_modulo = is_leap_year_modulo(year_to_check)
print(f"{year_to_check} is a leap year: {result_modulo}")

      #---------------------------------------------
# 8. program to check amstrong number....
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False
num=153
print(is_armstrong(num))


