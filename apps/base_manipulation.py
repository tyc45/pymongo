import streamlit as st
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb+srv://JordanT:Gg17Btz2tlhf@cluster0.hiike.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.carsDB
item = db.carDataset.find()

st.title("You like cars? I like cars!")