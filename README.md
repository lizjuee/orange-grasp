# orange-grasp
通过Yolo识别出橙子的大小，然后用机械手抓取橙子

# develop environment：
Ubuntu 16.04 + ros kinetic &&  Ubuntu 18.04 + ros melodic

# sensor：

intel realsense d435

# hardware：

Ti5hand bionic arm
  
# setup:
```
$mkdir your_ws
     
$cd your_ws/
     
$mkdir src && cd src/
     
$git clone https://github.com/qq44642754a/orange-grasp.git
     
$cd ..
     
$catkin_make
```


# run bionic arm:

## 1.connect serial port to control unit:
```
$cd /dev && ls
```
#### ps： when saw ttyUSBx equipments，it means the bionic arm is connected
## 2.run "moveHand service" program:
```
$rosrun serial_test move_hand_service.py
```

## 3.launch speech program
```
$roslaunch robot_voice robot_voice.launch
```

## 3.launch YOLOV3
```
$roslaunch darknet_ros darknet_ros-orange.launch
```

## 4. launch node of get width of orange
```
$rosrun grasp_demo get_width
```

## 5. launch orange grasp
```
$rosrun grasp_demo orange_grasp.py
```




