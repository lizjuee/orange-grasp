cmake_minimum_required(VERSION 3.0.2)
project(robot_voice)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
        roscpp
        std_msgs
        )


catkin_package(
        #  INCLUDE_DIRS include
        #  LIBRARIES robot_voice
        #  CATKIN_DEPENDS roscpp std_msgs
        #  DEPENDS system_lib
)


include_directories(
        include
        ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/robot_voice.cpp
# )

add_executable(iat_publish
        src/iat_publish.cpp
        src/speech_recognizer.c
        src/linuxrec.c)
target_link_libraries(
        iat_publish
        ${catkin_LIBRARIES}
        libmsc.so -ldl -lpthread -lm -lrt -lasound
)

add_executable(tts_subscribe src/tts_subscribe.cpp)
target_link_libraries(
        tts_subscribe
        ${catkin_LIBRARIES}
        libmsc.so -ldl -pthread
)

add_executable(voice_assistant src/voice_assistant.cpp)
target_link_libraries(
        voice_assistant
        ${catkin_LIBRARIES}
        libmsc.so -ldl -pthread
)




