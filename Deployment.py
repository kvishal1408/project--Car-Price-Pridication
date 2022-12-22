# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:51:44 2022

@author: dell
"""

# Necessary Libraries
import pickle
import streamlit as st
import numpy as np
import pandas as pd
import sklearn

st.title('CAR  PRICE  PREDICATOR')
data_1= pickle.load(open('data_1.pkl','rb'))
car_model = pickle.load(open('car24LR.pkl','rb'))
#sidebar



   
def predict(Name, Model, Transmission, KM, Owner, Fuel_type,
            Registration, EMI, Year, Brand, states, Age):
   
   prediction = car_model.predict(pd.DataFrame([[Name, Model, Transmission, KM, Owner, Fuel_type,
   Registration, EMI, Year, Brand, states, Age]],columns=['Name','Model','Transmission','KM','Owner','Fuel_type','Registration','EMI','Year','Brand','State','Age']))
   return prediction

    
col1,col2 = st.columns(2)
with col1:
   Brand=st.selectbox("Select the Brand Name",data_1['Brand'].unique())
   Name=st.selectbox("Select the Car Name",data_1["Name"].unique())
   Model=st.selectbox("Select the Car Model",data_1["Model"].unique())
   Transmission=st.selectbox("Select the Transmission Type",data_1["Transmission"].unique())
   KM=st.number_input("Enter KM")
   Owner=st.number_input("Enter Owner Number")
with col2:   
    Fuel_type=st.selectbox("Select the Fuel_type",data_1["Fuel_type"].unique())
    Registration=st.selectbox("Enter Registration Location",data_1['Registration'].unique())
    EMI=st.number_input("Enter EMI")
    Year=st.number_input("Enter the Year")
    states=st.selectbox("Enter the state",data_1['states'].unique())
    Age=st.number_input("Enter the Age")

   
if st.button("Predict"):
     price = predict(Name, Model, Transmission, KM, Owner, Fuel_type,
     Registration, EMI, Year, Brand, states, Age)
     st.success(f'The Predicted Price of car is  ₹  {price[0]:.2f}')
       
      