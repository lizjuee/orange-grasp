# grasp_demo
机械手抓取指定大小的橙子demo

demo流程：
1. 上位机语音提示 "Give me an big orange"
2. 此时人拿着橙子放到reaslese的识别范围内，并回复"This one ?"
3. 上位机回复到"Let me see", 此时通过算法开始识别橙子的大小
4. 若橙子太大或太小， 则回复到"its too big/small", 若不是橙子则回复"its not an orange"
5. 直到识别到符合要求的橙子，此时上位机会回复"OK, give me "
6. 此时人需要回复"Here you are", 并把橙子放到手抓上
7. 机器人回复"Ok, i am ready"，并开始抓橙子


# 开发环境：
Ubuntu 16.04 + ros kinetic &&  Ubuntu 18.04 + ros melodic

# 传感器：

深度摄像头

# 实验平台：

钛虎智能仿生手
  
# 运行机械手:

## 1.打开YOLOV3 识别橙子:
```
$roslaunch darknet_ros darkbet_ros-orange.launch
```
## 2.打开橙子大小识别程序:
```
$rosrun grasp_demo get_width
```
## 3.打开橙子抓取程序:
```
$rosrun grasp_demo orange_grasp.py 
```



