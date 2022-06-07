#Calculator Project Assignment for Y1-TA @ MEET Summer 2022.
import turtle

#Answers List.
Answ_List = []

#Variables
Stage = 0
Num1 = 0
Num2 = 0
Operation = ""
IsRunning = True

#Calculator Screen.
SIZE_X=500
SIZE_Y=500  
turtle.setup(SIZE_X, SIZE_Y)
turtle.tracer(1,0)
t = turtle.Turtle()
tDel = t.clone()
t.hideturtle()
tDel.hideturtle()
t.left(90)


############################################################################################

#Drawing The GUI Buttons.

def DrawButton(startX, startY, symbol):
  t.penup()
  t.goto(startX, startY)
  t.pendown()
  t.goto(startX, startY + 40)
  t.goto(startX + 62.5, startY + 40)
  t.goto(startX + 62.5, startY)
  t.goto(startX, startY)
  t.penup()
  t.goto(startX + 20, startY - 5)
  t.write(symbol, font=('Courier', 30, 'bold'))

def DrawRowButton(startX, startY, symbol):
  t.penup()
  t.goto(startX, startY)
  t.pendown()
  t.goto(startX, startY + 40)
  t.goto(startX + 280, startY + 40)
  t.goto(startX + 280, startY)
  t.goto(startX, startY)
  t.penup()
  t.goto(startX + 125, startY - 5)
  t.write(symbol, font=('Courier', 30, 'bold'))
  
#btn0
DrawButton(-240, -240, "0")

#btn1
DrawButton(-240, -190, "1")

#btn4
DrawButton(-240, -140, "4")

#btn7
DrawButton(-240, -90, "7")

#btnC
DrawButton(-167.5, -240, "C")

#btn2
DrawButton(-167.5, -190, "2")

#btn5
DrawButton(-167.5, -140, "5")

#btn8
DrawButton(-167.5, -90, "8")

#btn+
DrawButton(-95, -240, "+")

#btn3
DrawButton(-95, -190, "3")

#btn6
DrawButton(-95, -140, "6")

#btn9
DrawButton(-95, -90, "9")

#btn-
DrawButton(-22.5, -240, "-")

#btn*
DrawButton(-22.5, -190, "*")

#btn/
DrawButton(-22.5, -140, "/")

#btn^
DrawButton(-22.5, -90, "^")

#btn=
DrawRowButton(-240, -40, "=")

#Defining The GUI Buttons.

#btn0
def btnZero():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "0")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "0")
    Stage = 2
    # print(Num2)

#btn1
def btnOne():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "1")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "1")
    Stage = 2
    # print(Num2)
  
#btn4
def btnFour():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "4")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "4")
    Stage = 2
    # print(Num2)
  
#btn7
def btnSeven():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "7")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "7")
    Stage = 2
    # print(Num2)
  
#btnC
def btnC():
  global Stage
  global Num1
  global Num2
  global Operation
  
  Stage = 0
  Num1 = 0
  Num2 = 0
  Operation = ""
  delete()
  print("\nReset")
  
#btn2
def btnTwo():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "2")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "2")
    Stage = 2
    # print(Num2)
  
#btn5
def btnFive():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "5")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "5")
    Stage = 2
    # print(Num2)
  
#btn8
def btnEight():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "8")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "8")
    Stage = 2
    # print(Num2)
  
#btn+
def btnAdd():
  global Stage
  global Operation
  if (Stage == 0):
    Operation = "+"
    Stage += 1
    # print(Operation)
  
#btn3
def btnThree():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "3")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "3")
    Stage = 2
    # print(Num2)
  
#btn6
def btnSix():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "6")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "6")
    Stage = 2
    # print(Num2)
  
#btn9
def btnNine():
  global Num1
  global Num2
  global Stage
  if (Stage == 0):
    Num1 = int(str(Num1) + "9")
    # print(Num1)
  elif (Stage == 1 or Stage == 2):
    Num2 = int(str(Num2) + "9")
    Stage = 2
    # print(Num2)

