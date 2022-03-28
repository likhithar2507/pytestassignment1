def area_square(side):
    Area = side * side
    return Area


def perimeter_rect(l, w):
    perimeter = 2 * (l + w)
    return perimeter


def area_rect(l, b):
    Area = l * b
    return Area

def area_circle(r):
    PI = 3.14
    Area = PI * r * r
    return Area

def area_triangle(a,b,c):
    s = (a + b + c) / 2
    Area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return Area

if __name__=="__main__":
    while True:
        print("1. Calculate area of Rectangle ")
        print("2. Calculate perimeter of a rectangle ")
        print("3. Calculate area of Circle ")
        print("4. Calculate area of Square ")
        print("5. Calculate area of Triangle ")
        print("6. EXIT ")

        choice=int(input("Enter Your choice from the above Menu :"))

        if choice==1:
            l = int(input("Enter the length for finding area of rectangle :"))
            b = int(input("Enter the breath for finding area of rectangle :"))
            arearect = area_rect(l, b)
            print(arearect)

        elif choice==2:
            l = int(input("Enter the Length for finding perimeter of rectangle :"))
            w = int(input("Enter the width for finding perimeter of rectangle :"))
            perimeterrect = perimeter_rect(l, w)
            print(perimeterrect)

        elif choice==3:
            r=int(input("Enter the radius to find the area of circle :"))
            areacircle=area_circle(r)
            print(areacircle)

        elif choice==4:
            side = int(input("Enter the num for finding Area of square :"))
            squarearea = area_square(side)
            print(squarearea)

        elif choice==5:
            a = float(input('Enter the length of first side: '))
            b = float(input('Enter  the length of second side: '))
            c = float(input('Enter  the length of third side: '))
            areatriangle=area_triangle(a,b,c)
            print(areatriangle)

        elif choice==6:
            break

        else:
            print("Oops you hava entered an INVALID choice ....try again by choosing an valid choice!")

