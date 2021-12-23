# mechanical-arm
通过机械手完成不同的物体抓取

<p align="center">
<img src="https://github.com/qq44642754a/mechanical-arm/blob/master/serial_test/media/run_service.png" width="400">
<img src="https://github.com/qq44642754a/mechanical-arm/blob/master/serial_test/media/service_call.png" width="400">

# serial_test
使用rosservice来控制机械手完成指定动作

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
     
$git clone https://github.com/qq44642754a/mechanical-arm.git
     
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

## 3.在终端中call /move_hand 服务:
```
$rosservice call /move_hand "type: 1"
```

### 本demo的service请求类型

|request| 含义|
|:----:| -------------|
|1 | Open|
|2 | Fist|
|3 | Index finger|
|4| Middle finger|
|5| Ring finger|
|6| Little finger|
|7| Ok|


