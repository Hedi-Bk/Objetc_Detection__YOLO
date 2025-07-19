import streamlit as st 


st.title("Haram Blur ❤️")

#st.sidebar.header("Haram Blur From Images Uploaded")

st.markdown("""
* Using Image as an Input :
1. Get your image from your computer that u want to blur it.
2. Test it !
* Exemple :
""")

col1 , col2 ,col3 = st.columns([2,1,2])
with col1 :
    st.image("D:\ASL\PROJETs\ML\Object_Detetction\Project3-HaramBlur\images\images.jpg")
with col2 :
    st.markdown("""
                ###
                ###   ---🙈->
                """)
with col3 :
    st.image("D:\ASL\PROJETs\ML\Object_Detetction\Project3-HaramBlur\images\HaramBlur.jpg")