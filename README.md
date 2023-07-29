# CNN Image Classifier Project

## Overview

This project is an implementation of a Convolutional Neural Network (CNN) based image classifier. The primary objective is to classify images into two categories: cats and dogs. The classifier is built using Python and popular deep learning libraries like TensorFlow and Keras.

## Workflows

1. **Update config.yaml**: This step involves updating the configuration file to set various parameters for the CNN model and training process.

2. **Update secrets.yaml [Optional]**: In case there are any sensitive credentials or configurations needed, they can be stored securely in the secrets.yaml file.

3. **Update params.yaml**: This file contains the parameters required for training the CNN classifier, such as batch size, number of epochs, learning rate, etc.

4. **Update the entity**: In this step, the dataset entity is updated with the required data format and information.

5. **Update the configuration manager in src config**: The configuration manager in the source code should be updated to fetch the parameters from the config.yaml file.

6. **Update the components**: The different components of the CNN classifier, such as the model architecture, data pre-processing, and evaluation metrics, should be updated or modified if necessary.

7. **Update the pipeline**: This step involves updating the data processing and training pipeline, ensuring that it incorporates the latest changes and configurations.

8. **Update the main.py**: Finally, the main.py file, which is the entry point of the application, needs to be updated to reflect all the changes made in the previous steps.

## Dataset

The dataset for this project can be downloaded from the provided URL, which contains images of cats and dogs. (Kaggle)

## Model Performance

The CNN classifier achieved impressive performance on the cats and dogs dataset, with an accuracy of over 95% on the test set. The precision, recall, and F1-score for both classes were well-balanced, indicating the model's ability to generalize well to new data.

## How to Run the Project

To run the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yashguptatech/CNNClassifier
```

2. Create a conda environment after opening the repository:

```bash
conda create -n cnncls python=3.7 -y
conda activate cnncls
```

3. Install the requirements:

```bash
pip install -r requirements.txt
```

4. Finally, run the following command:

```bash
python app.py
```

5. Open up your local host and port to access the application.

## Tech Stack

The project utilizes the following technologies and libraries:

- Python
- TensorFlow
- Keras
- Convolutional Neural Network (CNN)
- Docker (for deployment on AWS)
- AWS (Amazon Web Services) for deployment using CI/CD with GitHub Actions

## AWS CI/CD Deployment with GitHub Actions

For deploying the CNN Classifier on AWS, the project provides a step-by-step guide to set up an IAM user with specific access (EC2 and ECR), create an ECR repository to store the Docker image, create an EC2 machine (Ubuntu), and configure it as a self-hosted runner for GitHub Actions.

Furthermore, it outlines how to set up GitHub secrets to securely store AWS access credentials and other necessary information for the CI/CD process.