#btn-
def btnSub():
  global Stage
  global Operation
  if (Stage == 0):
    Operation = "-"
    Stage += 1
    # print(Operation)

#btn*
def btnMulti():
  global Stage
  global Operation
  if (Stage == 0):
    Operation = "*"
    Stage += 1
    # print(Operation)

#btn/
def btnDivide():
  global Stage
  global Operation
  if (Stage == 0):
    Operation = "/"
    Stage += 1
    # print(Operation)

#btn^
def btnPower():
  global Stage
  global Operation
  if (Stage == 0):
    Operation = "^"
    Stage += 1
    # print(Operation)

#btn=
def btnEqual():
  global Stage
  if (Stage == 2):
    Stage += 1
    # print("=")

  
############################################################################################

#Calculator Answer Screen.
t.goto(-240,10)
t.pendown()
t.goto(-240,240)
t.goto(40,240)
t.goto(40,10)
t.goto(-240,10)
t.penup()

#Calculator Answer Screen Delete.
def delete():
    tDel.penup()
    tDel.fillcolor("white")
    tDel.begin_fill()
    tDel.goto(-235,15)
    tDel.goto(-235,235)
    tDel.goto(35,235)
    tDel.goto(35,15)
    tDel.goto(-235,15)
    tDel.end_fill()
                

#Calculator History.
t.penup()
t.goto(50,250)
t.pendown()
t.goto(50,-250)
t.penup()
t.goto(90,215)
t.write("History", font=('Courier', 20, 'bold'))
t.goto(250,210)
t.pendown()
t.goto(50,210)
t.penup()
t.goto(60,180)


#Clear Calculator History.
def btnClearHistory():
  t.fillcolor("white")
  t.begin_fill()
  t.goto(55,210)
  t.goto(1000,210)
  t.goto(1000,-250)
  t.goto(55,-250)
  t.goto(55,210)
  t.end_fill()
  t.goto(50,210)
  t.pendown()
  t.goto(1000,210)
  t.penup()
  t.penup()
  t.goto(240,-230)
  t.pendown()
  t.goto(180,-230)
  t.goto(180,-210)
  t.goto(240,-210)
  t.goto(240,-230)
  t.penup()
  t.goto(185,-230)
  t.write("Clear", font=("Courier", 12, 'bold'))
  t.goto(60,180)

btnClearHistory() 


def clickHandler(x,y):
  # clear
  if x > 180 and x < 240 and y > -230 and y < -210:
    btnClearHistory()
    print("\nCleared History!")
  ##########
  # btn0
  elif x > -240 and x < -177.5 and y > -240 and y < -200:
    btnZero()
  # btn1
  elif x > -240 and x < -177.5 and y > -190 and y < -150:
    btnOne()
  # btn4
  elif x > -240 and x < -177.5 and y > -140 and y < -100:
    btnFour()
  # btn7
  elif x > -240 and x < -177.5 and y > -90 and y < -50:
    btnSeven()
  ##########
  # btnC
  elif x > -167.5 and x < -105 and y > -240 and y < -200:
    btnC()
  # btn2
  elif x > -167.5 and x < -105 and y > -190 and y < -150:
    btnTwo()
  # btn5
  elif x > -167.5 and x < -105 and y > -140 and y < -100:
    btnFive()
  # btn8
  elif x > -167.5 and x < -105 and y > -90 and y < -50:
    btnEight()
  ##########
  # btn+
  elif x > -95 and x < -32.5 and y > -240 and y < -200:
    btnAdd()
  # btn3
  elif x > -95 and x < -32.5 and y > -190 and y < -150:
    btnThree()
  # btn6
  elif x > -95 and x < -32.5 and y > -140 and y < -100:
    btnSix()
  # btn9
  elif x > -95 and x < -32.5 and y > -90 and y < -50:
    btnNine()
  ##########
  # btn-
  elif x > -22.5 and x < 40 and y > -240 and y < -200:
    btnSub()
  # btn*
  elif x > -22.5 and x < 40 and y > -190 and y < -150:
    btnMulti()
  # btn/
  elif x > -22.5 and x < 40 and y > -140 and y < -100:
    btnDivide()
  # btn^
  elif x > -22.5 and x < 40 and y > -90 and y < -50:
    btnPower()
  ##########
  # btn=
  elif x > -240 and x < 40 and y > -40 and y < 0:
    btnEqual()

