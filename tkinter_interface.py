import tkinter as tk
from tkinter import messagebox
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# Load the trained model's .keras directory
model=tf.keras.models.load_model('neural_net.keras')

with open('tokenizer.pkl','rb') as file:
    tokenizer=pickle.load(file)

# Predict function
def predict_url():
    url=url_entry.get().strip()
    preprocessed_url=tokenizer.texts_to_matrix([url],mode='binary')
    # Predict using the loaded model
    prediction=model.predict(preprocessed_url,verbose=0)[0][0]
    # Maliciousness probability
    maliciousness_probability=round(prediction*100,2)
    # Display results in the Tkinter GUI
    if prediction<0.25:
        result_label.config(text=f"There is a {maliciousness_probability}% probability that {url} is malicious!",fg="green")
    elif prediction<0.50:
        result_label.config(text=f"There is a {maliciousness_probability}% probability that {url} is malicious!",fg="yellow")
    elif prediction<0.70:
        result_label.config(text=f"There is a {maliciousness_probability}% probability that {url} is malicious!",fg="orange")
    else:
        result_label.config(text=f"There is a {maliciousness_probability}% probability that {url} is malicious!",fg="red")
        
# Tkinter GUI code
root=tk.Tk()
root.title('URL Maliciousness Probability Predictor')

# Fix window size
root.geometry('800x200')
root.config(background='lightgray')

# Input field
tk.Label(root,text='Enter URL: ').grid(row=0,column=0,padx=10,pady=10)
url_entry=tk.Entry(root,width=70)
url_entry.grid(row=0,column=1,padx=10,pady=10)

# Predict button
predict_button=tk.Button(root,text='Check URL',command=predict_url)
predict_button.grid(row=0,column=2,padx=10,pady=10)

# Result label
result_label=tk.Label(root,text='',font=('Arial',14))
result_label.grid(row=1,column=0,columnspan=3,pady=10)
result_label.config(background='lightgray')

root.mainloop()
