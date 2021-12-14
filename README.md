
# radiating-body-classifier

*This work is protected by the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.*  

## Introduction and Statement of Purpose

The primary objective I sought to meet through my original work was to establish a technical foundation for my independent study. While I have learned much about my field of study as it relates to my future interests and ambitions, my independent study thus far has not been as involved with direct computer programming as I might have sought. Thus, my specific goal was to develop a fully-functional product that would be similar to one an industry-grade professional might create. The original work also served to answer the specific questions over which I have pondered: what are the technologies, algorithms, and techniques I will employ through my study and in what manners will they have an impact?  

As a result, the mission of this project was to develop a classifier that, when given spectral and photometric data, can with high accuracy determine if a radiating object is a star, galaxy, or quasar. Such a project would reinforce my proficiency in using Python, TensorFlow, and other machine learning and data science tools. Furthermore, it serves as a point off of which to jump as I dive deep into the intersection of computer science and physics. This considered, it has served to set the foundations of my independent study for this year.

## Methodology

### Materials

* A Computer Equipped with the Following
  * Anaconda (Provides the Following Necessary Tools)
    * Python (Programming Language for Development)
    * TensorFlow (Python Library for Machine Learning)
      * TensorFlow Docs (Supplement to TensorFlow)
    * NumPy (Python Library for Storing Data)
    * pandas (Python Library for Storing Data)
    * Matplotlib (Python Library for Plotting Data)
  * A Python Integrated Development Environment (IDE) such as PyCharm (Software for Writing Code)
  * An Internet Browser such as Google Chrome (Application to Access Internet Facilities)
  * Internet Access (Access Necessary for Internet Facilities)

### Procedure

1. Identify the Problem Statement.
2. Access the “Sloan Digital Sky Survey DR14” dataset made available by Lennart Grosser on Kaggle.
   1. Dataset Link: [Sloan Digital Sky Survey DR14](https://www.kaggle.com/lucidlenn/sloan-digital-sky-survey)
   2. License Link: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
3. Modify the dataset as follows:
   1. Perform feature selection on the dataset. I removed the object IDs from the input values as I did not see them as pertinent to the model’s training.
   2. Organize the data as needed. I moved the output column of the data to be the first column to simplify the reading of the data.  
The revised dataset is the attached file “data.csv”.
4. Read through the following TensorFlow tutorials and become familiar with the concepts presented:
   1. [Basic Image Classification](https://www.tensorflow.org/tutorials/keras/classification)
   2. [Overfit and Underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)
   3. [Save and Load](https://www.tensorflow.org/tutorials/keras/save_and_load)
   4. [Tune Hyperparameters with Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner)
   5. [CSV](https://www.tensorflow.org/tutorials/load_data/csv)
   6. [Working with Preprocessing Layers](https://www.tensorflow.org/guide/keras/preprocessing_layers)
   7. [Classify Structured Data with Preprocessing Layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers)
5. Based on the content learned, write the model training file which does the following:
   1. Reads the data and splits it into training data and testing data
   2. Develops and trains a basic sequential network to classify the radiating objects  
This file is "train.py".
6. Upload all of the project files to GitHub.

## Utilization of Higher-Level Thinking Skills

My execution of this project necessitated my application of quite a few portable skills. For example, an apparent skill applied throughout the project was that of problem solving. Essentially inevitable in any study in computer science, issues were persistent in this project, which required my constant utilization of not only analytical skills but also evaluation and research skills and I explored possible solutions. These skills were employed to the extent I perceive that I spent more time problem solving than actually implementing what I had learned. This falls hand-in-hand with the critical skill of perseverance. As many issues arose, I had to push through them in order to complete this project. This skill will prove worthy in all endeavors, regardless of field of study or the problem being solved. Finally, this project tasked me with utilizing my eye for detail, as I was responsible for adhering to formatting conventions and writing readable code, among other things.

## Results

In the end, the greatest amount of accuracy I achieved before running into errors that seemed to cause further errors was that of roughly 80%. This was achieved with a simple sequential model (the structure of which is laid out in the “train.py” file) and without any major data augmentation, normalization, or precautions against overfitting and underfitting. The results were unexpected in two ways: firstly, I did not suspect that such a simple model that took relatively little effort would perform so well, and, secondly, I expected that the amount of effort required to increase this accuracy would be lower.

## Conclusions

Such results demonstrate two things: that managing library and tool installations can quickly spiral out of hand if not maintained properly and that basic machine learning technologies have quite massive capacities. Regarding the former, throughout this project, I realized just how much I have yet to learn regarding the inner workings of Python and its interaction with libraries that is quite different from that of other programming languages such as Java. On the latter matter, prior to conducting this project, I was unaware just how powerful machine learning can be in order to create systems in the sense that the developer need not do complex computations. I had formerly perceived that the application of machine learning technologies were only useful when the absolutely correct hyperparameters were identified. But this project has made clear that predefined machine learning and data science libraries can do a massive amount of computation to develop models that output quite accurate results, even absent much human intervention.

## Application

While the primary goal of this project was simply to establish a foundation for my work at the intersection of computer science and physics, my uploading of the work to the public can facilitate community progress as well. I hope that someone might be able to build off of my open-source work to create an even more accurate model and thus further scientific knowledge. However, the larger implications of this work may be somewhat limited as the specific format of input data is a criteria of its application that might mitigate its applicability to the larger public. For me, individually, on the other hand, this project has served as a wonderful lesson about how I should pursue further projects. Not only has it served to entice me regarding machine learning, I have now learned that dedication is necessary for any successful project and will thus pursue with the greatest commitment my independent study ahead.
