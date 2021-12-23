cmake_minimum_required(VERSION 2.8.3)
project(grasp_demo)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS roscpp std_msgs sensor_msgs message_filters cv_bridge image_transport 
compressed_image_transport compressed_depth_image_transport darknet_ros_msgs)

## System dependencies are found with CMake's conventions
find_package(OpenCV REQUIRED)

generate_messages(
        DEPENDENCIES actionlib_msgs std_msgs
)

catkin_package(

)


include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(get_width src/get_width.cpp)
target_link_libraries(get_width
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
)







