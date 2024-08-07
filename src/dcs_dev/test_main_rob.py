from abb_rob.ros_client import DcsRosClient
from compas.geometry import Frame
import compas_rrc as rrc
import math
ROBOT_ON = True

# Velocities
MOVE_SPEED = 100
#MOVE_ZONE = rrc.Zone.Z20

# Robot configuration
ROBOT_TOOL = 't_A061_InlineMixer'
ROBOT_WORK_OBJECT = 'ob_A061_Wobjdata'

def rotate_vector(vector, angle):
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return [x, y, 0]

if __name__ == '__main__':

    # Create Ros Client
    rob_client = DcsRosClient()
    rob_client._init_ros_client()

    # Set Tool
    # rob_cleint._set_tool(ROBOT_TOOL)

    # Set Work Object
    rob_client._set_workobject(ROBOT_WORK_OBJECT)

    # Set Acceleration
    acc = 30  # Unit [%]
    ramp = 30 # Unit [%]
    rob_client._set_acceleration(acc, ramp)

    # Set Max Speed
    override = 100  # Unit [%]
    max_tcp = 1000  # Unit [mm/s]
    rob_client._set_max_speed(override, max_tcp)

    # ===========================================================================
    # Robot movement
    # ===========================================================================
    start = rob_client._print_text('Starting robotic movement.')

    # 1. Move robot to home position
    # startmsg = abb.send_and_wait(rrc.PrintText('PRINT START. Moving to home position'))
    # start = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, EXTERNAL_AXES, MAX_SPEED, rrc.Zone.FINE))
    # home_position = [22.39, 39.56, -18.24, -209.02, -31.92, 222.16]
    # rob_cleint._move_to_joints(home_position, 0, MOVE_SPEED, 20)

    # Get Robtarget
    # home_position = [-15.35, -26.44, 54.56, -152.76, -22.91, 143.16]
    home_position = [-19.75, 8.77, 38.17, -96.95, -3.53, 91.62]

    rob_client._move_to_joints(home_position, 0, MOVE_SPEED, 20)

    frame, external_axes = rob_client._get_robotarget()
    print(frame, external_axes)

    #adjust for the formwork

    frame.point[0] = -480
    frame.point[1] = -950
    frame.point[2] = 1350

    x = frame.point[0]
    y = frame.point[1]
    z = frame.point[2]

    xaxis = [-1, 0, 0]
    yaxis = [0, 1, 0]
    angle = math.radians(-45)


    frame_1 = Frame([x, y, z], xaxis, yaxis)
    frame_2 = Frame([x, y-800, z], rotate_vector(xaxis, angle), rotate_vector(yaxis, angle))
    frame_3 = Frame([x-850, y-800+20, z], rotate_vector(xaxis,angle ), rotate_vector(yaxis , angle))

    frames = [frame_1, frame_2, frame_3, frame_2, frame_1]
    frames_list = frames * 1000

    for frame in frames_list:
        rob_client._move_to_frame(frame, external_axes, MOVE_SPEED, rrc.Zone.Z20)
        rob_client._wait(1)


    # while True:
    #     for f in abb_frames:
    #         abb.send(rrc.MoveToRobtarget(f, EXTERNAL_AXES, MOVE_SPEED, MOVE_ZONE, rrc.Motion.LINEAR))

    # End of Code
    done = rob_client._print_text('Executing commands finished.')

    # Close client
    rob_client._close_ros_client()

    # 3. Move robot back to home position
    # endmsg = abb.send_and_wait(rrc.PrintText('PRINT END. Moving to home position'))
    # end = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, EXTERNAL_AXES, MAX_SPEED, rrc.Zone.FINE))
