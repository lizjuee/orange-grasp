#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Use rosservice to control the hand to perform specified actions


Author：Simple
"""
import serial
import threading
import rospy
from serial_test.srv import *


class MoveHand(threading.Thread):

    def __init__(self):
        try:
            threading.Thread.__init__(self)
            # 打开串口
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            # 判断是否能打开串口
            if not self.ser.isOpen():
                rospy.logerr("Serial Port open failed.\n")
            else:
                rospy.loginfo('Action list \n 1. Open \n 2. Fist \n 3. Index finger \n 4. Middle finger \n '
                              '5. Ring finger \n 6. Little finger \n 7. Ok \n')
        except Exception as e:
            rospy.logerr("Serial Port open failed: %s" % (e))

    def run(self):
        # 创建/move_hand的rosservice
        self.move_hand_service = rospy.Service(
            '/move_hand', moveHand, self.moveHandCallback)

    def moveHandCallback(self, req):
        try:
            # 分别接受到不同请求时
            if req.type == 1:
                open_cmd = 'FFFF03B1010000000000000000000000FFFF'
                open_cmd_bytes = open_cmd.decode('hex')
                self.ser.write(open_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 2:
                fist_cmd = 'FFFF03B1020000000000000000000000FFFF'
                fist_cmd_bytes = fist_cmd.decode('hex')
                self.ser.write(fist_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 3:
                index_cmd = 'FFFF03B1030000000000000000000000FFFF'
                index_cmd_bytes = index_cmd.decode('hex')
                self.ser.write(index_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 4:
                middle_cmd = 'FFFF03B1040000000000000000000000FFFF'
                middle_cmd_bytes = middle_cmd.decode('hex')
                self.ser.write(middle_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 5:
                ring_cmd = 'FFFF03B1050000000000000000000000FFFF'
                ring_cmd_bytes = ring_cmd.decode('hex')
                self.ser.write(ring_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 6:
                little_cmd = 'FFFF03B1060000000000000000000000FFFF'
                little_cmd_bytes = little_cmd.decode('hex')
                self.ser.write(little_cmd_bytes)
                return moveHandResponse(True)
            if req.type == 7:
                ok_cmd = 'FFFF03B1070000000000000000000000FFFF'
                ok_cmd_bytes = ok_cmd.decode('hex')
                self.ser.write(ok_cmd_bytes)
                return moveHandResponse(True)
        except Exception as e:
            rospy.logerr('cant move hand: %s' % (e))


def main():
    rospy.init_node('move_hand', anonymous=True)
    movehand = MoveHand()
    movehand.start()
    rospy.spin()


if __name__ == "__main__":
    main()
