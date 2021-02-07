# # number 1

# # change the list if it's necessary
# mylist = [2,4,6,1,2]

# if len(mylist) % 2 == 1:
#   index = len(mylist)//2

#   temp1 = mylist[:index]
#   mid = mylist[index]
#   temp2 = mylist[index+1:]

#   swapped = temp2 + [mid] + temp1

#   print(f"initial list :{mylist}")
#   print(f"swapped list :{swapped}")
# else:
#   index = int(len(mylist)/2)

#   temp1 = mylist[:index]
#   temp2 = mylist[index:]

#   temp2.extend(temp1)
#   print(f"initial list :{mylist}")
#   print(f"swapped list :{temp2}")


# number 2

n = int(input('Enter a number in 0 - 9 range: '))
while n not in range(10):
  print('Invalid number')
  break

print(list(range(0,n+1,2)))



"""
Question: Check the 80th minute of the course
The instruction says to "to print out all of the even number from 0 to n (including n)".
What if n is not an even integer?

for example, let say n=7, 
  then 
    are we expecting the program is gonna print out [0,2,4,6] 
      OR 
    is gonna print out [0,2,4,6,7]

I'm still confusing with the "including" word there, it's a pleasure to have your opinion
"""