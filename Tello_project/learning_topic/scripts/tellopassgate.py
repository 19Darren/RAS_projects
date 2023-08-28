#!/usr/bin/env python3

import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import imutils
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/drone1/image_raw',Image,self.image_callback)

        # self.image_sub = rospy.Subscriber('/drone1/image_raw',Image,self.tello_image_callback)

        self.cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size =1)

        self.tello_cmd_vel_pub = rospy.Publisher('/drone1/cmd_vel',Twist,queue_size =1)
		
        self.waffle_twist = Twist()
        self.tello_twist = Twist()
		
    def tello_image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        cv2.namedWindow("TelloImage",cv2.WINDOW_NORMAL)
        cv2.imshow("TelloImage",image)
        cv2.waitKey(1)
        # pass

    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_green = numpy.array([40, 80, 60])
        upper_green = numpy.array([60, 200, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        color_detected = cv2.bitwise_and(image, image, mask=mask)
        gray = cv2.cvtColor(color_detected, cv2.COLOR_BGR2GRAY)
        cnt = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt = imutils.grab_contours(cnt)
        cnt = numpy.concatenate(cnt, axis=0) # get the point set
        cnts = cnt[:,0,:]
        if cnts.any(): #  draw the smallest rectangle which could contain all the points
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255 ,0),8)
            cv2.drawContours(image, cnt, -1, (155, 255, 0), 8)  # Draw the outline
            hole_centre=(int(x+(w/2)),int(y+(h/2))) 
            cv2.circle(image ,hole_centre, 20,(0,0,255), -1)   # Draw the center
            area = w * h
            error = x - 500
            if area > 500:
                self.tello_twist.linear.x = 0.2 #(Tello Speed)
                self.tello_twist.angular.z = - error / 1500  
                self.tello_cmd_vel_pub.publish(self.tello_twist)
                self.waffle_twist.linear.x = 0.1 #(Waffle Speed)
                self.waffle_twist.angular.z = -float(error)*2/w*1.57
                self.cmd_vel_pub.publish(self.waffle_twist)
            else:
                self.tello_twist.linear.x = -0.05 #(Tello Speed)
                self.tello_twist.angular.z = - error / 700
                self.tello_cmd_vel_pub.publish(self.tello_twist)
            
             
            # plt.imshow(img[:, :, ::-1])
            # plt.show()
            cv2.namedWindow("GreenGatePass",cv2.WINDOW_NORMAL)
        cv2.imshow("GreenGatePass",image)        
        cv2.waitKey(1)
        
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()

