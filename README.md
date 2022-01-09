# orange-grasp
identify the width of orange use Yolo, then use bionic arm to grasp it

# develop environment：
Jetson Nano

# sensor：

intel realsense d435

# hardware：

Ti5hand bionic arm
  
# setup:
```
$mkdir your_ws
     
$cd your_ws/
     
$mkdir src && cd src/
     
$git clone git@github.com:lizjuee/orange-grasp.git
     
$cd ..
     
$catkin_make
```


# run bionic arm:

## 1.launchRealsense
```
$roslaunch realsense2_camera rs_rgbd.launch
```

## 2.launch YOLOV3
```
$cd test_ws/ && source devel/setup.bash
$roslaunch darknet_ros darknet_ros.launch
```

## 3. launch node of get columen of orange
```
$cd your_ws/ && source devel/setup.bash
$rosrun grasp_demo get_volumen
```

## 4. subscribe thr topic about volumen
```
$rostopic echo /volumen
```




