

'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/13/2023
Lab: lab09
Last modified: 11/14/2023
Purpose: A program that defines a class representing a circle as a data type.
'''

#Circle Class

#import math

from math import pi


class Circle:
    def __init__(self, radius, x_pos, y_pos):
        self.radius = radius
        self.x_pos = x_pos
        self.y_pos = y_pos

    def diameter(self):
        return self.radius*2

    def area(self):
        return pi*(self.radius**2)

    def circumference(self):
        return pi*2*self.radius

    def dist_to_origin(self):
        return (self.x_pos**2 + self.y_pos**2)**0.5

    def dist_to_center(self, other):
        return ((self.x_pos-other.x_pos)**2 + (self.y_pos-other.y_pos)**2)**0.5

    def is_inside(self, other_circle):
        return (self.dist_to_center(other_circle) + self.radius <= other_circle.radius)  


    def is_overlap(self, other_circle):
        if(self.is_inside(other_circle) or other_circle.is_inside(self)):
            return True
        elif(self.radius > other_circle.radius):
            return ((self.radius - other_circle.radius) <= self.dist_to_center(other_circle) <= (self.radius + other_circle.radius))
        else:
            return ((other_circle.radius - self.radius) <= self.dist_to_center(other_circle) <= (self.radius + other_circle.radius))


    def intersect_count(self, other_circle):
        biggerRad = 0
        
        if(self.radius > other_circle.radius):
            if(self.dist_to_center(other_circle) == self.radius + other_circle.radius):
                return 1
            elif(self.dist_to_center(other_circle) == self.radius - other_circle.radius):
                return 1
            elif(self.dist_to_center(other_circle) == 0 and self.radius == other_circle.radius):
                return 1
            elif(self.radius - other_circle.radius < self.dist_to_center(other_circle) < self.radius + other_circle.radius):
                return 2
            else:
                return 0

        else:
            if(self.dist_to_center(other_circle) == self.radius + other_circle.radius):
                return 1
            elif(self.dist_to_center(other_circle) == other_circle.radius - self.radius):
                return 1
            elif(self.dist_to_center(other_circle) == 0 and self.radius == other_circle.radius):
                return 1
            elif(other_circle.radius - self.radius < self.dist_to_center(other_circle) < self.radius + other_circle.radius):
                return 2
            else:
                return 0
        
                        

       
            
        




        
        
