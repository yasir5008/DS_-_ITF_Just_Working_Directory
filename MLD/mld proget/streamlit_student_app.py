import streamlit as st
import pickle
import pandas as pd



st.sidebar.title('Car Price Prediction')




html_temp = """
<div style="background-color:red;padding:15px">
<h1 style="color:yellow;text-align:center;">Streamlit ML Cloud App</h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

age = st.sidebar.selectbox("What is the age of your car?", (1,2,3,4,5,6,7,8,9))
hp = st.sidebar.slider("What is the hp of your car?",60,200,step=5)
km = st.sidebar.slider("What is the km of your car?",0,100000,step=500)
gear_type = st.sidebar.radio("What is the gear type of your car?",('Automatic','Manual','Semi-automatic'))
car_model = st.sidebar.radio("What is the model of your car?",['A1','A2','A3','Astra','Clio','Corsa','Espace','Insignia'])




model_name=st.selectbox('Select your ML model',('Xgboost','RanFor'))
if model_name=='Xgboost':
    model=pickle.load(open('xgb_model','rb'))
    st.success('You selected {} model'.format(model_name))
elif model_name=='RanFor':
    model=pickle.load(open('rf_model','rb'))
    st.success('You selected {} model'.format(model_name))

my_dict={

    'age': age,
    'hp':hp,
    'km':km,
    'model':car_model,
    'gearing_type':gear_type
    
}

df = pd.DataFrame.from_dict([my_dict])

columns=pickle.load(open('my_columns','rb'))

df=pd.get_dummies(df).reindex(columns=columns, fill_value=0)

st.header('The configuration of your car:')
st.table(df)


st.subheader('Press the predict button if congiguration is okay')
if st.button('Predict'):
    if model_name=='RanFor':
        scaler=pickle.load(open('my_scaler','rb'))
        df=scaler.transform(df)
        prediction=model.predict(df)
    else:
        prediction=model.predict(df)
    st.success('The estimation of your model is €{}'.format(int(prediction[0])))
    st.balloons()