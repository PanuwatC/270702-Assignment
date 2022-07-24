N = int(input("How many stick in the pile : "))
print("There are",N,"sticks in the pile.")
name = str(input("What is your name : "))
count = 0
while(N != 0):
  x = int(input(str(name) + ", how many stick you will take? (1 or 2): "))
  if(x > 2):
    print("No you cannot take more than 2 stick!")
  elif(x < 1):
    print("No you cannot take less than 1 stick!")
  elif(N - x < 0):
    print("There are no enough sticks to take.")
  else:
    N = N-x
    count += 1 
    if(N == 0):
      print("OK. There is no stick left in the pile. You spent",count,"times.")
    elif(N):
      print("There are",N,"sticks in the pile.")
      
      