#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import time
# hello
# hey there

def talker():
  
    # Publish to the direction topic 
    pub = rospy.Publisher('direction', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    pub.publish( 'start' )

    while not rospy.is_shutdown():

        # detect button presses on the two pins
        new_direction = input("New direction: ")
        
        if new_direction == 'left':
            
            rospy.loginfo( 'left' )
            
            # simple button debounce
            pub.publish( 'left' )
            
        if new_direction == 'right':
            
            rospy.loginfo( 'right' )
            pub.publish( 'right' )
        
        rate.sleep();
                

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
