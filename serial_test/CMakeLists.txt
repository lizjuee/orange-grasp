cmake_minimum_required(VERSION 2.8.3)
project(serial_test)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  serial
  std_msgs
  message_generation
)

add_service_files(
  FILES
  moveHand.srv
)

generate_messages(
        DEPENDENCIES std_msgs
)


catkin_package(
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#add_executable(serial_test src/serial_test.cpp)
#target_link_libraries(serial_test ${catkin_LIBRARIES})
#add_dependencies(serial_test ${PROJECT_NAME}_generate_messages_cpp)
