#!/usr/bin/env python3
# 若使用的是python3，将第一行改成python3
import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import Image

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber(
                    '/camera/rgb/image_raw',
                    Image,
                    self.image_callback )
    
    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,                   
                            desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_yellow = numpy.array([20,43,46])
        upper_yellow = numpy.array([90,255,255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        # 同Exp4-2相同 不多做介绍
        h,w,d= image.shape
        top = 3*h/4
        bot = top + 20
    # 在图像的下3/4处进行切片 注意：image纵向向下为x正向 横向向右为y正向
        mask[int(0):int(top),:] = 0
        mask[int(bot):int(h),:] = 0
        M = cv2.moments(mask)
        #moments（）： Opencv中用于计算图像中心的函数类 参见Opencv官网
        if M['m00']>0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image,(cx,cy),20,(0,0,255),-1)
        # 对切片之后的图像计算中心，并标记小圆圈
        cv2.namedWindow("showImage",cv2.WINDOW_NORMAL)
        cv2.imshow("showImage",image)
        cv2.namedWindow("findLine",cv2.WINDOW_NORMAL)
        cv2.imshow("findLine",mask)
        cv2.waitKey(3)
        
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()

