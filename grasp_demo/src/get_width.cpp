#include "get_width.h"

ImageConverter::ImageConverter() : it_(nh_), xmin(0), xmax(0), ymin(0), ymax(0), get_obj(false)
{
	// topic sub:
	image_sub_depth = it_.subscribe("/camera/aligned_depth_to_color/image_raw",
									1, &ImageConverter::imageDepthCb, this);

	image_sub_color = it_.subscribe("/camera/color/image_raw", 1,
									&ImageConverter::imageColorCb, this);
	camera_info_sub_ =
		nh_.subscribe("/camera/aligned_depth_to_color/camera_info", 1,
					  &ImageConverter::cameraInfoCb, this);

	object_sub = nh_.subscribe("/darknet_ros/bounding_boxes", 1, &ImageConverter::YoloCb, this);
	width_pub = nh_.advertise<std_msgs::Float64>("width", 1);
}

ImageConverter::~ImageConverter()
{
}

void ImageConverter::cameraInfoCb(const sensor_msgs::CameraInfo &msg)
{
	camera_info = msg;
}

void ImageConverter::imageDepthCb(const sensor_msgs::ImageConstPtr &msg)
{
	cv_bridge::CvImagePtr cv_ptr;

	try
	{
		cv_ptr =
			cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_16UC1);
		depthImage = cv_ptr->image;
	}
	catch (cv_bridge::Exception &e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}
}

void ImageConverter::imageColorCb(const sensor_msgs::ImageConstPtr &msg)
{
	cv_bridge::CvImagePtr cv_ptr;
	try
	{
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
		colorImage = cv_ptr->image;
	}
	catch (cv_bridge::Exception &e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}
	if (get_obj)
	{
		real_z_min = 0.001 * depthImage.at<u_int16_t>((ymin + ymax) / 2, xmin);
		real_x_min =
			(xmin - camera_info.K.at(2)) / camera_info.K.at(0) * real_z_min;
		real_z_max = 0.001 * depthImage.at<u_int16_t>((ymin + ymax) / 2, xmax);
		real_x_max =
			(xmax - camera_info.K.at(2)) / camera_info.K.at(0) * real_z_max;
		width.data = real_x_max - real_x_min;
		width_pub.publish(width);
	}
	else
	{
		width.data = 0;
		width_pub.publish(width);
	}
	get_obj = false;
}

void ImageConverter::YoloCb(const darknet_ros_msgs::BoundingBoxes &yolo_temp)
{
	get_obj = true;
	xmin = yolo_temp.bounding_boxes[0].xmin;
	xmax = yolo_temp.bounding_boxes[0].xmax;
	ymin = yolo_temp.bounding_boxes[0].ymin;
	ymax = yolo_temp.bounding_boxes[0].ymax;
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "get_obj_width");
	ImageConverter imageconverter;
	ros::spin();
	return (0);
}
