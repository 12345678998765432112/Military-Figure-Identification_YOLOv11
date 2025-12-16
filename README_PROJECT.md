本项目为睿抗机器人智能侦查赛道兵人识别模块的实现代码

该模块基于Ultralytics YOLO框架进行二次开发，面向比赛场景下的车载摄像头拍摄的图像，实现对兵人目标的自动检测与识别。

项目重点不在于网络结构创新，而在于小数据集条件下训练策略与参数配置优化，在有限的训练样本规模下取得稳定且有效的检测结果。

数据来源：

由比赛提供的参赛智能车搭载的摄像头在真实比赛环境中采集图像数据。

数据类型：

RGB图像+对应目标检测标注

说明：本仓库未包含任何原始数据，仅提供数据组织方式与配置文件示例。

方法概述：

检测模型：YOLOv11（基于 Ultralytics 框架）

训练方式：监督式目标检测训练

推理方式：单帧图像

本项目未对网络结构进行修改，主要工作集中在：

训练超参数的合理配置

小样本条件下的收敛稳定性提升

实际比赛场景下的泛化表现优化

训练参数与经验：

在小规模数据集条件下，通过调整关键参数，有效提升了模型训练效果。相关参数配置与训练脚本已保留在本仓库中，欢迎后续参赛团队参考复现。



Soldier Recognition Module for RKEC Robot Intelligent Reconnaissance Track

This module is the implementation code for the soldier recognition module of the RKEC (RoboMaster \& KOB \& E-Creativity Challenge) Robot Intelligent Reconnaissance Track.

Developed based on the secondary development of the Ultralytics YOLO framework, it targets images captured by on-vehicle cameras in competition scenarios to achieve automatic detection and recognition of soldier targets.

The focus of this project is not on the innovation of network structure, but on the optimization of training strategies and parameter configuration under the condition of small datasets, to achieve stable and effective detection results with a limited scale of training samples.

Data Source

Image data collected by the cameras mounted on the participating intelligent vehicles provided by the competition in real competition environments.

Data Type

RGB images + corresponding target detection annotations

Note: This repository does not contain any raw data, only examples of data organization methods and configuration files are provided.

Method Overview

Detection Model: YOLOv11 (based on the Ultralytics framework)

Training Method: Supervised object detection training

Inference Method: Single-frame image

This project does not modify the network structure, and the main work focuses on:

Rational configuration of training hyperparameters

Improvement of convergence stability under small-sample conditions

Optimization of generalization performance in actual competition scenarios

Training Parameters and Experience

Under the condition of small-scale datasets, the model training effect is effectively improved by adjusting key parameters. Relevant parameter configurations and training scripts have been retained in this repository, and subsequent participating teams are welcome to refer to and reproduce them.



