
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n8306699
#    Student name: Thomas Feldman   
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = []

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#

# Draw the stick figures as per the provided data set
def draw_portrait(dummy_parameter):
    # Defining the function 'hat' to be called into each drawing for Part B of the assesment
    def hat(location, stretch):

        # repeated if elif function that cycles through the second and third (or MyFamily[1] and [2])cell in the portrait lists above to check and assign a position
        # From the background display we can see the coordinates that the pictures need to be placed in,
        # and we have called this position, and variable x in our if statement parametre
        # Stretch is the third cell in the lists and is assigned to y
        #(i did this as it was easier for me to visualise where i was on the canvas if everything was x and y)
        if location == 4:
            x = 300 # If value is 4 in MyFamily[1], variable x = 300
            y = stretch # If value is 4 in MyFamily[2], Assign the value of MyFamily[2] to equal y
        elif location == 3:
            x = 150 # If value is 3 in MyFamily[1], variable x = 150
            y = stretch # If value is 3 in MyFamily[2], Assign the value of MyFamily[2] to equal y
        elif location == 2:
            x = 0 # If value is 2 in MyFamily[1], variable x = 0
            y = stretch # If value is 2 in MyFamily[2], Assign the value of MyFamily[2] to equal y
        elif location == 1:
            x = -150 # If value is 1 in MyFamily[1], variable x = -150
            y = stretch # If value is 1 in MyFamily[2], Assign the value of MyFamily[2] to equal y 
        elif location == 0:
            x = -300 # If value is 0 in MyFamily[1], variable x = -300
            y = stretch # If value is 0 in MyFamily[2], Assign the value of MyFamily[2] to equal y
        else:
            pass # If there isnt anything, skip the function
        
        ## Crown Basic Shape - Each shape is called in this order to have correct layering for the shape stamp
        showturtle()
        tilt(105) # Turns the turtle by angle (105)
        goto(x-20, 200*y) # Using these goto functions, we are calling the x value to align with the middle of the picture and adding or subtracting for either side
        shape('triangle') # and multiplying the y coordinate by stretch
        fillcolor("yellow")
        pencolor("black")
        shapesize(1.5*y,3)
        stamp()
        tilt(345)
        goto(x, 200*y)
        shape('triangle')
        fillcolor("yellow")
        pencolor("black")
        shapesize(1.5*y,3)
        stamp()
        tilt(345)
        goto(x+20, 200*y)
        shape('triangle')
        fillcolor("yellow")
        pencolor("black")
        shapesize(1.5*y,3)
        stamp()
        tilt(285)
        goto(x, 180*y)
        shape('square')
        fillcolor("yellow")
        pencolor("black")
        shapesize(1.5*y,4)
        stamp()
        penup()
        #Gem 1 Right hand side
        goto(x+17.5, 180*y)
        shape('circle')
        fillcolor("red")
        pencolor("black")
        shapesize(0.5*y,0.5)
        stamp()
        penup()
        #Gem 2 middle
        goto(x, 180*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(0.5*y,0.5)
        stamp()
        penup()
        #Gem 3 left hand side
        goto(x-17.5, 180*y)
        shape('circle')
        fillcolor("green")
        pencolor("black")
        shapesize(0.5*y,0.5)
        stamp()
        penup()
        hideturtle()
        
    def kenny (location, stretch):
        # If statement as above
        if location == 4:
            x = 300
            y = stretch
        elif location == 3:
            x = 150
            y = stretch
        elif location == 2:
            x = 0
            y = stretch
        elif location == 1:
            x = -150
            y = stretch 
        elif location == 0:
            x = -300
            y = stretch
        else:
            pass      
    ## Legs - got first to get the right layering with the shape stamp
        showturtle()
        goto(x,20*y)
        shape('square')
        fillcolor("Orange Red")
        pencolor("black")
        shapesize(1.5*y,3,1)
        stamp()
    ## Feet - after legs to be layered ontop of the legs
        goto(15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()
        goto(-15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()
     ## Body (Doubling the Code gives the outline color in black, which is a desired effect)
        goto(x+35,90*y)
        pendown()
        begin_fill()
        color("Orange Red")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand    
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y) #bottom left
        goto(x+35,60*y) #hand 
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        end_fill()
        penup()
        goto(x+35,90*y)
        pendown()
        color("black")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand location marker  
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y) #bottom left
        goto(x+35,60*y) #hand location marker
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        penup()
        # adds the middle of the shirt 
        goto(x,90*y)
        pendown()
        color("black")
        goto(x,35*y)
        penup()
    ## Hands using the above values, stamp hands
        goto(x+40,60*y) #Left hand
        shape('circle')
        fillcolor("Brown")
        pencolor("black")
        shapesize(0.5*y,1,1)
        stamp()
        goto(x-40,60*y) #Right hand
        shape('circle')
        fillcolor("Brown")
        pencolor("black")
        shapesize(0.5*y,1,1)
        stamp()
    ## Head - order for layering
        ## hoodie
        goto(x,120*y)
        shape('circle')
        fillcolor("Orange Red")
        pencolor("black")
        shapesize(5*y,5,1)
        stamp()
        ## inside hood lining
        goto(x,120*y)
        shape('circle')
        fillcolor("brown")
        pencolor("black")
        shapesize(4*y,3,1)
        stamp()
        ## Face
        goto(x,120*y)
        shape('circle')
        fillcolor("wheat")
        pencolor("black")
        shapesize(4*y,2,1)
        stamp()
    ## Eyes - Not quite touching but intended to be almost overlapping in the centre
        goto(x+10.5, 120*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp()
        goto(x-10., 120*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp()
    ##Pupils
        goto(x-7,120*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x+7,120*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
    ## Hoodie Cords - last piece of the kenny picture as he does not have an exposed mouth
        penup()
        color("black")
        goto(x,80*y)
        pendown()
        goto(x+5,56*y)
        penup()
        goto(x,80*y)
        pendown()
        goto(x-5,65*y)
        penup()
        # This if stament is used to search MyFamily[3] to look for *, if the * is in the list, call the hat function with location and stretch as per the fucntion
        if dummy_parameter[MyFamily][3] == '*':
            hat(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        else:
            pass
        hideturtle()
                
    def cartman (location, stretch):
        # Repeated If statement as above
        if location == 4:
            x = 300
            y = stretch
        elif location == 3:
            x = 150
            y = stretch
        elif location == 2:
            x = 0
            y = stretch
        elif location == 1:
            x = -150
            y = stretch 
        elif location == 0:
            x = -300
            y = stretch
        else:
            pass
    ## Legs
        showturtle()
        penup()
        goto(x,20*y)
        shape('square')
        fillcolor("brown")
        pencolor("black")
        shapesize(1.5*y,5,1)
        stamp()
    ## Feet
        goto(25+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,3.5)
        stamp()
        goto(-25+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,3.5)
        stamp()
    ## Body (Doubling the Code gives the outline color in black, which is a desired effect)
        goto(x+55,90*y)
        pendown()
        begin_fill()
        color("red")
        goto(x-55,90*y)
        goto(x-65,75*y) 
        goto(x-65,60*y)
        goto(x-55,60*y) #hand    
        goto(x-55,35*y) #bottom right
        goto(x+55,35*y)
        goto(x+55,60*y) #hand 
        goto(x+65,60*y)
        goto(x+65,75*y)
        goto(x+55,90*y)
        end_fill()
        penup()
        #outline
        goto(x+55,90*y)
        pendown()
        color("black")
        goto(x-55,90*y)
        goto(x-65,75*y) 
        goto(x-65,60*y)
        goto(x-55,60*y) #hand    
        goto(x-55,35*y) #bottom right
        goto(x+55,35*y)
        goto(x+55,60*y) #hand 
        goto(x+65,60*y)
        goto(x+65,75*y)
        goto(x+55,90*y)
        penup()
        ## Middle of shirt and buttons - cartmans buttons are not inline so they have been pushed out at the top and bottom
        goto(x,90*y)
        pendown()
        color("black")
        goto(x,35*y)
        penup()  
        goto(x-6,60*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x-4,50*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x-6,40*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        ## Hands #Left
        goto(x+60,60*y) 
        shape('circle')
        fillcolor("yellow")
        pencolor("black")
        shapesize(0.75*y,1.25,1)
        stamp()
        #Right
        goto(x-60,60*y) 
        shape('circle')
        fillcolor("yellow")
        pencolor("black")
        shapesize(0.75*y,1.25,1)
        stamp()
        # Head
        goto(x,120*y)
        shape('circle')
        fillcolor("wheat")
        pencolor("black")
        shapesize(5*y,6.5,1)
        stamp()
        # Beenie
        penup()
        goto(x,175*y)
        color("cyan")
        pendown()
        begin_fill()
        goto(x+1, 175*y)
        goto(x+15, 172*y)
        goto(x+30,170*y)
        goto(x+45,165*y)
        goto(x+59,145*y)
        goto(x+66,135*y)
        goto(x+66,134*y)
        goto(x-66,134*y)
        goto(x-66,135*y)
        goto(x-59,145*y)
        goto(x-45,165*y)
        goto(x-30,170*y)
        goto(x-15, 172*y)
        goto(x-1, 175*y)
        goto(x,175*y)
        end_fill()
        goto(x-1,175*y)
        penup()
        #outline
        goto(x,175*y)
        color("black")
        pendown()
        goto(x+1, 175*y)
        goto(x+15, 172*y)
        goto(x+30,170*y)
        goto(x+45,165*y)
        goto(x+59,145*y)
        goto(x+66,135*y)
        goto(x+66,134*y)
        goto(x-66,134*y)
        goto(x-66,135*y)
        goto(x-59,145*y)
        goto(x-45,165*y)
        goto(x-30,170*y)
        goto(x-15, 172*y)
        goto(x-1, 175*y)
        goto(x,175*y)
        goto(x-1,175*y)
        penup()
        #yellow edge of beenie
        goto(x-66,134*y)
        color("yellow")
        begin_fill()
        goto(x+66, 134*y)
        goto(x+66, 124*y)
        goto(x-66, 124*y)
        end_fill()
        penup()
        goto(x-66,134*y)
        color("black")
        pendown()
        goto(x+66, 134*y)
        goto(x+66, 124*y)
        goto(x-66, 124*y)
        goto(x-66, 134*y)
        penup()
        #ball ball on benie
        goto(x,175*y)
        shape('circle')
        fillcolor("yellow")
        pencolor("black")
        shapesize(0.5*y,2,1)
        stamp()
        penup()
        ## Eyes
        goto(x+11, 108*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp()
        goto(x-11, 108*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp()     
        #pupil
        goto(x+10, 108*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        goto(x-10, 108*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        # frown
        penup()
        goto(x+7, 81*y)
        pendown()
        goto(x+5, 82*y)
        goto(x+1, 84*y)
        goto(x-1, 84*y)
        goto(x-5, 82*y)
        goto(x-7, 81*y)
        penup()
        #Double Chin
        penup()
        goto(x+10, 75*y)
        pendown()
        goto(x+7, 74*y)
        goto(x+3, 73*y)
        goto(x-3, 73*y)
        goto(x-7, 74*y)
        goto(x-10, 75*y)
        penup()
        # repeated if statement
        if dummy_parameter[MyFamily][3] == '*':
            hat(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        else:
            pass
        hideturtle()
        
    def stan (location, stretch):
        # repeated if statement
        if location == 4:
            x = 300
            y = stretch
        elif location == 3:
            x = 150
            y = stretch
        elif location == 2:
            x = 0
            y = stretch
        elif location == 1:
            x = -150
            y = stretch 
        elif location == 0:
            x = -300
            y = stretch
        else:
            pass
    ## Legs
        showturtle()
        penup()
        goto(x,20*y)
        shape('square')
        fillcolor("royal blue")
        pencolor("black")
        shapesize(1.5*y,3,1)
        stamp()
    ## Feet
        goto(15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()
        goto(-15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()  
    ## Body (Doubling the Code gives the outline color in black, which is a desired effect)
        goto(x+35,90*y)
        pendown()
        begin_fill()
        color("Peru")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand    
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y)
        goto(x+35,60*y) #hand 
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        end_fill()
        penup()
        goto(x+35,90*y)
        pendown()
        color("black")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand    
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y)
        goto(x+35,60*y) #hand 
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        penup()
        ## Middle of shirt and buttons
        goto(x,90*y)
        pendown()
        color("black")
        goto(x,35*y)
        penup()
        goto(x-5,60*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x-5,50*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x-5,40*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25)
        stamp()
    ## Hands
        goto(x+40,55*y) #Left
        shape('circle')
        fillcolor("red")
        pencolor("black")
        shapesize(1*y,1,1)
        stamp()
        goto(x-40,55*y) #Right
        shape('circle')
        fillcolor("red")
        pencolor("black")
        shapesize(1*y,1,1)
        stamp()
    ## Head
        goto(x,110*y)
        shape('circle')
        fillcolor("red")
        pencolor("black")
        shapesize(4.35*y,4,1)
        stamp()
        goto(x,120*y)
        shape('circle')
        fillcolor("wheat")
        pencolor("black")
        shapesize(5*y,5,1)
        stamp()
        ##beanie
        penup()
        goto(x-10,175*y)
        color("blue")
        pendown()
        begin_fill()
        goto(x+10,175*y)
        goto(x+30,165*y)
        goto(x+40,155*y)
        goto(x+47,145*y)
        goto(x+52,135*y)
        goto(x-52,135*y)
        goto(x-47,145*y)
        goto(x-40,155*y)
        goto(x-30,165*y)
        goto(x-10,175*y)
        end_fill()
        goto(x-10,175*y)
        color("black")
        pendown()
        goto(x+10,175*y)
        goto(x+30,165*y)
        goto(x+40,155*y)
        goto(x+47,145*y)
        goto(x+52,135*y)
        penup()
        goto(x-52,135*y)
        pendown()
        goto(x-47,145*y)
        goto(x-40,155*y)
        goto(x-30,165*y)
        goto(x-10,175*y)
        penup()
        #Red bit of beenie
        goto(x-52,135*y)
        color("red")
        begin_fill()
        goto(x+52, 135*y)
        goto(x+52, 125*y)
        goto(x-52, 125*y)
        end_fill()
        penup()
        #ball ball on benie
        goto(x,175*y)
        shape('circle')
        fillcolor("red")
        pencolor("black")
        shapesize(1*y,1,1)
        stamp()
        penup()
     ## Eyes
        goto(x+11, 110*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp() 
        goto(x-11, 110*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        shapesize(1.5*y,1,1)
        stamp()
        #pupil
        goto(x+10, 110*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        goto(x-10, 110*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        #smile
        penup()
        goto(x-15, 85*y)
        pendown()
        begin_fill()
        color("black")
        goto(x+15, 85*y)
        goto(x-5, 75*y)
        goto(x-15, 85*y)
        end_fill()
        penup()
        #teeth
        goto(x-8,82.5*y)
        shape('square')
        fillcolor("white")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x-4,82.5*y)
        shape('square')
        fillcolor("white")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x+0,82.5*y)
        shape('square')
        fillcolor("white")
        shapesize(0.25*y,0.25)
        stamp()
        goto(x+4,82.5*y)
        shape('square')
        fillcolor("white")
        shapesize(0.25*y,0.25)
        stamp()
        # repeated if statement
        if dummy_parameter[MyFamily][3] == '*':
            hat(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        else:
            pass
        hideturtle()
        
        
    def kyle (location, stretch):
        # repeated if statement
        if location == 4:
            x = 300
            y = stretch
        elif location == 3:
            x = 150
            y = stretch
        elif location == 2:
            x = 0
            y = stretch
        elif location == 1:
            x = -150
            y = stretch 
        elif location == 0:
            x = -300
            y = stretch
        else:
            pass
    ## Legs
        showturtle()
        goto(x,20*y)
        shape('square')
        fillcolor("forest green")
        pencolor("black")
        shapesize(1.5*y,3,1)
        stamp()
    ## Feet
        goto(15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()
        goto(-15+x,0*y)
        shape('circle')
        fillcolor("black")
        pencolor("black")
        shapesize(0.5*y,2)
        stamp()
    ## Body (Doubling the Code gives the outline color in black, which is a desired effect)
        goto(x+35,90*y)
        pendown()
        begin_fill()
        color("dark orange")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand    
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y)
        goto(x+35,60*y) #hand 
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        end_fill()
        penup()
        goto(x+35,90*y)
        pendown()
        color("black")
        goto(x-35,90*y)
        goto(x-45,75*y) 
        goto(x-45,60*y)
        goto(x-35,60*y) #hand    
        goto(x-35,35*y) #bottom right
        goto(x+35,35*y)
        goto(x+35,60*y) #hand 
        goto(x+45,60*y)
        goto(x+45,75*y)
        goto(x+35,90*y)
        penup()
        goto(x,90*y)
        pendown()
        color("black")
        goto(x,35*y)
        penup()
        goto(x+20,55*y)
        shape('square')
        fillcolor("dark orange")
        pencolor("dim grey")
        shapesize(1*y,0.5)
        stamp()
        goto(x-20,55*y)
        shape('square')
        fillcolor("dark orange")
        pencolor("dim grey")
        shapesize(1*y,0.5)
        stamp()
    ## Hands
        goto(x+40,60*y) #Left
        shape('circle')
        fillcolor("yellow green")
        pencolor("black")
        shapesize(0.5*y,1,1)
        stamp()
        goto(x-40,60*y) #Right
        shape('circle')
        fillcolor("yellow green")
        pencolor("black")
        shapesize(0.5*y,1,1)
        stamp()
        ## Head
        goto(x,110*y)
        shape('circle')
        fillcolor("forest green")
        pencolor("black")
        shapesize(4.35*y,4,1)
        stamp()
        goto(x,120*y)
        shape('circle')
        fillcolor("wheat")
        pencolor("black")
        shapesize(5*y,5,1)
        stamp()
        ## Eyes
        goto(x+11, 110*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        tilt(15)
        shapesize(1.5*y,1,1)
        stamp() 
        goto(x-11, 110*y)
        shape('circle')
        fillcolor("white")
        pencolor("black")
        tilt(330)
        shapesize(1.5*y,1,1)
        stamp()
        tilt(15)
        #pupil
        goto(x+10, 110*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        goto(x-10, 110*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.25*y,0.25,1)
        stamp()
        ## Beenie
        goto(x+50, 120*y)
        shape('circle')
        fillcolor("yellow green")
        pencolor("black")
        shapesize(2*y,1,1)
        stamp()
        goto(x-50, 120*y)
        shape('circle')
        fillcolor("yellow green")
        pencolor("black")
        shapesize(2*y,1,1)
        stamp()
        goto(x, 155*y)
        shape('square')
        fillcolor("yellow green")
        pencolor("black")
        shapesize(2.25*y,5,1)
        stamp()
        goto(x, 140*y)
        shape('square')
        fillcolor("forest green")
        pencolor("black")
        shapesize(1.25*y,4.5,1)
        stamp()
        # frown
        penup()
        goto(x+7, 81*y)
        pendown()
        goto(x+5, 82*y)
        goto(x+1, 84*y)
        goto(x-1, 84*y)
        goto(x-5, 82*y)
        goto(x-7, 81*y)
        penup()  
        # repeated if statement
        if dummy_parameter[MyFamily][3] == '*':
            hat(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        else:
            pass
        hideturtle()
        
    def mrhankie (location, stretch):
        # repeated if statement
        if location == 4:
            x = 300
            y = stretch
        elif location == 3:
            x = 150
            y = stretch
        elif location == 2:
            x = 0
            y = stretch
        elif location == 1:
            x = -150
            y = stretch 
        elif location == 0:
            x = -300
            y = stretch
        else:
            pass
        ## Mr hankie is sort of one big body
        showturtle()
        goto(x,30*y)
        shape('circle')
        fillcolor("saddle brown")
        pencolor("saddle brown")
        shapesize(3*y,1.5)
        stamp()
        goto(x,80*y)
        shape('circle')
        fillcolor("saddle brown")
        pencolor("saddle brown")
        shapesize(4*y,2)
        stamp()
        goto(x,120*y)
        shape('circle')
        fillcolor("saddle brown")
        pencolor("saddle brown")
        shapesize(3*y,1.5)
        stamp()
        ## Eyes
        goto(x+5,125*y)
        shape('circle')
        fillcolor("white")
        pencolor("white")
        shapesize(1*y,0.5)
        stamp()
        goto(x-5,125*y)
        shape('circle')
        fillcolor("white")
        pencolor("white")
        shapesize(1*y,0.5)
        stamp()
        ## pupils
        goto(x+5,125*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.75*y,0.45)
        stamp()
        goto(x-5,125*y)
        shape('circle')
        fillcolor("black")
        shapesize(0.75*y,0.45)
        stamp()
        ## Smile
        penup()
        goto(x-8, 110*y)
        pendown()
        begin_fill()
        color("black")
        goto(x+8, 110*y)
        goto(x+5, 101*y)
        goto(x-6, 104*y)
        goto(x-8, 110*y)
        end_fill()
        penup()
        #teeth
        goto(x-4.5,108*y)
        shape('square')
        fillcolor("white")
        shapesize(0.2*y,0.2)
        stamp()
        goto(x,108*y)
        shape('square')
        fillcolor("white")
        shapesize(0.2*y,0.2)
        stamp()
        goto(x+4,108*y)
        shape('square')
        fillcolor("white")
        shapesize(0.2*y,0.2)
        stamp()
        ## Hat
        penup()
        goto(x,140*y)
        shape('square')
        fillcolor("white")
        shapesize(0.2*y,1.4)
        stamp()
        goto(x+15 , 142*y)
        begin_fill()
        color("red")
        goto(x-15, 142*y)
        goto(x-10, 150*y)
        goto(x-9, 151*y)
        goto(x-5.5, 152*y)
        goto(x, 154*y)
        goto(x+5.5, 152*y)
        goto(x+9, 151*y)
        goto(x+10, 150*y)
        goto(x+15,142*y)
        end_fill()
        penup()
        goto(x+15 , 142*y)
        color("black")
        pendown()
        goto(x-15, 142*y)
        goto(x-10, 150*y)
        goto(x-9, 151*y)
        goto(x-5.5, 152*y)
        goto(x, 154*y)
        goto(x+5.5, 152*y)
        goto(x+9, 151*y)
        goto(x+10, 150*y)
        goto(x+15,142*y)
        penup()
        ## Santa hat tail
        goto(x-15, 142*y)
        pendown()
        begin_fill()
        color("red")
        goto(x-25, 130*y)
        goto(x-23, 128*y)
        goto(x-14, 135*y)
        goto(x-15, 142*y)
        penup()
        end_fill()
        goto(x-15, 142*y)
        pendown()
        color("black")
        goto(x-25, 130*y)
        goto(x-23, 128*y)
        goto(x-14, 135*y)
        goto(x-15, 142*y)
        penup()
        goto(x-23, 130*y)
        shape('circle')
        fillcolor("white")
        shapesize(0.45*y,0.45)
        stamp()
        penup()
        ## Arms
        goto(x+21, 80*y)
        pendown()
        color("black")
        goto(x+35, 115*y)
        color("white")
        penup()
        stamp()
        goto(x-21, 80*y)
        pendown()
        color("black")
        goto(x-35, 115*y)
        color("white")
        penup()
        stamp()
        # repeated if statement
        if dummy_parameter[MyFamily][3] == '*':
            hat(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        else:
            pass
        hideturtle()

    # This If elseif statement is used to find which person is in the portrait function. It is not working properly because I do not know how to make it search for
    # a varying number in the range. As it stands, this will search through the portrait lists and fin out which people/pet is in it, and give the functions for my
    # pictures a value to use for location and stretch. However it will continue to try to search for 5 different lists, even when there are not 5 in there
    for MyFamily in range(5):
        # If the MyFamily[0] is Person A, then send the second and third values to the Kenny function (location and stretch)
         if dummy_parameter[MyFamily][0] == 'Person A':
                kenny(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        # If the MyFamily[0] is Person A, then send the second and third values to the Cartman function (location and stretch)    
         elif dummy_parameter[MyFamily][0] == 'Person B':
                cartman(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
        # If the MyFamily[0] is Person A, then send the second and third values to the Stan function (location and stretch)    
         elif dummy_parameter[MyFamily][0] == 'Person C':
                stan(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
         # If the MyFamily[0] is Person A, then send the second and third values to the Kyle function (location and stretch)   
         elif dummy_parameter[MyFamily][0] == 'Person D':
                kyle(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
         # If the MyFamily[0] is Person A, then send the second and third values to the MrHankie function (location and stretch)   
         elif dummy_parameter[MyFamily][0] == 'Pet':
                mrhankie(dummy_parameter[MyFamily][1], dummy_parameter[MyFamily][2])
         # if nothing, skip               
         else:
             pass
            
             
        
    pass


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Family: The South Park Gang; Kenny, Cartman, Stan, Kyle, and Mr Hanky)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False

#If you change these my hat is broken because i used tilt :(
draw_locations(True)
draw_labels(True)
mark_coords(True)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False

tracer(True) # making this false kills my program aswell because my last if elif statement is not quite working :(


# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_11)
# Exit gracefully by hiding the cursor and releasing the window
tracer(True)



#
#--------------------------------------------------------------------#









