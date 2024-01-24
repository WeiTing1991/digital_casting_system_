# Container for running ros2

# Base ROS2 image
ARG ROS_DISTRO=humble

FROM osrf/ros:${ROS_DISTRO}-desktop as Base
LABEL key="weitingchen"

SHELL [ "/bin/bash", "-c" ]

# Intall basic package
RUN apt-get update && apt-get install -y python3-pip

ENV DCS_BUILD_ROS = 1

RUN mkdir -p /dcs_ws/src
WORKDIR /dcs_ws/src

# Build the base Colcon workspace, installing dependencies first.
WORKDIR /dcs_ws
RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
 && apt-get update -y \
 && rosdep install --from-paths src --ignore-src --rosdistro ${ROS_DISTRO} -y \
 && colcon build --symlink-install

RUN echo "source /opt/ros/${ROS_DISTRO}/setup.zsh" >> /root/.bashrc
