#!usr/bin/env python
import rospy
from std_msgs.msg import String
from noob_pkg.msg import kratos
#from std_msgs.msg import String

def kratos_callback(msg):
	global message
	message=msg
	print message

pub = rospy.Publisher( 'kratos' , kratos , queue_size=10)

rospy.init_node( 'kratos' )
rate = rospy.Rate(10)
#data='wassup'

data=kratos()
data.sensor_name='barometer'
data.x=1
data.y=1
data.z=1
while not rospy.is_shutdown():
	pub.publish(data)
	rate.sleep()
