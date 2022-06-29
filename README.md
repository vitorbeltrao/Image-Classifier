# Computer Vision - Image Classifier

![Image Classifier App](https://github.com/vitorbeltrao/Pictures/blob/main/image_classifier.png?raw=true)

## Table of Contents

1. [Installation](#installation)
2. [Project Motivation, Development and Conclusion](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing and Authors](#licensingandauthors)

## Installation <a name="installation"></a>

To run this notebook, you must install the [opencv](https://opencv.org/) and [tensorflow](https://www.tensorflow.org/)

```
!pip install opencv-python
```
```
!pip install tensorflow
```

Taking this, there should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

## Project Motivation, Development and Conclusion<a name="motivation"></a>

**Project Motivation:**

This is one of the central problems of computer vision which, despite its simplicity, has a variety of practical applications. Image classification is the task of assigning an input image a label from a finite set of categories.

This classifier model that we are going to create will be very useful and important for doctors and radiologists, since it can help them in this task of diagnosing a patient with pneumonia or not, helping them to make much faster and more assertive decisions.

Technically speaking, we will approach the problem with supervised learning. We will use neural networks for the classification task. At the performance level of the algorithm, we will use the confusion matrix, accuracy, precision and recall.

***

**Development:**

In this project, we went through several necessary steps of a data science project, which were:

* We address the problem and analyze the big picture (described above in the project motivation).
* We collect data from [Kaggle](https://www.kaggle.com/).
* We did a quick exploratory data analysis.
* We pre-processed the data, which consisted of: split the dataset into training and testing, Normalization of images and Data Augmentation.
* We create our neural network using the tensorflow sequential API.
* We optimize the neural network hyperparameters and save the best parameters.
* Finally we evaluate the best model in the test set.

***

**Conclusion:**

For computer vision problems, using CNNs are more suitable and will certainly achieve better performances than ours here. Our model did not perform as well, but for a first iteration it was reasonable! We can leave as next steps, address this problem with CNNs and compare the respective performances of the two architectures. We can also, in addition to testing our own CNN, test various architectures of pre-trained models with transfer learning.

We ended up suffering a bit from the overfitting problem, where our model performs better on the training dataset than on the validation dataset, but that's to be expected as this is a complex problem. In the end, we ended up reaching an accuracy of 82% in the test set, which as we said, is not bad for a first iteration.

## File Descriptions <a name="files"></a>

We have the following files here:

* One Python file (app.py) which makes the entire structure of the web application. In addition, this code takes the file with the saved neural network parameters and makes the inferences.
* A notebook where the entire analysis of the respective problem was developed.
* A txt file where are all the libraries and their versions needed for the web application to work (requirements.txt).
* A txt file about the license to use the entire project developed (license.txt).
* For reasons of storage capacity, we will not make the data available here, but you can download it directly from [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

## Results<a name="results"></a>

The final web application for this job is available at the following link: https://vitorbeltrao-image-classifier-app-h51xdz.streamlitapp.com/

## Licensing and Authors <a name="licensingandauthors"></a>

Licensing: [MIT license](https://github.com/vitorbeltrao/Image-Classifier/blob/main/license.txt)

Authors: [Vitor Beltrão](https://www.linkedin.com/in/v%C3%ADtor-beltr%C3%A3o-56a912178/)
