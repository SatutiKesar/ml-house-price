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

### Backend
cd server  
uvicorn main:app --reload  

### Frontend
cd ui  
streamlit run app.py  

## Dataset
https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data
