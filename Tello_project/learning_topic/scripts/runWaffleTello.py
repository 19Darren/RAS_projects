#!/usr/bin/env python3

import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw',Image,self.image_callback)

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
        lower_yellow = numpy.array([20,43,46])
        upper_yellow = numpy.array([90,255,255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        h,w,d= image.shape
        top = 5*h/6
        bot = top + 20
        mask[int(0):int(top),:] = 0
        mask[int(bot):int(h),:] = 0
        mask[:,:w//5] = 0
        mask[:,4*w//5:] = 0
        #cut the image to a blade
        M = cv2.moments(mask)
        #class MOMENTS
        if M['m00']>0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image,(cx,cy),20,(0,0,255),-1)
            err = cx-w/2
            self.waffle_twist.linear.x = 0.1 #(Waffle Speed)
            self.waffle_twist.angular.z = -float(err)*2/w*1.57
            self.cmd_vel_pub.publish(self.waffle_twist)
            self.tello_twist.linear.x = 0.025 #(Tello Speed)
            self.tello_twist.angular.z = -float(err)/w*1.57/2
            self.tello_cmd_vel_pub.publish(self.tello_twist)        
            cv2.namedWindow("YelloLineTracking",cv2.WINDOW_NORMAL)
        cv2.imshow("YelloLineTracking",image)

        cv2.waitKey(1)
        
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()

