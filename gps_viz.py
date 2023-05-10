#!/usr/bin/env python3 


import matplotlib.pyplot as plt
import rospy
#import tf
from sensor_msgs.msg import NavSatFix
#from tf.transformations import quaternion_matrix
import numpy as np
from matplotlib.animation import FuncAnimation


class Visualiser:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ln, = plt.plot([], [], 'ro')
        self.x_data, self.y_data = [] , []

    def plot_init(self):
        self.ax.set_xlim(34.8150, 34.8156)
        self.ax.set_ylim(-82.3260, -82.3266)
        return self.ln

    # def getYaw(self, pose):
    #     latitude = (pose.orientation.x, pose.orientation.y, pose.orientation.z,
    #             pose.orientation.w)
    #     euler = tf.transformations.euler_from_quaternion(quaternion)
    #     yaw = euler[2] 
    #     return yaw   

    def gps_callback(self, msg):
        longitude = msg.longitude
        print(longitude)
        latitude = msg.latitude
        print(latitude)
        self.y_data.append(longitude)
        self.x_data.append(latitude)

    def update_plot(self, frame):
        self.ln.set_data(self.x_data, self.y_data)
        return self.ln


rospy.init_node('gps_visualizer_node')
vis = Visualiser()
sub = rospy.Subscriber('/piksi_multi_position/navsatfix_best_fix', NavSatFix, vis.gps_callback)

ani = FuncAnimation(vis.fig, vis.update_plot, init_func=vis.plot_init)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("LIVE GPS", fontdict = font1)
plt.xlabel("longitudes", fontdict = font2)
plt.ylabel("latitudes", fontdict = font2)
plt.show(block=True)
