
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/13/2023
Lab: lab09
Last modified: 11/15/2023
Purpose: A program that uses the circle class to output information
about user-inputted circle data.
'''

#Driver Module

from circle import Circle


def create_user_circle():
    print("Enter information for Circle: ")

    radius = float(input("Radius: "))
    x_pos = float(input("X Position: "))
    y_pos = float(input("Y Position: "))

    circle = Circle(radius, x_pos, y_pos)
    return circle


def print_circle_info(circ, name="Circle"):

    print(f"""
Information for {name}:
location: ({circ.x_pos}, {circ.y_pos})
diameter: {circ.diameter()}
area: {circ.area()}
circumference: {circ.circumference()}
distance from the origin: {circ.dist_to_origin()}
""")


def main():

    print("Circle 1: ")
    circle1 = create_user_circle()
    
    print("Circle 2: ")
    circle2 = create_user_circle()


    print_circle_info(circle1, name="Circle 1")
    print_circle_info(circle2, name="Circle 2")
    

    print(f"The two circles are {circle1.dist_to_center(circle2)} units apart.")

    if(circle1.is_overlap(circle2)):
        print("The two circles overlap.")
    else:
        print("The two circles do not overlap.")

    if(circle1.is_inside(circle2) or circle2.is_inside(circle1)):
        print("One circle contains the other.")
    else:
        print("Neither circle contains the other.")

    print(f"The two circles intersect each other {circle1.intersect_count(circle2)} time(s).")

    
    

main()





