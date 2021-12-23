#!/usr/bin/env python
 
import rospy
from std_msgs.msg import Float64
 
 
rospy.init_node('width', anonymous=True)
pub = rospy.Publisher('width', Float64, queue_size=1)

rate = rospy.Rate(2)
width = Float64() 
width.data = 0.065
while not rospy.is_shutdown():
    pub.publish(width)
    rate.sleep()
