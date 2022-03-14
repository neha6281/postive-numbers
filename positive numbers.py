#positive numbers
#using for loop
list1 = [5,-3,0,23,-6,8]
for num  in list1:
  if num >=0:
    print (num,end = " ")
    
    
#using while loop 
list1 = [5,-3,0,23,-6,8]
num = 0
while (num < len(list1)):
  if list1[num] >=0:
      print(list1[num],end = " ")
  num += 1
