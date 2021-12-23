# robot-voice
基于科大讯飞语音库搭建的语音识别和播报系统

# 开发环境：
Ubuntu 16.04 + ros kinetic &&  Ubuntu 18.04 + ros melodic

# 实验支持库：

科大讯飞语音库
  
#安装方法:

1. 在讯飞开放平台注册自己的账号，申请语音的SDK

2. 拷贝并安装库
```
$ sudo cp libmsc.so /usr/lib/

$ sudo apt install sox

$ sudo apt install libsox-fmt-all 
```
3. 将src/iat_publish 和 src/tts_subscribe 中的appid修改为自己的appid

# 指令示例:

- 语音识别示例
```
$ roscore

$ rosrun robot_voice iat_publish

$ rostopic pub /voiceWakeup std_msgs/String "data: 'any string'"
```
- 语音输出示例
```
$ roscore

$ rosrun robot_voice tts_subscribe

$ rostopic pub /voiceWords std_msgs/String "data: '你好，我是机器人'"
```
- 将语音输入与语音输出结合
```
$ roslaunch robot_voice robot_voice.launch
  
$ rostopic pub /voiceWakeup std_msgs/String "data: 'any string'"
```

