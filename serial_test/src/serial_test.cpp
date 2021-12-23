#include <ros/ros.h>
#include <serial/serial.h> //ROS已经内置了的串口包
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>

serial::Serial ser; //声明串口对象

int main(int argc, char **argv)
{
    //初始化节点
    ros::init(argc, argv, "serial_example_node");
    //声明节点句柄
    ros::NodeHandle nh;

    unsigned char s_buffer[18];
    s_buffer[0] = 0xFF;
    s_buffer[1] = 0xFF;
    s_buffer[2] = 0x03;
    s_buffer[3] = 0xB1;
    s_buffer[4] = 0x01;
    s_buffer[5] = 0x00;
    s_buffer[6] = 0x00;
    s_buffer[7] = 0x00;
    s_buffer[8] = 0x00;
    s_buffer[9] = 0x00;
    s_buffer[10] = 0x00;
    s_buffer[11] = 0x00;
    s_buffer[12] = 0x00;
    s_buffer[13] = 0x00;
    s_buffer[14] = 0x00;
    s_buffer[15] = 0x00;
    s_buffer[16] = 0xFF;
    s_buffer[17] = 0xFF;

    try
    {
        //设置串口属性，并打开串口
        ser.setPort("/dev/ttyUSB0");
        ser.setBaudrate(115200);
        serial::Timeout to = serial::Timeout::simpleTimeout(1000);
        ser.setTimeout(to);
        ser.open();
    }
    catch (serial::IOException &e)
    {
        ROS_ERROR_STREAM("Unable to open port ");
        return -1;
    }

    //检测串口是否已经打开，并给出提示信息
    if (ser.isOpen())
    {
        ROS_INFO_STREAM("Serial Port initialized");
    }
    else
    {
        return -1;
    }

    ser.write(s_buffer, 18);
}
