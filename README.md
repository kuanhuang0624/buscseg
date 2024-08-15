# AI Model Notebooks for Breast Ultrasound Image Analysis

This repository contains several Jupyter Notebooks that demonstrate various tasks including segmentation, classification, and multi-task learning using different model backbones on the Breast Ultrasound Images Dataset.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Models and Notebooks](#models-and-notebooks)
- [Usage](#usage)
- [Citations](#citations)
- [License](#license)

## Introduction
This project utilizes several neural network architectures for the following tasks:
- **Segmentation**: Identifying the regions of interest in breast ultrasound images.
- **Classification**: Classifying the breast ultrasound images into categories.
- **Multi-task learning**: Performing both segmentation and classification simultaneously.

The models used in this project are:
- ResNet50
- VGG16
- SwinV2 Tiny
- VMamba

Our paper on this project has been accepted by the 2024 7th International Conference on Pattern Recognition and Artificial Intelligence. The paper will be available online after the conference.

## Dataset
The dataset used in this project is the Breast Ultrasound Images Dataset, which can be downloaded from [Kaggle](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset). After downloading, please place all images in the `Dataset_BUSI_with_GT` folder.

## Models and Notebooks
The project is divided into several notebooks, each targeting specific tasks with different model backbones:

### ResNet50
- **reset_segmentation.ipynb**: Segmentation using a U-Net with ResNet50 backbone.
- **resnet_multi.ipynb**: Multi-task classification and segmentation using ResNet50.
- **resnet_classification.ipynb**: Classification using ResNet50.

### VGG16
- **vgg_segmentation.ipynb**: Segmentation using a U-Net with VGG16 
backbone.
- **vgg_multi.ipynb**: Multi-task classification and segmentation using 
VGG16.
- **vgg_classification.ipynb**: Classification using VGG16.

### SwinV2 Tiny
- **swinv2tiny_segmentation.ipynb**: Segmentation using a U-Net with SwinV2 Tiny backbone.
- **swinv2tiny_multi.ipynb**: Multi-task classification and segmentation using SwinV2 Tiny.
- **swinv2tiny_classification.ipynb**: Classification using SwinV2 Tiny.

### VMamba
- **vmamba_segmentation.ipynb**: Segmentation using a U-Net with VMamba backbone.
- **vmamba_multi.ipynb**: Multi-task classification and segmentation using VMamba.
- **vmamba_classification.ipynb**: Classification using VMamba.

### ROC Curve
- **ROC curve.ipynb**: Drawing the ROC curve for all the classification models.

[//]: # (## Requirements)

[//]: # (To run these notebooks, you need to install the following dependencies:)

[//]: # ()
[//]: # (```bash)

[//]: # (pip install -r requirements.txt)

### Usage

1. Clone the repository:
```bash
git clone https://github.com/kuanhuang0624/buscseg.git
cd buscseg
```

2. Follow the [VMamba](https://github.com/MzeroMiko/VMamba) GitHub to install requirements.
3. Download the Breast Ultrasound Images Dataset from [Kaggle](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset) and place all images in the Dataset_BUSI_with_GT folder.
4. Run the desired notebook using Jupyter Notebook or Jupyter Lab.

### Citations

We utilized the code from the [VMamba GitHub Repository](https://github.com/MzeroMiko/VMamba) and are grateful for their excellent work.
If you use the VMamba model, please cite the following paper:

```bash
@misc{liu2024vmambavisualstatespace,
      title={VMamba: Visual State Space Model}, 
      author={Yue Liu and Yunjie Tian and Yuzhong Zhao and Hongtian Yu and Lingxi Xie and Yaowei Wang and Qixiang Ye and Yunfan Liu},
      year={2024},
      eprint={2401.10166},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2401.10166}, 
}
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.
