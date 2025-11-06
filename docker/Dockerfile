FROM ros:humble

USER root

RUN apt-get update && apt-get install -y lsb-release gnupg curl

RUN curl -sSL https://packages.osrfoundation.org/gazebo.gpg | tee /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg > /dev/null
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | tee /usr/share/keyrings/ros-archive-keyring.gpg > /dev/null
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
    gz-harmonic \
    ros-humble-rviz2 \
    ros-humble-ros-gzharmonic \
    bash \
    bash-completion \
    build-essential \
    cmake \
    git \
    python-is-python3 \
    python3-pip \
    ripgrep

RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mv /ros_entrypoint.sh /old_entrypoint.sh
COPY entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh

RUN mkdir -p /home/spaceros-user/spaceros/ws/src/spaceros_gz_demos

WORKDIR /home/spaceros-user/spaceros/ws

USER spaceros-user

