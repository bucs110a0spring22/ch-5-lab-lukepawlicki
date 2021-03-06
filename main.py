'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
  Draws the outline of the square for the dartboard
  args: myturtle- str, turtle object used to draw the square
        width- int, length of each side of the square
        top_left_x- int, x value of the top left of the square
        top_left_y- int, y value of the top left of the square
  '''
  myturtle.up()
  myturtle.goto(top_left_x,top_left_y)
  myturtle.down()
  for i in range(4):
    myturtle.forward(width)
    myturtle.right(90)
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  '''
  Draws the x and y axes for the dartboard
  args: myturtle- str, turtle object used to draw the axes
        x_start- int, x value of where the turtle starts the line
        y_start- int, y value of where the turtle starts the line 
        x_end- int, x value of where the turtle ends the line
        y_end- int, y value of where the turtle ends the line
  '''
  myturtle.up()
  myturtle.goto(x_start,y_start)
  myturtle.down()
  myturtle.goto(x_end,y_end)
def drawCircle(myturtle=None, radius=0):
  '''
  Draws the outline of the circle for the dartboard
  args: myturtle- str, turtle object that draws the circle
        radius- int, radius of the circle
  '''
  myturtle.goto(0,-1)
  myturtle.circle(radius, steps=100)
def setUpDartboard(myscreen=None, myturtle=None):
  '''
  Calls previous functions to set up the dartboard
  args: myscreen- str, window where the dartboard can be seen
        myturtle- str, turtle that draws the board
  '''
  turtle.setworldcoordinates(-1,-1,1,1)
  drawSquare(myturtle, width=2, top_left_x=-1, top_left_y=1)
  drawLine(myturtle,-1,0,1,0)
  drawLine(myturtle,0,-1,0,1)
  drawCircle(myturtle,1)
def throwDart(myturtle=None):
  '''
  Sends the turtle to a random location within the square/circle to simulate throwing a dart, dot is blue if the turtle is in the circle and red if the turtle is outside of the circle
  args: myturtle- str, used to simulate the action of throwing a dart
  return: boolean expression depending on whether the dot is inside the circle or not
  '''
  x = random.uniform(-1,1)
  y = random.uniform(-1,1)
  myturtle.up()
  myturtle.goto(x,y)
  if myturtle.distance(0,0) <= 1:
    myturtle.dot('blue')
  else:
    myturtle.dot('red')
def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  '''
  Determines if the dot is inside the circle 
  args: myturtle- str, turtle object that makes the dots
        circle_center_x- int, x value of the center of the circle 
        circle_center_y- int, y value of the center of the circle 
        radius- int, radius of the circle 
  return: boolean, true if the turtle is in the circle and false if not
  '''
  if myturtle.distance(circle_center_x,circle_center_y) <= 1:
    return True
  else:
    return False
def playDarts(myturtle=None):
  '''
  Simulates a game of darts between two players where each player has 10 shots
  args: myturtle- str, turtle object used to simulate the game of darts
  '''
  accum_1 = 0
  accum_2 = 0
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,0):
      accum_1 = accum_1 + 1
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,0):
      accum_2 = accum_2 + 1
  if accum_1 > accum_2:
    print('Player 1 Wins!')
  elif accum_1 < accum_2:
    print('Player 2 Wins!')
  elif accum_1 == accum_2:
    print('The Game is a Tie!')
def montePi(myturtle=None, number_darts=0):
  '''
  Estimates the value of pi using the ration of the area of the circle to the area of the square
  args: myturtle- str, creates the dots for the simulation
        number_darts- int, user inputs the number of darts to be used for the approximation
  return: int, returns approximation of pi
  '''
  inside_count = 0
  for i in range(number_darts):
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,0):
      inside_count = inside_count + 1
  approx = 4*(inside_count/number_darts)
  return approx
      
  
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
      throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
