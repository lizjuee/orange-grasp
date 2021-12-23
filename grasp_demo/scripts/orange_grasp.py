#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import flags
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from serial_test.srv import *


class orangeGrasp():

    def __init__(self):
        self.voice_pub = rospy.Publisher('xfwords', String, queue_size=1)
        self.wackup_pub = rospy.Publisher('/voiceWakeup', String, queue_size=1)
        self.voice_sub = rospy.Subscriber(
            'voiceWords', String, self.voiceCallback)
        self.orange_width = 0.0
        self.grasp = False
        self.start_get_width = False
        self.start_give = False
        self.start_grasp = False
        self.prepare = False

    def voiceCallback(self, words):
        if words.data.find('This one') > -1:
            rospy.sleep(1)
            self.voice_pub.publish('Let me see')
            self.start_get_width = True

        if words.data.find('Here you are') > -1:
            rospy.sleep(1)
            self.voice_pub.publish('Ok, i am ready')
            self.start_grasp = True

    def widthCallback(self, msg):
        if (self.start_get_width):
            self.orange_width = msg.data

    def initGrasp(self):
        rospy.sleep(1)
        self.voice_pub .publish('give me an big orange')
        rospy.loginfo('please show me an big orange')
        rospy.sleep(1)

        while not self.start_give:
            self.wackup_pub.publish('wack up!')
            rospy.loginfo('say This one')
            rospy.sleep(10)
            print (self.start_get_width)
            if (self.start_get_width):
                self.start_give = True
            else:
                rospy.sleep(1)
                self.voice_pub.publish('sorry, i cant understand')
                rospy.sleep(3)

        while not self.grasp:
            rospy.loginfo('Get the width of orange')
            self.orange_sub = rospy.Subscriber(
                'width', Float64, self.widthCallback)
            rospy.sleep(3)
            self.orange_sub.unregister()
            print (self.orange_width)

            if self.orange_width == 0:
                rospy.sleep(1)
                self.voice_pub .publish('its not an orange')
                rospy.sleep(2)
                self.voice_pub .publish('give me another orange')
                rospy.sleep(2)

            if self.orange_width > 0.08:
                rospy.sleep(1)
                self.voice_pub .publish('its too big')
                rospy.sleep(2)
                self.voice_pub .publish('give me another orange')
                rospy.sleep(2)

            if self.orange_width < 0.06 and self.orange_width > 0:
                rospy.sleep(1)
                self.voice_pub .publish('its too small')
                rospy.sleep(2)
                self.voice_pub .publish('give me another orange')
                rospy.sleep(2)

            if self.orange_width > 0.06 and self.orange_width < 0.08:
                rospy.sleep(1)
                self.voice_pub .publish('OK, give me!')
                self.grasp = True

        while not self.prepare:
            self.wackup_pub.publish('wack up!')
            rospy.loginfo('say here you are')
            rospy.sleep(10)
            print (self.start_grasp)
            if (self.start_grasp):
                self.prepare = True
            else:
                rospy.sleep(1)
                self.voice_pub.publish('sorry, i cant understand')
                rospy.sleep(3)
        # grasp
        rospy.wait_for_service('/move_hand')
        hand_client = rospy.ServiceProxy('/move_hand', moveHand)
        r = moveHandRequest()
        r.type = 2
        hand_client.call(r)

def main():
    rospy.init_node('orange_grasp', anonymous=True)
    rospy.sleep(1)
    orangegrasp = orangeGrasp()
    orangegrasp.initGrasp()
    rospy.spin()


if __name__ == '__main__':
    main()
