# -*- coding: utf-8 -*-


import pickle
import streamlit as st



load=open("mark.pkl","rb")
model=pickle.load(load)



def predict(Education, Income,Recency,Complain,Response,Purchases,spendings,Campaign,Age,Children,marital_Status):

# Preprocced
     
    if Education == "Basic":
        Education = 0

    elif Education == "Graduated":
        Education = 1

    elif Education == "PHD":
        Education = 2
#*****************************************#
    if marital_Status == "Married":
        marital_Status = 0

    elif marital_Status == "Single":
        marital_Status = 1


#*****************************************#

    if Campaign == "Accepted 0 Campaign":
        Campaign = 0

    elif Campaign == "Accepted 1 Campaign":
        Campaign = 1

    elif Campaign == "Accepted 2 Campaign":
        Campaign = 2

    elif Campaign == "Accepted 3 Campaign":
        Campaign = 3

    elif Campaign == "Accepted 4 Campaign":
        Campaign = 4



#*****************************************#
    if Response == "YES":
        Response = 1

    elif Response == "NO":
        Response = 0

#*****************************************#
    if Complain == "YES":
        Complain = 1

    elif Complain == "NO":
        Complain = 0


    prediction = model.predict(
        [[Education, Income, Recency,Complain,Response,Purchases,spendings,Campaign,Age,Children,marital_Status]])

    if prediction == 0:
        pred = 'cluster 0'

    elif prediction == 1:
        pred = 'cluster 1'

    elif prediction == 2:
        pred = 'cluster 2'
        
    elif prediction == 3:
         pred = 'cluster 3'
         
    return pred

def main():
    
    st.title("Customer Personality Analysis")
    
    Education = st.selectbox("Education",("Basic","Graduated","PHD"))

    marital_Status = st.radio("Marital_Status: ", ('Married', 'Single'))
    if (marital_Status == 'Single'):
        st.success("Single")
    elif (marital_Status == 'Married'):
        st.success("Married")

    Age = st.slider("Select Age", 0, 80)
    st.text('Selected: {}'.format(Age))

    Income= st.slider("Income",0,600000)

    Children = st.text_input("Children")

    #Teenhome = st.text_input("Teenhome")

    Purchases= st.slider("NUmber of Purchase Made", 0, 50)
    st.text('Selected: {}'.format(Purchases))

    spendings = st.slider("Select Monthly Expense", 0, 3000)
    st.text('Selected: {}'.format(spendings))

    Recency= st.slider("last Purchase", 0, 100)
    st.text('Selected: {}'.format(Recency))

    Campaign =st.selectbox("Campaign",("Accepted 0 Campaign","Accepted 1 Campaign","Accepted 2 Campaign","Accepted 3 Campaign","Accepted 4 Campaign"))

    Complain = st.selectbox("Complain",("YES","NO"))

    Response = st.selectbox("Accepted the offer in the last campaign",("YES","NO"))

    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = predict(Education, Income, Recency,Complain,Response,Purchases,spendings,Campaign,Age,Children,marital_Status)
        st.success('Above customer belongs to  {}'.format(result))


if __name__=='__main__':
    main()