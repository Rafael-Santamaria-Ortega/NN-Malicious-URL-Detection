# Guide to Saving and Loading Neural Network Models in `.h5` Format

This guide walks you through saving and loading your trained neural network model using the `.h5` format, with an example integration into a Tkinter GUI.

---

## **1. Train Your Model**
Ensure you have a trained Keras/TensorFlow model in your Jupyter Notebook. Here's an example:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a sample model
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Example training data
import numpy as np
X_train = np.random.rand(100, 4)
y_train = np.random.randint(0, 2, size=(100,))

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=16)
```

---

## **2. Save the Model in `.h5` Format**
Once your model is trained, save it to a file:

```python
# Save the trained model
model.save('model.h5')
print("Model saved to 'model.h5'")
```

This saves:
- The model architecture.
- The weights.
- The optimizer configuration.

---

## **3. Load the Model in Your Tkinter Script**
In your Tkinter interface script (or another Python file), load the `.h5` file like this:

```python
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('model.h5')
print("Model loaded successfully!")

# Example usage of the model
import numpy as np

# Simulate preprocessing for prediction
example_input = np.array([[10, 2, 1, 1]])  # Adjust according to your preprocessing
prediction = model.predict(example_input)

print("Prediction:", prediction)
```

---

## **4. Integrate with Tkinter**
Connect the loaded model to your Tkinter interface. Replace the `predict_url` function with one that uses your loaded model:

#### Example Tkinter Integration:
```python
import tkinter as tk
from tkinter import messagebox
import numpy as np
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('model.h5')

# Example preprocessing function
def preprocess_url(url):
    return np.array([len(url), url.count('/'), url.count('.'), 'https' in url]).reshape(1, -1)

# Predict function
def predict_url():
    url = url_entry.get().strip()

    # Example URL preprocessing (adjust this function to your actual preprocessing logic)
    features = preprocess_url(url)
    
    # Predict using the loaded model
    prediction = model.predict(features)
    confidence = prediction[0][0]  # Adjust based on your model's output
    
    # Display results in the Tkinter GUI
    if confidence > 0.5:
        result_label.config(text=f"Malicious (Confidence: {confidence:.2%})", fg="red")
    else:
        result_label.config(text=f"Safe (Confidence: {confidence:.2%})", fg="green")

# Tkinter GUI
root = tk.Tk()
root.title("URL Maliciousness Checker")

# Input field
tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Predict button
predict_button = tk.Button(root, text="Check URL", command=predict_url)
predict_button.grid(row=0, column=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
```

---

## **5. Test the End-to-End Workflow**
- Ensure your `.h5` file is in the same directory as your script (or provide the full path).
- Run the script, enter a URL, and observe the prediction.

---

## **Tips**

1. **Use Consistent Preprocessing**: Ensure the preprocessing in your Tkinter script matches the steps used during training.
2. **Validate `.h5` Loading**: Always confirm the model loads correctly by printing its summary:
   ```python
   model.summary()
   ```
3. **Dependency Management**: Ensure TensorFlow is installed in the environment where the Tkinter script will run:
   ```bash
   pip install tensorflow
   ```

---
1. Use PyInstaller to Create a Standalone Executable
Install PyInstaller
Install PyInstaller in your Python environment:

bash
Copy
Edit
pip install pyinstaller
Package Your Application
Run the following command to create a standalone executable:

bash
Copy
Edit
pyinstaller --onefile --noconsole your_script.py
--onefile: Packages everything into a single executable file.
--noconsole: Prevents the console window from appearing (useful for GUI applications).
This will generate the executable in the dist/ directory.

2. Include the Model File (model.h5)
Since the .h5 file is not embedded in the executable, you need to ensure it is accessible. You can package it with your application or define its path dynamically.

Modify Your Script to Handle Relative Paths
Update your script to load the model file dynamically:

python
Copy
Edit
import os
import tensorflow as tf

# Get the directory where the script/executable is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the model from the same directory
model_path = os.path.join(base_dir, 'model.h5')
model = tf.keras.models.load_model(model_path)
Place the model.h5 file in the same directory as the executable.

3. Test the Executable
Navigate to the dist/ directory.
Place the model.h5 file alongside the executable.
Run the executable:
On Windows: Double-click the .exe file.
On macOS/Linux: Run the executable from the terminal if needed.
4. Distribute the Application
Package the executable and required files (like model.h5) into a ZIP or installer.

Create an Installer (Optional)
You can use tools like Inno Setup (Windows) or pkgbuild (macOS) to create an installer for a more professional distribution.

Advantages of This Approach
No Docker or Python Required: End-users only need to download and run the application.
Self-Contained: All dependencies are bundled.
Cross-Platform: With some adjustments, you can create executables for multiple operating systems.
