import streamlit as st
import pymongo

client = pymongo.MongoClient(**st.secrets["mongo"], connect=False)
# client = pymongo.MongoClient("mongodb+srv://JordanT:Gg17Btz2tlhf@cluster0.hiike.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cars_db = client.carsDB
cars = cars_db.get_collection("carDataset")
cars_display = st.container()

st.title("Who likes cars? I like cars!")

def car_to_string(car):
    return f"La {car['Make']} {car['Model']} {car['Vehicle Style']} de {car['Year']} a {car['Engine HP']} chevaux et {car['Engine Cylinders']} cylindres. Sa consommation sur autoroute est de {car['Highway L/100 km']} L au 100 km et de {car['City L/100 km']} L au 100km en ville."
    #TODO check and fix Fiat 500e

make_list = cars.distinct('Make')
with cars_display:
    make_box = st.sidebar.selectbox('Maker', make_list)
    # model_mask = cars['Model'] == st.sidebar.selectbox('Model', model_list)
    model_box = st.sidebar.selectbox('Model', cars.distinct('Model', {'Make': make_box}))

    display_result = [car_to_string(car) for car in cars.find({'Make': make_box, 'Model': model_box})]
    display_result
    # cars[make_mask]
# for item in list(cars.find()):
#     st.write(f"{item['make']}")
    if st.sidebar.checkbox('Add a new car'):
        maker_input = st.sidebar.text_input('Make')
        model_input = st.sidebar.text_input('Model')
        year_input = st.sidebar.text_input('Year')
        hp_input = st.sidebar.text_input('Engine HP')
        cylinders_input = st.sidebar.text_input('Engine Cylinders')
        if st.sidebar.button('Create New Car!'):
            new_car = {'Make':maker_input, 'Model':model_input, 'Year':year_input, 'Engine HP':hp_input, 'Engine Cylinders':cylinders_input}
            cars.insert_one(new_car)