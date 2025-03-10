#find area of circle
#find area of tringle
#find area of square and rectangle
#find simple  interset
#exit.(exit: use infinite while loop for menu)
choice=0
while(choice!=5):
    print("1.find area of circle")
    print("2.find area of tringle")
    print("3.find area of square and rectangle")
    print("4.find simple interset")
    print("5.exit")

    choice=int(input("enter your choice"))
    if choice ==1:
       pi= 3.14
       radius = float (input("please enter the redius of circle:"))
       area = pi * radius * radius
       circumference = 2 * pi * radius
       print("area of circle = % 2.f" %area)
       print("circumference of circle = % 2.f"%circumference)

    elif choice ==2:
        a = float(input("enter first side"))
        b = float(input("enter second side"))
        c = float(input("enter third side"))

        #calculate the semi-perimeter
        s = (a + b +c) / 2
        #calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) **0.5
        print("the area of triangle is % 0.2"%area)

      elif choice == 3:
        side  
