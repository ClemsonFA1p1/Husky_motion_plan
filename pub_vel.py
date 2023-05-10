#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import numpy as np

import numpy as np
#array = np.loadtxt('vel.csv', delimiter=',')
#array = np.loadtxt('skidpad.csv', delimiter=',')
#array = np.loadtxt('straightline.csv', delimiter=',')
#array = np.loadtxt('fishook.csv', delimiter=',')
#print(array.shape)
#print(array)

def publisher():
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel',Twist, queue_size=10)
    rospy.init_node('cmd_vel_array_publisher')
    rate = rospy.Rate(100)
    #cmd_vel_array = array[:,1]
    #ang_vel_array = array[:,2]
    #print(cmd_vel_array.shape)
    #print (len(cmd_vel_array))
    vel = Twist()
    time_0 = rospy.Time.now().to_sec()
    time_1 = rospy.Time.now().to_sec()
    time_diff = time_1-time_0
    i=1
    while not rospy.is_shutdown():
        if i < 6000:
            vel.linear.x = 1.0
            vel.angular.z = -0.00002*i
                #print("Publishing linear velocity:" + str(cmd_vel_array[int(i)]))
                #print("Publishing angular velocity:" + str(ang_vel_array[int(i)]))
        #time_1 = rospy.Time.now().to_sec()

        else:
            vel.linear.x = 0
            vel.angular.z = 0
        pub.publish(vel)
        i = i+1
        print(i)
        rate.sleep()
        #time_0 = rospy.Time.now().to_sec()
        #time_1 = rospy.Time.now().to_sec()

# def fishook_publisher():
#     pub = rospy.Publisher('/husky_velocity_controller/cmd_vel',Twist, queue_size=10)
#     rospy.init_node('cmd_vel_array_publisher')
#     rate = rospy.Rate(100)
#     cmd_vel_array = array[:,1]
#     ang_vel_array = array[:,2]
#     vel = Twist()
#     time_0 = rospy.Time.now().to_sec()
#     time_1 = rospy.Time.now().to_sec()
#     vel.angular.z = 0.1
#     while not rospy.is_shutdown():
#         for i in range(len(cmd_vel_array)):
#             while time_1 - time_0 < 1.8:
#                 vel.linear.x = cmd_vel_array[i]
#                 if (time_1 - time_0)%0.1 == 0.0:
#                     vel.angular.z +=0.1
#                 print("Publishing linear velocity:" + str(cmd_vel_array[int(i)]))
#                 print("Publishing angular velocity:" + str(ang_vel_array[int(i)]))
#                 pub.publish(vel)
#                 time_1 = rospy.Time.now().to_sec()
#                 #i = i+1
#                 rate.sleep()
#             time_0 = rospy.Time.now().to_sec()
#             time_1 = rospy.Time.now().to_sec()
#             vel.angular.z = 0.1            


if __name__ == '__main__':
    publisher()