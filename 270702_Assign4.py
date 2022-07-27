import random                                               # import library random     
N = int(input("How many stick in the pile : "))             # รับค่า stick
print("There are",N,"sticks in the pile.")
name = str(input("What is your name : "))                   # รับค่า ชื่อผู้เล่น

i = 1                                                       # กำหนดให้ i=1 เพื่อให้คอมพิวเตอร์เริ่มก่อน
while(N != 0):                                              # เช็คว่ายังมี stick เหลืออยู่ให้เข้าลูป
  if(i%2 == 0):                                             # เช็คเทิร์นของผู้เล่น ถ้า i%2 = 0 เป็นเทิร์นของผู้เล่น ถ้า i%2 = 1 เป็นเทิร์นของคอมพิวเตอร์
    x = int(input(str(name) + ", how many stick you will take? (1 or 2): "))    # รับค่า stick จากผู้เล่น
  else:                                                     # เทิร์นของคอมพิวเตอร์
    if((N-1)%3 == 1):                                       # ถ้า (N-1)%3 == 1 ให้คอมพิวเตอร์หยิบ stick = 1
      x = 1                       
    elif((N-1)%3 == 2):                                     # ถ้า (N-1)%3 == 2 ให้คอมพิวเตอร์หยิบ stick = 2
      x = 2
    else:                                                   # ถ้า (N-1)%3 == 0 ให้คอมพิวเตอร์หยิบ stick แบบ random
      x = random.randint(1,2)                               # computer random sticks 
    print("Computer, takes: ",x)                            
  if(x > 2):                                                # เช็คว่าหยิบ stick มากกว่า 2 หรือเปล่า ถ้าหยิบมากกว่า 2 จะขึ้นข้อความแจ้งเตือน แล้วให้ทำการหยิบใหม่
    print("No you cannot take more than 2 stick!")          
  elif(x < 1):                                              # เช็คว่าหยิบ stick น้อยกว่า 1 หรือเปล่า ถ้าน้อยกว่า 1 จะขึ้นข้อความแจ้งเตือน แล้วให้ทำการหยิบใหม่
    print("No you cannot take less than 1 stick!")
  elif(N - x < 0):                                          # เช็คว่ามี stick ในกองมีพอให้หยิบหรือไม่ ถ้าไม่พอ จะขึ้นข้อความแจ้งเตือน แล้วให้ทำการหยิบใหม่
    print("There are no enough sticks to take.")
  else:                                                     # นอกเหนือจากการเช็คเงื่อนไขข้างต้น จะทำการสรุปว่าเงื่อนไขการหยิบถูกต้อง
    N = N-x                                                 # อัพเดตจำนวน stick in the pile 
    if(N == 0):                                             # หลังจากหยิบ เช็คว่ามี stick เหลืออยู่หรือไม่ ถ้ามีจะแสดงข้อความจำนวน stick ที่เหลือ
      if(i%2 == 0):                                         # ถ้าไม่มี stick เหลืออยู่ในกอง แล้ว i%2 == 0 จะแสดงว่า Computer ชนะ 
        print(name,end=", take the last stick.\n")
        print("Computer win !!!")
      else:                                                 # ถ้าไม่มี stick เหลืออยู่ในกอง แล้ว i%2 == 1 จะแสดงว่า ผู้เล่น ชนะ
        print("Computer, take the last stick.")
        print(name,"win (Computer, am sad T_T)")
    else:                                                   # ยังมี stick เหลืออยู่ในกอง จะแสดงข้อความจำนวน stick ที่เหลือ
      print("There are",N,"sticks in the pile.\n")
    i += 1                                                  # อัพเดตค่า i เพื่อเปลี่ยนตาผู้เล่น

      
