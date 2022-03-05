
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LinearRegression


with st.echo():
    df = pd.read_csv("Advertising.csv")
    X= df.drop("sales", axis=1)
    y= df["sales"]
    x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(x_train, y_train)
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(x_test, y_test)
    st.write(result)
    pred = model.predict([[100,200,300]])
    st.write(pred)
    
    
st.table(df.head())
a = float(st.sidebar.number_input("TV:",value=230.1, step=10.1))
b = float(st.sidebar.number_input("radio:",value=37.8, step=10.1))
c = float(st.sidebar.number_input("newspaper:",value=69.2, step=10.1))
if st.button("Predict"): 
    pred = model.predict([[a,b,c]])
    st.write(pred)