turtle.onscreenclick(clickHandler, 1)
turtle.listen


#Defining The Calculator Operations And Their Functions.
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return x ** y


############################################################################################

#History List Print.
def hlp():
  global Stage
  Stage += 1
  for i in range(len(Answ_List)):
    ##print(Answ_List[i])
    t.write(Answ_List[i], font=('Courier', 20, 'bold'))
    Answ_List.clear()
    t.backward(25)

#Welcome & Instructions Text.
print("Welcome To George's Helpful Calculator!\nThe Operations That Are Available Are:")
print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Exponent(^)")
print("Press On The GUI Buttons To Do Math!")
# input("\nPress Enter to Start")

#Defining The Calculation Function, Handling User Inputs & Errors.
def PerformCalc():
  global Stage
  global Num1
  global Num2
  global Operation
  global IsRunning
  while (IsRunning == True):
    if (Stage == 0):
      if (len(str(Num1)) < 22):
        if (Num1 != 0):
          tDel.penup()
          tDel.goto(-200,200)
          tDel.write(Num1, font=('Courier', 13))
        else:
          delete()
          tDel.penup()
          tDel.goto(-200,200)
          tDel.write(Num1, font=('Courier', 13))
      elif (len(str(Num1)) == 22):
        tDel.penup()
        tDel.goto(-200,200)
        tDel.write(str(Num1) + "~", font=('Courier', 13))
      else:
        tDel.penup
        tDel.goto(-200,200)

    elif (Stage == 1):
      tDel.goto(-200,175)
      tDel.write(Operation, font=('Courier', 13))
      
    elif (Stage == 2):
      if (len(str(Num2)) < 22):
        tDel.goto(-200,150)
        tDel.write(Num2, font=('Courier', 13))
      elif (len(str(Num2)) == 22):
        tDel.goto(-200,150)
        tDel.write(str(Num2) + "~", font=('Courier', 13))
      else:
        tDel.penup
        tDel.goto(-200,150)
        
    elif (Stage == 3):
      try:
        Answ = 0
        if Operation == '+':
          Answ = add(Num1, Num2)
          print("\nAnswer:", Num1, "+", Num2, "=", Answ)
          tDel.goto(-200,125)
          tDel.write("=", font=('Courier', 13, 'bold'))
  
  
        elif Operation == '-':
          Answ = subtract(Num1, Num2)
          print("\nAnswer:", Num1, "-", Num2, "=", Answ)
          tDel.goto(-200,125)
          tDel.write("=", font=('Courier', 13, 'bold'))
  
  
        elif Operation == '*':
          Answ = multiply(Num1, Num2)
          print("\nAnswer:", Num1, "*", Num2, "=", Answ)
          tDel.goto(-200,125)
          tDel.write("=", font=('Courier', 13, 'bold'))
  
  
        elif Operation == '/':
          Answ = divide(Num1, Num2)
          print("\nAnswer:", Num1, "/", Num2, "=", Answ)
          tDel.goto(-200,125)
          tDel.write("=", font=('Courier', 13, 'bold'))
  
  
        elif Operation == '^':
          Answ = power(Num1, Num2)
          print("\nAnswer:", Num1, "^", Num2, "=", Answ)
          tDel.goto(-200,125)
          tDel.write("=", font=('Courier', 13, 'bold'))
  
        if (len(str(Answ)) < 22):
          tDel.goto(-200,100)
          tDel.write(Answ, font=('Courier', 13, 'bold'))
          Answ_List.append(Answ)
          hlp()
        else:
          tDel.goto(-200,100)
          tDel.write(str(Answ)[0:22] + "~", font=('Courier', 13, 'bold'))
          Answ_List.append(Answ)
          hlp()
          
      except ZeroDivisionError:
        tDel.goto(-200,50)
        tDel.write("ERROR \n'Can't Divide By Zero'", font=('Courier', 13, 'bold'))
      except OverflowError:
        tDel.goto(-200,50)
        tDel.write("ERROR \n'The Number Is \nToo Big To Handle'", font=('Courier', 13, 'bold'))        
        
    else:
      tDel.goto(0,0)

    
