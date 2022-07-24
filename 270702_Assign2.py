import random
N = int(input("How many stick in the pile : "))
print("There are",N,"sticks in the pile.")
name = str(input("What is your name : "))

i = 0
while(N != 0):
  if(i%2 == 0):
    x = int(input(str(name) + ", how many stick you will take? (1 or 2): "))
  else:
    x = random.randint(1,2)
    print("Computer, takes: ",x)
  if(x > 2):
    print("No you cannot take more than 2 stick!")
  elif(x < 1):
    print("No you cannot take less than 1 stick!")
  elif(N - x < 0):
    print("There are no enough sticks to take.")
  else:
    N = N-x
    if(N == 0):
      if(i%2 == 0):
        print(name,end=", take the last stick.\n")
        print("Computer win !!!")
      else:
        print("Computer, take the last stick.")
        print(name,"win (Computer, am sad T_T)")
    else:
      print("There are",N,"sticks in the pile.\n")
    i += 1 

      