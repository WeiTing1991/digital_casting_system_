from ros_client import DcsRosClient

rob_cleint = DcsRosClient()

#TODO: ### read all setting from json
#TODO: ### finish the setup with the DCS system.

# ==============================================================================
# Set parameters
# ==============================================================================

# Home position
# HOME_POSITION = [46.94, -5.68, 36.76, 141.63, 73.04, 38.53]
# Linear axis position

LINEAR_AXIS_X = 490
EXTERNAL_AXES = [LINEAR_AXIS_X]

ROBOT_ON = True

# Velocities
MOVE_SPEED = 100
MOVE_ZONE = rrc.Zone.Z20

# Robot configuration
ROBOT_TOOL = 'tool0'
ROBOT_WORK_OBJECT = 'ob_A061_Wobjdata'

#TODO:
# ==============================================================================
# Define geometry
# ==============================================================================

# define mid point of column
MID_PT = Point(2643, -370, 2230)

# define polygon details
POLYGON_POINTS = 16
RADIUS = 70

# create polygon and translate to mid point of column
polygon = Polygon.from_sides_and_radius_xy(POLYGON_POINTS, RADIUS)
T_frame_to_frame = Translation.from_frame_to_frame(Frame.worldXY(), Frame(MID_PT, Vector(1,0,0), Vector(0,1,0)))

# define tool axes
x_axis = Vector(-0.707, -0.000, -0.707)
y_axis = Vector(-0.000, 1.000, 0.000)

abb_frames = []

# transform polygon points and create frames
for p in polygon.points:
    p_trans = p.transformed(T_frame_to_frame)
    abb_frame = Frame(p_trans, x_axis, y_axis)
    abb_frames.append(abb_frame)

# End if robot is not on
if not ROBOT_ON:
    # End
    print('Finish code without moving robot')
    exit()

# ==============================================================================
# Main robotic control function
# ==============================================================================

#TODO:
if __name__ == '__main__':

    # SETTING OF THE ROBOT

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected')

    # Set Tool
    abb.send(rrc.SetTool(ROBOT_TOOL))

    # Set Work Object
    abb.send(rrc.SetWorkObject(ROBOT_WORK_OBJECT))

    # Set Acceleration
    acc = 30  # Unit [%]
    ramp = 30 # Unit [%]
    abb.send(rrc.SetAcceleration(acc, ramp))

    # Set Max Speed
    override = 100  # Unit [%]
    max_tcp = 1000  # Unit [mm/s]
    abb.send(rrc.SetMaxSpeed(override, max_tcp))

    # ===========================================================================
    # Robot movement
    # ===========================================================================
    startmsg = abb.send_and_wait(rrc.PrintText('Starting robotic movement.'))
    print("Starting robotic movement.")

    # 1. Move robot to home position
    # startmsg = abb.send_and_wait(rrc.PrintText('PRINT START. Moving to home position'))
    # start = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, EXTERNAL_AXES, MAX_SPEED, rrc.Zone.FINE))

    while True:
        for f in abb_frames:
            abb.send(rrc.MoveToRobtarget(f, EXTERNAL_AXES, MOVE_SPEED, MOVE_ZONE, rrc.Motion.LINEAR))

    # Print Text
    done = abb.send_and_wait(rrc.PrintText('Executing commands finished.'))
    print('Executing commands finished.')

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()

    # 3. Move robot back to home position
    # endmsg = abb.send_and_wait(rrc.PrintText('PRINT END. Moving to home position'))
    # end = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, EXTERNAL_AXES, MAX_SPEED, rrc.Zone.FINE))

