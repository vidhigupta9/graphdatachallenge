import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import json
import re
import configparser
import preprocess as pp
from csv import writer
import similarity as sm
import hypergraph as hg


#To Hide Warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style> """


def main():

    html_temp = """
    <link href='https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&display=swap' rel='stylesheet'>
	    <div style="background-color:#8C1515;">
            <p style="color:white;font-size:50px;padding:9px;text-transform:uppercase;font-family:Open Sans,sans-serif;;letter-spacing: 3px">
                <b>Phizon</b>
            </p>
        </div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Don't be the victim!")
 
    from PIL import Image
    #image = Image.open('')
    #st.image(image,use_column_width=True)
	

    def enter_news():
        # Collect Input from user :
        news = str(st.text_input("Enter the text (Press Enter once done)"))
        publisher = str(st.text_input("Enter the publisher name (Press Enter once done)"))
        # Import writer class from csv module
        df = pd.read_csv("newdata.csv",index_col=0)
        length = df.shape[0]
        with open('newdata.csv','a',newline='') as f_object:
            temp = [int(length),pp.clean_publisher(str(publisher)),pp.clean_news(str(news))]
            writer_object = writer(f_object)
            writer_object.writerow(temp)
            f_object.close()
            st.write("done news")


    def similarity_process(name):
        df = sm.similarity(name)
        st.write("similarity")

    process_name = st.selectbox(
    'Select Operation',
    ('Select','Enter News')
    )

    if process_name == 'Enter News':
        enter_news()
        similarity_process("similarity_scores.csv")  
        hy , l = hg.build()
        st.write("hypergraph built")
        image = Image.open(hg.draw(hy))
        st.image(image,use_column_width=True)
        hg.hyper_file(l)
        similarity_process("hypernode.csv")
        st.write("hyper similarity built")
        #my_bar =  st.progress(100)
        #if st.button("Predict Results"):
            #st.write(result)             
       
    
    #Sidebar
    st.sidebar.header("About App")
    st.sidebar.info("")
    
    st.sidebar.info("[Source Code](https://github.com/vidhigupta9/graphdatachallenge)")
    st.sidebar.header("Made by :")
    st.sidebar.info("[Vidhi Gupta](https://github.com/vidhigupta9)")
    st.sidebar.info("[Deep Rodge](https://github.com/deeprodge)")
    

if st.button("Exit"):
        st.balloons()


if __name__ == '__main__':
    main()