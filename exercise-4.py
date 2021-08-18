# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print('Enter the lengths of three side of a triangle:')
a = input('a:')
b = input('b:')
c = input('c:')

if a == b and a == c:
    print(f'All sides are equal {a},{b},{c}, this is an equalateral triangle')
elif a != b and a != c and b != c:
    print(f'None of the sides {a},{b},{c}, are equal in length, this is a scalene triangle ')
else:
    print(f'Two sides are equal {a},{b},{c}, this is an isosceles')