PerformCalc()
t.mainloop()
    
# #Defining The Calculation Function, Asking For The User's Input & Error Handling.
# def calculate():
#     try:
#         delete()
#         x = float(input("\nEnter Your First Number: "))
#         tDel.penup()
#         tDel.goto(-200,200)
#         tDel.write(x, font=('Courier', 13, 'bold'))
#         y = float(input("Enter Your Second Number: "))
#         tDel.goto(-200,150)
#         tDel.write(y, font=('Courier', 13, 'bold'))

        
#     except ValueError:
#         print("ERROR 'Integers Only'")
#         calculate()
#     else:
#         try:            
#             operation = input("Enter Your Operation Of Choice: ")
#             tDel.goto(-200,175)
#             tDel.write(operation, font=('Courier', 13, 'bold'))
#             if operation in ('+', '-', '*', '/', '^'):

#                 if operation == '+':
#                     Answ1 = add(x, y)
#                     print("Answer:", x, "+", y, "=", Answ1)
#                     tDel.goto(-200,125)
#                     tDel.write("=", font=('Courier', 13, 'bold'))
#                     tDel.goto(-200,100)
#                     tDel.write(Answ1, font=('Courier', 13, 'bold'))
#                     Answ_List.append(Answ1)
#                     hlp()

#                 elif operation == '-':
#                     Answ2 = subtract(x, y)
#                     print("Answer:", x, "-", y, "=", Answ2)
#                     tDel.goto(-200,125)
#                     tDel.write("=", font=('Courier', 13, 'bold'))
#                     tDel.goto(-200,100)
#                     tDel.write(Answ2, font=('Courier', 13, 'bold'))
#                     Answ_List.append(Answ2)
#                     hlp()

#                 elif operation == '*':
#                     Answ3 = multiply(x, y)
#                     print("Answer:", x, "*", y, "=", Answ3)
#                     tDel.goto(-200,125)
#                     tDel.write("=", font=('Courier', 13, 'bold'))
#                     tDel.goto(-200,100)
#                     tDel.write(Answ3, font=('Courier', 13, 'bold'))
#                     Answ_List.append(Answ3)
#                     hlp()

#                 elif operation == '/':
#                     Answ4 = divide(x, y)
#                     print("Answer:", x, "/", y, "=", Answ4)
#                     tDel.goto(-200,125)
#                     tDel.write("=", font=('Courier', 13, 'bold'))
#                     tDel.goto(-200,100)
#                     tDel.write(Answ4, font=('Courier', 13, 'bold'))
#                     Answ_List.append(Answ4)
#                     hlp()

#                 elif operation == '^':
#                     Answ5 = power(x, y)
#                     print("Answer:", x, "^", y, "=", Answ5)
#                     tDel.goto(-200,125)
#                     tDel.write("=", font=('Courier', 13, 'bold'))
#                     tDel.goto(-200,100)
#                     tDel.write(Answ5, font=('Courier', 13, 'bold'))
#                     Answ_List.append(Answ5)
#                     hlp()

#             else:
#                 print("ERROR 'Invalid Operation'")
#                 calculate()
#         except ZeroDivisionError:
#             print("ERROR 'Can Not Divide By Zero'")
#             calculate()
#         except OverflowError:
#             print("ERROR 'The Number Is Too Big For The Computer To Handle'")
#             calculate()
#         else:
#             rerun()


# #Asking If The User Wants To Continue Or Stop Using The Calculator.    
# def rerun():

#     run_again = input("\nWould you like to calculate again?\nPlease Type Y for Yes or N for No: ")
      
#     if run_again.upper() == "Y":
#         calculate()

#     elif run_again.upper() == "N":
#         print("Good Luck!")
#         quit()

#     else:
#         rerun()


    
# calculate()


      
# t.mainloop()
