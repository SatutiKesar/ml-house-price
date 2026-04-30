# House Price Prediction (ML Project)

This project predicts Bangalore house prices using Machine Learning.

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit

## Features
- ML model for price prediction
- FastAPI backend for serving predictions
- Streamlit UI for user interaction

## Project Structure
server/ → FastAPI backend  
ui/ → Streamlit frontend  
artifacts/ → model-related files  

## How to Run
# Run FastAPI backend:
uvicorn app:app --reload
# Run Streamlit frontend:
streamlit run app.py

### Backend
cd server  
uvicorn main:app --reload  

### Frontend
cd ui  
streamlit run app.py  

# Screenshot
<img width="1920" height="943" alt="UI" src="https://github.com/user-attachments/assets/b9cb35a3-d739-480d-b8fc-be3dcf64758b" />

## Dataset
https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data
