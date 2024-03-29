#!/usr/bin/python3
# coding=utf-8

import sys
import rospy
import numpy as np
import os
from sensor_msgs.msg import Image
from nn_vs.msg import Image_Msg
import cv2

class image_listenner:
    def __init__(self): 
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image_Msg, self.image_sub_callback)
        self.img = np.zeros((480, 640, 3), dtype=np.uint8)  # 初始图像

    def image_sub_callback(self, data):
        ''' callback of image_sub '''
        image = np.ndarray(shape=(data.height, data.width, data.channels), dtype=np.uint8, buffer=data.data) # 将自定义图像消息转化为图像
        self.img[:,:,0],self.img[:,:,1],self.img[:,:,2] = image[:,:,2],image[:,:,1],image[:,:,0] # 将rgb 转化为opencv的bgr顺序
        cv2.imshow("Image ", self.img)
        cv2.waitKey(10)

if __name__ == '__main__':
	rospy.init_node('image_listenner', anonymous=True)
	image_listenning = image_listenner()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()






