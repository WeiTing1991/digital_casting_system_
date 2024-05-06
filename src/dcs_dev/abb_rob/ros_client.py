import compas_rrc as rrc

class DcsRosClient():

    def __init__ (self):
        self._ros = None
        self._abb = None


    def _init_ros_client(self):
        self.ros = rrc.RosClient()
        self.ros.run()
        self.abb = rrc.AbbClient(self.ros, "/rob1")

        print ("ROS client initialized")
        self.abb.send(rrc.PrintText("Connected to ROS"))
        self.abb.send(rrc.PrintText("Wellcome to digital casting sytsem"))


    def _close_ros_client(self):
        self.ros.close()
        self.ros.terminate()

        self.abb.send(rrc.PrintText("disconected to ROS"))
        print ('ROS client disconnected')
