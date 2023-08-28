#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge # 导入opencv模块和协议模块

def image_callback(msg):
    image = bridge.imgmsg_to_cv2(msg,desired_encoding="bgr8")
    # 将ros_image通过蓝绿红8位色空间转换为OpenCV图像，结果返回给image，类参数bridge转换函数
    if(image.all() == None):
        print("Can't get your image, please check your code!")
    else :
        # print(image.size, image.shape) # 输出图像大小以及形状
        cv2.namedWindow("YourDearWindow",cv2.WINDOW_NORMAL) # 建立名为YourDearWindow的窗口 窗口类为 cv2内置的NORMAL窗口
        cv2.imshow("YourDearWindow",image[:,:,0]) # 在YourDearWindow中显示二维图像
        cv2.waitKey(3) # waitkey()延时显示图像，在imshow之后，没有waitkey（）函数图像将无法显示

rospy.init_node('follower',anonymous = True) # anonymous 同步选项 每公布一条消息就接受一个消息
bridge = cv_bridge.CvBridge() # 创建CvBridge对象
image_sub=rospy.Subscriber('/camera/rgb/image_raw',Image,image_callback)
# 以上括号内分别是 接受的node名称, 数据类型, 触发的回调函数
rospy.spin()
