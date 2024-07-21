# Simple GeometryLibpy #

## What is this? ##
Python lib that allows to calculate area of geometric figures

----------

## Using ##

Using the library is as simple and convenient as possible:
Install: 
    
    pip install geometryLibPy

Let's import it first:
First, import everything from the library (use the `from `...` import *` construct).

Examples of all operations:

### Triangle ###

Create a triangle and get it area:

    triangle = Triangle([15, 9, 7])
    area = triangle.get_area()
    print(area)


Resize the triangle and get updated area:

    triangle.update_sides([5, 6, 7])
    area = triangle.get_area()
    print(area)

### Circumference ###
Create a circumference and get area:

    circle = Circumference(5)
    area = circle.get_area()
    print(area)


Update radius of the circumference and get new area:

    circle.update_radius(4)
    area = circle.get_area()
    print(area)
----------


## UnitTest ##

Run in terminal in root directory:
    
    cd GeometryLibPy
    python -m unittest -v testLib 
    

----------

## Developer ##
My GitHub: [**_Link_**](https://github.com/mav735) 