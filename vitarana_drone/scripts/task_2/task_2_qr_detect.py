#!/usr/bin/env python3



from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import rospy
from pyzbar.pyzbar import decode
from std_msgs.msg import String


class image_proc():

    # Initialise everything
    def __init__(self):
        rospy.init_node('qr_scanner')  # Initialise rosnode
        # Subscribing to the camera topic
        self.image_sub = rospy.Subscriber("/edrone/camera/image_raw", Image, self.qr_decode)
        self.img = np.empty([])
        # This will contain your image frame from camera
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('qrValue',String,queue_size=1)
        self.rate = rospy.Rate(10)
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        rospy.spin()

    def qr_decode(self, data):
        rospy.loginfo("Bupesh, Starting QR scanner node")
        # Converting the image to OpenCV standard image
        self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")


        # Decoding Qrcode and publishing value
        data = ''
        decoded_data = decode(self.img)
        cv2.imshow("camera paarunga", self.img)
        cv2.waitKey(1)
        if decoded_data:
            for obj in decoded_data:
                data = obj.data
                self.pub.publish(data)


'''
# Callback function of camera topic
    def image_callback(self, data):
        try:

        except CvBridgeError as e:
            print(e)
            return'''


if __name__ == '__main__':
    image_proc_obj = image_proc()
    rospy.loginfo("Bupesh, QR scanner done ")
    #qr_decode()
    

    '''try:
        
        image_proc_obj = image_proc()
    except rospy.ROSInterruptException:
        pass'''