import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Hyerim Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author: Hyerim Hong")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Hyerim</h1></div>""")  # TODO: Add your name


    # ----- Profile image file -----
    profile_image_file_path = "Hyerim.jpeg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "I am currently studying Big Data Analytics at EAE Business School." \
    "I graduated in Hotel and Tourism Management from CETT–University of Barcelona." \
    "I have professional experience working as a receptionist in hotels in both South Korea and Spain, where I developed strong customer service, communication, and operational skills." \
    "My goal is to contribute to business decision-making by combining data analytics expertise with a solid background in tourism and hospitality management."   # TODO: Change this

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 🧑‍💻 I am a student in EAE Business School (Big Data Analystic) 

    - 🛩️ prev: Bachelor’s degree in Hotel and Tourism Management from CETT-UB, with hands-on experience in Reception and VIP Services at five-star hotels in Seoul and Barcelona
    
    - ❤️ With my background, I am highly motivated to work in business data analysis to generate insights that support strategic decisions

    - 🤖 Personal Projects :  http://127.0.0.1:8502/

    - 🏂 My hobby is doing sports, reading books

    - 📫 How to reach me: carol011017@gmail.com / +34 695 864 286
             
    - 🔗 Linkedin : www.linkedin.com/in/hyerim-hong-82765a2b4

    - 🏠 Barcelona
             

    """)
     

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()