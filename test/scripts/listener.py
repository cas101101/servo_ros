#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import pi_servo_hat
import time

heading = 360

def init():
    # Initialize Constructor
    test = pi_servo_hat.PiServoHat()

    # Restart Servo Hat (in case Hat is frozen/locked)
    test.restart()

    # Test Run
    #########################################
    # Moves servo position to 0 degrees (1ms), Channel 0
    test.move_servo_position(0, 0)

    # Pause 1 sec
    time.sleep(3)

    # Moves servo position to 90 degrees (2ms), Channel 0
    test.move_servo_position(0, 90)


def callback(data):
    
    global heading
    
    if( data.data == 'left' ):
        x = 'heard left'
        print(x)
        # Turn left code
     
    if( data.data == 'right' ): 
        x = 'heard right'
        print(x)
        # Turn right code
        
    rospy.loginfo( 'heading %d', heading )
    
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('direction', String, callback) #subscribed to direction


    rospy.spin()

if __name__ == '__main__':
    init()
    listener()
