import pandas as pd
import pickle
import streamlit as st

model = pickle.load(open('unburn_model2.pkl', 'rb'))

st.title('Prediksi Unburn Carbon')


nilai_kalor = st.number_input('Input nilai kalor (kcal/kg) ')
co = st.number_input('Input Co (%) ')
co2 = st.number_input('Input CO2 (%) ')
out_generator = st.number_input('Input Output generator (MW) ')
sfc = st.number_input('Input SFC (kg/kWh) ')
eco_gas_out_temp = st.number_input('Eco gas Outlet Temperatur (C) ')
pa_flow = st.number_input('Input PA Flow (T/H) ')
o2 = st.number_input('Input O2 Outlet APH  (%) ')
fuel_temp = st.number_input('Input fuel temperature (C) ')
sa_flow = st.number_input('Secondary Air (T/H) ')
carbon = st.number_input('Input carbon (%) ')
hydrogen = st.number_input('Input Hydrogen (%) ')
nitrogen = st.number_input('Input nitrogen (%) ')
sulfur = st.number_input('Input Sulfur (%) ')
ash = st.number_input('Input ash (%) ')
total_moisture = st.number_input('Input total_moisture ( %) ')
oxygen = st.number_input('Input Oxygen batubara (%) ')
surface_moisture = st.number_input('input surface_moisturer (%) ')
inherent_moisture = st.number_input('Input inherent_moisture (%) ')


predict = ''

if st.button('Estimasi hasil Unburn Carbon'):
    predict = model.predict(
        [[nilai_kalor, co, co2, out_generator, sfc, eco_gas_out_temp, pa_flow, o2, fuel_temp, sa_flow, carbon, hydrogen, nitrogen, sulfur, ash, total_moisture, oxygen, surface_moisture, inherent_moisture]]
    )
    # Merubah dalam format DataFrame
    predict = pd.DataFrame(predict, columns=['unburn_carbon'])
    st.write ('Besar hasil Unburn Carbon =', predict, '%')
