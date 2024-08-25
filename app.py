import streamlit as st

st.set_page_config(page_title = "SMAQCloud2.0",  
                   page_icon =  "🐠", 
                   layout = "wide"
                   )

st.markdown(
    """
    <style>
      p {
        text-align: justify;
        text-justify: inter-word;
      }
    </style>
    """,
    unsafe_allow_html= True,
)

home_page = st.Page(
	page="pages/home.py",
	title="Home",
	icon = "🏡",
  default=True
)

sysparams_page = st.Page(
	page="pages/sysparams.py",
	title="System Parameters",
	icon = "📈",
)

plant_page = st.Page(
	page="pages/fish.py",
	title="Plant Monitoring",
	icon = "🪴",
)

fish_page = st.Page(
	page="pages/plant.py",
	title="Fish Monitoring",
	icon = "🐟",
)

#assign navigation
web_pages = st.navigation(pages = [home_page,sysparams_page,plant_page,fish_page]
				)

web_pages.run()

st.markdown(
    """
    <style>
      p {
        text-align:justiy;
        text-justify:inter-word;
      }
    </style>
    
    <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
    import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-analytics.js";

    const firebaseConfig = {
      apiKey: "AIzaSyCkdpVaklVq5hviY3e7cb_Zas7filzWw90",
      authDomain: "smaqcloudv2-prototype.firebaseapp.com",
      projectId: "smaqcloudv2-prototype",
      storageBucket: "smaqcloudv2-prototype.appspot.com",
      messagingSenderId: "172545355628",
      appId: "1:172545355628:web:de9863f39abf5d1482cd49",
      measurementId: "G-24EETGCXTH"
    };

    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
    </script>
    """,
    unsafe_allow_html=True,
)