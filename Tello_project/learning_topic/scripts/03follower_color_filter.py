#!/usr/bin/env python3
# 若使用的是python3，将第一行改成python3
import rospy ,cv2, cv_bridge , numpy
from sensor_msgs.msg import Image
# 导入模块
class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()  #创建CvBridge对象
        self.image_sub=rospy.Subscriber('/camera/rgb/image_raw',Image,self.image_callback)
        # 函数变量分别为：接受节点 、 接受消息类型、 回调函数
    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg)
        if(image.all()!=None):
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            # 进行消息-> rgb -> hsv格式变量 的两步转换
            lower_yellow = numpy.array([20,43,46])
            upper_yellow = numpy.array([90,255,255])
            # 建立蒙版参量 参量使用指针格式（inRange函数的要求）
            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
            masked = cv2.bitwise_and(image,image,mask=mask)
            # 使用蒙版进行二值化 bitwise
            cv2.namedWindow("showYellowOnly",cv2.WINDOW_NORMAL)
            cv2.imshow("showYellowOnly",mask)  #进行显示
            cv2.waitKey(3)
        
rospy.init_node('follower',anonymous = True)
follower = Follower()
rospy.spin()
