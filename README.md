# Neural Network for Malicious URL Prediction

This TensorFlow-based neural network is designed to predict whether URLs collected from the wild are malicious or benign. Initially trained on Kaggle's Malicious URL Dataset, the project is currently being enhanced with features like learning rate decay, F1 score metrics, and additional data from URLhaus. While still under development, the project is approximately 85% complete and already offers a reliable framework for malicious URL detection.

## Project Motivation

The growing sophistication of phishing attacks and malicious websites, coupled with human susceptibility to social engineering, inspired this project. Traditional blacklist approaches often fail to detect newly created or modified malicious URLs, emphasizing the need for dynamic and intelligent detection methods. Without such advancements, the battle between attackers and defenders becomes an endless game of cat and mouse.

## Current Results

The model has demonstrated solid performance metrics on the test set, showing promising real-world applicability. It could serve as an essential component of a company's cybersecurity infrastructure, especially for real-time threat detection and prevention. As the saying goes:

"Prevention is better than cure."

While similar applications already exist, this project does not aim to reinvent the wheel. Instead, it seeks to showcase how machine learning can be leveraged to create adaptive and robust cybersecurity solutions.

## Implementation Details

The project is divided into five phases and is developed in a modular format using Jupyter Notebook. By breaking the neural network into individual components through custom functions, the code is easier to:

## Understand and debug.

Modify (e.g., changing activation functions, model architecture, or hyperparameters) without disrupting the entire neural network.

Reuse for other machine learning projects, such as phishing detection, malware classification, or anomaly detection.

This modular approach also enables calling the complete training and prediction pipeline in just a few lines of code, enhancing efficiency and reusability.

## Future Scope

This project continues to evolve as additional data and features are integrated. Its modular design ensures adaptability, making it a strong foundation for tackling similar challenges in cybersecurity.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
