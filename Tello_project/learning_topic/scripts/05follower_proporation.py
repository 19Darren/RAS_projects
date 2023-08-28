#!/usr/bin/env python3
# 若使用的是python3，将第一行改成python3
import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw',Image,self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size =1)
        self.twist =Twist()
        
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
        #cut the image to a blade
        M = cv2.moments(mask)
        #class MOMENTS
        if M['m00']>0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image,(cx,cy),20,(0,0,255),-1)
            err = cx-w/2
            self.twist.linear.x = 0.2 #(注：小车的速度不易设置太快)
            self.twist.angular.z = -float(err)/1000
            self.cmd_vel_pub.publish(self.twist)
        cv2.namedWindow("window2",cv2.WINDOW_NORMAL)
        cv2.imshow("window2",image)

        cv2.waitKey(3)
        
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()

