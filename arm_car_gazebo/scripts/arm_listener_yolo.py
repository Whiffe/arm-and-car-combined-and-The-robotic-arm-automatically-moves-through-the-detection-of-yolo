#!/usr/bin/env python  
import rospy
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Float64

def callback(data):
    print data.bounding_boxes[0].Class

    if data.bounding_boxes[0].Class == 'person':
        pub = rospy.Publisher('/arm/joint2_position_controller/command', Float64, queue_size=10)
        pub.publish(1.0)
        print "arm jiont2 1.0"

def listener():
    rospy.init_node('topic_subscriber')

    sub = rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
