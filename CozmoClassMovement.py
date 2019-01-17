#In this sample code, you will learn how to program Cozmo to
#move forward, turn 90 degrees left or right, spin in a circle
#talk, and perform an animation


#import the cozmo and image libraries
import cozmo

#import libraries for movement 
from cozmo.util import degrees, distance_mm

#we shouldn't need anything for asynchronous behavior
#import asyncio

#import libraries for light colors.  If this library has not been
#acquired, comment out all actions involving colors
#from colors import Colors
#from woc import WOC

#import _thread
#import time

def moveInCircle(robot, speed, seconds):

	robot.say_text("I will spin in three circles").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.BLUE)
	#the first value is the speed for one of the treads, and the second value
	#is the speed for the other tread (left? right?).  They can both be
	#the same sign, or have opposite signs.  the last value is the duration of the
	#movement (measured in seconds?)
	robot.drive_wheels(speed, -1 * speed, None, None, seconds)
   
	#robot.set_all_backpack_lights(Colors.GREEN)
    
	return

def turnRight(robot):
	robot.say_text("I will turn right").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.RED)
	robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
	#robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnLeft(robot):
	robot.say_text("I will turn left").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.BLUE)
	robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
	#robot.set_all_backpack_lights(Colors.GREEN)
	return

unit = 100 #mm
speed = 200 #mmps

def facePosition(currPosition,positionToFace,robot):
    diffInPosition = positionToFace - currPosition
    if (diffInPosition == -1 or diffInPosition == -3):
        turnLeft(robot)
    elif (diffInPosition == 2 or diffInPosition == -2):
        robot.turn_in_place(cozmo.util.degrees(180)).wait_for_completed()
    elif (diffInPosition == 1 or diffInPosition ==3):
        turnRight(robot)

def movetoXY(robot,targetX,targetY,currentX,currentY):
    xnow = targetX - currentX
    ynow = targetY-currentY
    currOrientation = 0
    while(xnow != 0 or ynow != 0):
        robot.say_text("I need to go " +str(xnow) +"x and " + str(ynow) + "y").wait_for_completed()
        if(ynow >0 ):
            facePosition(currOrientation,0,robot)
            currOrientation = 0
            robot.drive_straight(cozmo.util.distance_mm(unit), cozmo.util.speed_mmps(150)).wait_for_completed()
            ynow = ynow -1
            
        elif(ynow < 0):
            facePosition(currOrientation,2,robot)
            currOrientation = 2
            robot.drive_straight(cozmo.util.distance_mm(unit), cozmo.util.speed_mmps(150)).wait_for_completed()
            ynow = ynow +1
        if (xnow > 0):
            facePosition(currOrientation,1,robot)
            currOrientation = 1
            robot.drive_straight(cozmo.util.distance_mm(unit), cozmo.util.speed_mmps(150)).wait_for_completed()
            xnow = xnow -1
        elif( xnow < 0):
            facePosition(currOrientation,3,robot)
            currOrientation = 3
            robot.drive_straight(cozmo.util.distance_mm(unit), cozmo.util.speed_mmps(150)).wait_for_completed()
            xnow = xnow +1
    
    robot.say_text("I am at positon " +str(targetX) +" " + str(targetY)).wait_for_completed()
    robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
    
    
    
def cozmo_program(robot: cozmo.robot.Robot):
	
	# Move lift down and tilt the head up
	robot.move_lift(-3)
	robot.set_head_angle(degrees(0)).wait_for_completed()
    
	movetoXY(robot,4,8,5,6)

cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)
