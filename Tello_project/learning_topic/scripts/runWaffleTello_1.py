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
        
        lower_green = numpy.array([40, 80, 60])
        upper_green = numpy.array([60, 200, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        
        ## 滤色结果
    	color_detected = cv2.bitwise_and(image, image, mask=mask)
    	## detected contours and all color points
    	gray = cv2.cvtColor(color_detected, cv2.COLOR_BGR2GRAY)

    	cnt = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    	cnt = imutils.grab_contours(cnt)

    	cnt = np.concatenate(cnt, axis=0) # 把所有检测出的轮廓拼接到一起，成为一个点集
    	cnts = cnt[:,0,:]# 变成2维

	if cnts.any():
		#轮廓拼接 ，最小矩形估计，意思是画出一个最小的矩形，能包括所有的点
		x, y, w, h = cv2.boundingRect(cnt)
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255 ,0),8)
		cv2.drawContours(img, cnt, -1, (155, 255, 0), 8)  # 画出轮廓
		hole_centre=(int(x+(w/2)),int(y+(h/2))) 
		cv2.circle(img ,hole_centre, 7, (0, 255, 0), -1)# 画出中心

		plt.imshow(img[:, :, ::-1])
		plt.show()
	
        
        
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

