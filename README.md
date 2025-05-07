
# Spam Message Classifier Web App

This project is a **Spam Message Classifier** built using Python and Streamlit. The web app predicts whether a message is spam or ham (not spam) using a machine learning model.

## Technologies Used
- Python
- Streamlit
- scikit-learn
- Pickle (for saving the trained model)

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/dishapawarkhausi/spam-message-classifier.git
cd spam-message-classifier
```

### 2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app:
```bash
streamlit run app.py
```

### 5. Open the app:
Once the app runs, a local URL will be provided, typically `http://localhost:8501/`.

## How It Works
1. The user inputs a message in the text area.
2. The message is vectorized using the trained TF-IDF vectorizer.
3. The model predicts whether the message is **spam** or **ham**.
4. The prediction confidence (probability) is shown along with the result.

## Model
The machine learning model used in this app is trained on a spam message dataset and saved as a `.pkl` file. The model uses a TF-IDF vectorizer to process text data and a classifier (like Logistic Regression) for predictions.

## Future Improvements
- Improve UI/UX
- Use advanced machine learning models (e.g., deep learning)
- Add user feedback collection for model improvement

## 🚀 Live Demo

Check out the live Streamlit app here:  
👉 [Spam Classifier App](https://spam-message-classifierapp.streamlit.app/)
