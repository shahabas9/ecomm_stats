import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("This is the ecomm app which im creating")
    st.sidebar.title("Here you can upload the files")

    upload_file =st.sidebar.file_uploader("you can upload files here",type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith(".csv"):
                data=pd.read_csv(upload_file)
            else:
                data=pd.read_excel(upload_file)
            if 'Stay_In_Current_City_Years' in data.columns:
                data['Stay_In_Current_City_Years'] = data['Stay_In_Current_City_Years'].str.replace('+', '').astype(int)
            st.sidebar.success("you have succesffully uploaded the file")
            st.subheader("im going to showcase the data here")
            st.dataframe(data.head(5))

            st.subheader("let see some more details of the data here")
            st.write("you can see shape of the data",data.shape)
            st.write("the column name inside the data is ", data.columns)
            st.write("missing values in the columns",data.isnull().sum())

            st.subheader("i will show you bit of stats")
            st.write("the description of the file",data.describe())


        except Exception as e:
            print(e)

if __name__=="__main__":
    main()