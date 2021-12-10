import streamlit as st
import pandas as pd
import pymongo

client = pymongo.MongoClient(**st.secrets["mongo"])

@st.cache(ttl=600)
def get_data():
    db = client.carsDB
    item = db.carDataset.find()
    item = list(item)  # make hashable for st.cache
    return item

cars = get_data()

st.title("You like cars? I like cars!")