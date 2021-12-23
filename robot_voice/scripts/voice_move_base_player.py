#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
import actionlib
import roslib;
import rospy
from std_msgs.msg import String

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

waypoints = [  # 导航的坐标点
    [(0.775753974915, -5.87806129456, 0.0), (0.0, 0.0, 0.999998745646, -0.00158388945662)],
    [(4.4747171402, -5.84645605087, 0.0), (0.0, 0.0, 0.999998746024, -0.00158365103834)]
]


def goal_pose(pose):  # <2>
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose


def callback(msg):
    print msg.data
    pub2 = rospy.Publisher('xfwords', String, queue_size=1)

    if msg.data.find('小车休眠') > -1:
        pub2.publish('我去休眠拉')
    if msg.data.find('小白小白') > -1:
        pub2.publish('我在')

    if msg.data.find('小车唤醒') > -1:
        rospy.sleep(0.5)
        pub2.publish('我在')


    if msg.data.find('房间的门') > -1:
        pose = waypoints[0]
        pub2.publish('出发去房间的门')
    elif msg.data.find('桌子前') > -1:
        pose = waypoints[1]
        pub2.publish('出发去桌子前面')
    else:
        return;

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  # <3>
    client.wait_for_server()

    print("goal:x=%f y=%f" % (pose[0][0], pose[0][1]))
    goal = goal_pose(pose)
    client.send_goal(goal)
    client.wait_for_result()
    if msg.data.find('房间的门') > -1:
        pub2.publish('到达房间的门')
    elif msg.data.find('桌子前') > -1:
        pub2.publish('到达桌子前面')



if __name__ == '__main__':
    rospy.init_node('message_publisher')

    rospy.sleep(1)

    sub = rospy.Subscriber('voice_words', String, callback)
    rospy.spin()
