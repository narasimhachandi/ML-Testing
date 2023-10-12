import streamlit as st
import pickle

model = pickle.load(open('C:/Users/Amit/Desktop/ML-Heroku/Random_Forest.pkl','rb'))

def diabetes_prediction(data):
    prediction = model.predict([data])
    if prediction[0]==0:
        return 'The Person is Non-Diabetic!'
    else:
        return 'The Person is Diabetic!!!!'

def main():

    st.title('Diabetes Prediction Application')
    Pregnencies = st.number_input('Number Of Pregnencies',0,20)
    Glucose = st.number_input('Glucose',0,200 )
    BloodPressure = st.number_input('Blood Pressure', 0,150)
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.number_input('Insulin', 0,1000)
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.number_input('Age', 0,100)

    predict = ''

    if st.button('Predict'):
        predict = diabetes_prediction([Pregnencies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(predict)

if __name__ == '__main__':
    main()

