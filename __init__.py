from os import getenv

class RosVersionException(Exception):
    def __init__(self) -> None:
        Exception.__init__(self,
            "Unknow ROS version."
        )

ros_version = getenv('ROS_VERSION')

if ros_version == None:
    raise RosVersionException
elif ros_version == '1':
    from .ros1 import *
    del ros1
elif ros_version == '2':
    from .ros2 import *
    del ros2
else:
    raise RosVersionException

del ros_version
del getenv