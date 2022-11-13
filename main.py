from math import pi

#Function for calculating a surface area for a sphere with user specified radius 
def calculate_surface_area(radius):
    surface_area = 4 * pi * radius ** 2
    print(surface_area)

#Function for calculating a volume for a sphere with user specified radius 
def calculate_volume(radius):
    volume = 4 / 3 * pi * radius ** 3
    print(volume)