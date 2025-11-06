# spaceros_gz_demos

This is a ROS 2 package demonstrating how to use Gazebo Harmonic for robotic simulations in the Space ROS environment. This package is meant to serve as a baseline for how to create Gazebo worlds, set them up with the appropriate plugins for sending controls and receiving data, and bridge these topics to ROS. The simulated worlds use realistic gravity and include a submersible robot on Enceladus, the Perseverance rover and Ingenuity helicopter on Mars, a space capsule docking to the ISS, and two rovers on the Moon.

This package was made by David Dorf and Katie Hughes for the NASA Space ROS Sim Summer Sprint Challenge. The relevant PR in the Space ROS demos repository is [here](https://github.com/space-ros/demos/pull/33).


https://github.com/user-attachments/assets/b5a11627-e0f3-451b-af0c-b0e76b30fb04

Eeman Has made changes to the moon world and X2 models fro her AIAA paper on swarm robotics 

## Moon
Launch the moon demo with the following command:

```ros2 launch spaceros_gz_demos moon.launch.xml```

This world contains an X1 rover holding a truss that can be detached, an X2 rover, and a solar panel with one controllable joint on a lunar environment.
Images, camera info, laser scans, point clouds, and odometry topics are provided for each robot.
Additionally, each rover can be commanded as a differential drive system via a commanded base twist.
This world uses the Selenographic Coordinate System (SCS). 


<details>
<summary><b>Click here for information about the topics available in this demo.</b></summary>
<br>

| Topic Name | Topic Type | Description | 
| ---------- | ---------- | ----------- |
| ` /X1/camera_front/camera_info ` | ` sensor_msgs/msg/CameraInfo ` |  Camera info for X1's front camera  |
| ` /X1/camera_front/image ` | ` sensor_msgs/msg/Image ` |  Image on X1's front camera  |
| ` /X1/cmd_vel ` | ` geometry_msgs/msg/Twist ` |  Used to command the X1's base velocity  |
| ` /X1/front_laser/scan ` | ` sensor_msgs/msg/LaserScan ` |  Laser scan from the X1's camera  |
| ` /X1/front_laser/scan/points ` | ` sensor_msgs/msg/PointCloud2 ` |  Point cloud from the X1's camera  |
| ` /X1/imu_sensor/imu ` | ` sensor_msgs/msg/Imu ` |  IMU data from X1  |
| ` /X1/odometry ` | ` nav_msgs/msg/Odometry ` |  Base odometry topic from X1  |
| ` /X1/odometry_with_covariance ` | ` nav_msgs/msg/Odometry ` |  Odometry with covariance from X1  |
| ` /X1/truss/attach ` | ` std_msgs/msg/Empty ` |  Used to attach the truss on the back of the X1  |
| ` /X1/truss/detach ` | ` std_msgs/msg/Empty ` |  Used to detach the truss on the back of the X1  |
| ` /X2/camera_front/camera_info ` | ` sensor_msgs/msg/CameraInfo ` |  Camera info for X2's front camera  |
| ` /X2/camera_front/image ` | ` sensor_msgs/msg/Image ` |  Image on X2's front camera  |
| ` /X2/cmd_vel ` | ` geometry_msgs/msg/Twist ` |  Used to command the X2's base velocity  |
| ` /X2/front_laser/scan ` | ` sensor_msgs/msg/LaserScan ` |  Laser scan from the X2's camera  |
| ` /X2/front_laser/scan/points ` | ` sensor_msgs/msg/PointCloud2 ` |  Point cloud from the X2's camera  |
| ` /X2/imu_sensor/imu ` | ` sensor_msgs/msg/Imu ` |  IMU data from X2  |
| ` /X2/odometry ` | ` nav_msgs/msg/Odometry ` |  Base odometry topic from X2  |
| ` /X2/odometry_with_covariance ` | ` nav_msgs/msg/Odometry ` |  Odometry with covariance from the X2  |
| ` /solar_panel/joint ` | ` std_msgs/msg/Float64 ` |  Used to command the joint of the solar panel  |
| ` /tf ` | ` tf2_msgs/msg/TFMessage ` |  TF topic containing odometry from both the X1 and X2  |





### Getting Visualizations in Gazebo
If you would like to visualize camera image feeds or laser scans in Gazebo, you can add an Image Display or Visualize Lidar plugin to the Gazebo GUI from the top right menu. You can then select the topic you would like to visualize from the plugin's menu.
