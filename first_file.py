import pandas as pd 
import streamlit as st 
import numpy as np 

########creating the title-
st.title("HELLO STREAMLIT")

####writing the text
st.write("i am providing some information for your convience")

####creating a simple dataframe (tables)
df=pd.DataFrame(
    {
        'first_column':[1,2,3,4],
        'second_column':[20,30,40,50]
    }
)

##displaying that dataframe
st.write("my dataframe")
st.write(df)

##creating a line chart
chart_Data=pd.DataFrame(
                np.random.rand(20,3),columns=['a','b','c']
            )
st.line_chart(chart_Data)