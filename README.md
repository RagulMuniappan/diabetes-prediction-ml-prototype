## Diabetes Prediction ML Prototype

A prototype machine learning project for predicting diabetes based on basic medical attributes using a neural network model.

---

### About the Project

This project is an **early-stage prototype** for diabetes prediction using machine learning.  
It focuses on building, training, saving, and testing a simple neural network model using a sample diabetes dataset.

The goal of this prototype is to **validate the workflow** of data loading, model training, model persistence, and prediction — not to provide a production-ready medical system.

---

### Features

- Prototype diabetes prediction using ML  
- Neural network model built with Keras  
- Training using tabular medical data  
- Model saved and loaded using JSON and H5 formats  
- Basic prediction testing on sample data  

---

### Technologies Used

- Python  
- NumPy  
- TensorFlow / Keras  
- CSV-based dataset  

---

### Dataset Information

The dataset contains medical attributes commonly used for diabetes prediction:

- Pregnancies  
- Glucose level  
- Blood pressure  
- Skin thickness  
- Insulin  
- BMI  
- Diabetes pedigree function  
- Age  
- Outcome (0 = Non-diabetic, 1 = Diabetic)

> ⚠ This dataset is used **only for learning and experimentation**.

---

### How to Run

1. Train the model:
   ```bash
   python train.py

2. Test the trained model:
   ```bash
   python test.py

---

### Project Folder Structure

diabetes-prediction-ml-prototype/
│
├── train.py                        # Model training script
├── test.py                         # Model testing script
├── diabetes_dataset_samples.csv    # Sample dataset
├── model.json                      # Saved model architecture
├── model.h5                        # Saved model weights
├── README.md                       # Project documentation
└── requirements.txt                # Required libraries


---

### Working Principle

- Load diabetes dataset from CSV file  
- Split data into input features and output labels  
- Build a neural network with Dense layers  
- Train the model using binary cross-entropy loss  
- Save trained model architecture and weights  
- Reload the model for prediction testing  

---

### Applications (Prototype-Level)

- Learning machine learning workflows  
- Understanding neural networks on tabular data  
- Academic practice and experimentation  
- Base model for future healthcare ML projects  

---

### Limitations

- Prototype-level implementation  
- No train/test data split  
- No real-world validation  
- Not suitable for medical decision-making  

---

### Output

- Training accuracy displayed in console  
- Sample predictions printed for test data  

---

### License

This project is intended for educational purposes.
