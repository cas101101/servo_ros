#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO
import time
# hello

def talker():
  
    # Publish to the direction topic 
    pub = rospy.Publisher('direction', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    pub.publish( 'start' )

    # Set up the GPIO pins
    
    left_pin = 18
    right_pin = 24
    debounce_sleep = 0.2
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(right_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)


    while not rospy.is_shutdown():

        # detect button presses on the two pins
        
        left = GPIO.input(left_pin)
        right = GPIO.input(right_pin)
        
        if left == False:
            
            rospy.loginfo( 'left' )
            
            # simple button debounce
            time.sleep( debounce_sleep )
            pub.publish( 'left' )
            
        if right == False:
            
            rospy.loginfo( 'right' )
            time.sleep( debounce_sleep )
            pub.publish( 'right' )
        
        rate.sleep();
                

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
