# import pandas as pd
# import streamlit as st
# from streamlit_option_menu import option_menu
# from PIL import Image

# # Streamlit page configuration

# st.set_page_config(layout = "wide")
# st.title("AIRBNB DATA ANALYSIS")
# st.write("")

# with st.sidebar:

#     select = option_menu("Main Menu",["Home", "Data Exploration", "About"])

# if select == "Home":
#     image1 = Image.open(r"C:\\Users\\viren\\OneDrive\Desktop\\IIT-MADARAS(GUVI)\\Airbnb Analysis\\AIRbnb.png.png")
#     st.image(image1)

#     st.header("About AirBnb")
#     st.write("")
#     st.write('''***Airbnb is a global online marketplace that connects people who want to rent out their homes with travelers
#               looking for accommodations. Founded in 2008 in San Francisco, Airbnb has transformed the way people 
#              travel by offering unique, affordable, and flexible alternatives to traditional hotels.
#              Through the platform, hosts can list properties ranging from shared rooms to entire homes, 
#              while guests can book stays in over 220+ countries and regions worldwide. Airbnb also provides experiences, 
#              allowing local hosts to offer activities like tours, cooking classes, and adventures.***''')

# if select == "Data Exploration":
#     pass

# if select == "About":
#     pass


import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Airbnb Data Analysis", layout="wide")

# ------------------- SIDEBAR MENU -------------------
with st.sidebar:
    select = option_menu(
        "Main Menu",
        ["Home", "Data Exploration", "About"],
        icons=["house", "bar-chart", "info-circle"],  # nice icons
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f8f9fa"},
            "icon": {"color": "red", "font-size": "22px"},
            "nav-link": {"font-size": "18px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#ff5a5f"},  # Airbnb theme color
        },
    )

# ------------------- HOME PAGE -------------------
if select == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            image1 = Image.open(r"AIRbnb.png.png")
            st.image(image1, use_container_width=True)
        except:
            st.warning("⚠️ Logo not found. Please check the image path.")

    with col2:
        st.markdown("<h2 style='color:#ff5a5f;'>Welcome to Airbnb Data Analysis</h2>", unsafe_allow_html=True)
        st.write(
            """
            Airbnb is a **global online marketplace** that connects people who want to rent out their homes 
            with travelers looking for accommodations.  
            
            ✅ Founded in **2008 in San Francisco**  
            ✅ Available in **220+ countries & regions**  
            ✅ Offers **unique stays** — from apartments to castles  
            ✅ Hosts can also provide **experiences & activities**  

            ---
            """
        )

# ------------------- DATA EXPLORATION -------------------
if select == "Data Exploration":
    st.markdown("<h2 style='color:#ff5a5f;'>📊 Data Exploration</h2>", unsafe_allow_html=True)
    st.info("This section will include Airbnb dataset exploration, visualizations, and insights.")
    # Example placeholder
    st.write("👉 Upload or connect your dataset here...")

# ------------------- ABOUT PAGE -------------------
if select == "About":
    st.markdown("<h2 style='color:#ff5a5f;'>ℹ️ About This Project</h2>", unsafe_allow_html=True)
    st.success(
        """
        This project focuses on analyzing **Airbnb data** using Python and Streamlit.  
        It aims to uncover insights about property availability, pricing, and customer preferences.
        
        **Tools & Skills Used:**  
        - 🐍 Python, Pandas, Numpy  
        - 📊 Streamlit, Plotly, Matplotlib  
        - 🗄️ MongoDB for data storage  
        - 🔍 EDA & Data Visualization  
        """
    )

