#Geometry Module

import string

class shapes_2d (object):
    def __init__ (self,sides):
        self.sides = sides
        return print("shape sides is",self.sides)
    
    def coordinates (self):
        sides_counter = 0
        alphabet_list = string.ascii_uppercase
        sides_points = []
        sides_coordinates =[]
        while sides_counter < self.sides:
            sides_points.append("Point_"+alphabet_list[sides_counter])
            sides_points[sides_counter] = [sides_points[sides_counter],input("input x coordinate for "+sides_points[sides_counter]+" ",),input("input y coordinate for "+sides_points[sides_counter]+" ",)]
            print(sides_points[sides_counter])
            sides_coordinates.append(sides_points[sides_counter])
            sides_counter +=1
        return sides_coordinates
    
    def shapes_2d_plot ():
        return
    
shapes_2d_parameter_sides = int(input("input number of sides",))    
first_shape_2d = shapes_2d(shapes_2d_parameter_sides)
first_shape_2d_coordinates = first_shape_2d.coordinates()
print(first_shape_2d_coordinates)