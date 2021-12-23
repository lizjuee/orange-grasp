# orange-grasp
通过Yolo识别出橙子的大小，然后用机械手抓取橙子

# 开发环境：
Ubuntu 16.04 + ros kinetic &&  Ubuntu 18.04 + ros melodic

# 传感器：

深度摄像头

# 实验平台：

钛虎智能仿生手
  
#安装方法:
```
$mkdir your_ws
     
$cd your_ws/
     
$mkdir src && cd src/
     
$git clone https://github.com/qq44642754a/orange-grasp.git
     
$cd ..
     
$catkin_make
```


# 运行机械手:

## 1.将U盘插入工控机或者开发板上:
```
$cd /dev && ls
```
#### 注： 当看到有ttyUSBx开头的设备时，代表机械手的串口已连接
## 2.运行moveHand service程序:
```
$rosrun serial_test move_hand_service.py
```

## 3.启动语音程序
```
$roslaunch robot_voice robot_voice.launch
```

## 3.启动YOLOV3
```
$roslaunch darknet_ros darknet_ros-orange.launch
```

## 4. 启动获取橙子大小节点
```
$rosrun grasp_demo get_width
```

## 5. 启动橙子抓取
```
$rosrun grasp_demo orange_grasp.py
```




