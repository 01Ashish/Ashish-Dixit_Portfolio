import streamlit as st
from streamlit_option_menu import option_menu
import requests 
from streamlit_lottie import st_lottie
# Setting Page Config, must remain at top
st.set_page_config(page_title="My Portfolio ", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Creating Functions for differet Sections
# Home Function --------------------------------------------------------------------------------------------------------------
def Home():
    st.markdown("""
    ## Hi, I'm Ashish 👋
    # A Artificial Intelligent & Data Science Student
    By day, I'm immersed in the world of Artificial Intelligence, designing algorithms that power intelligent systems, and exploring the transformative potential of Generative AI to create meaningful, cutting-edge applications. By night, I delve into Machine Learning and Deep Learning, unearthing patterns, building predictive models, and crafting innovative solutions that redefine how data interacts with technology.

    This exploration is more than just a career—it's a commitment to harnessing AI's potential to revolutionize the way we work, create, and live. With every project, I strive to merge creativity and technology, leaving a lasting impact on the world of Generative AI and beyond.

    Does this fit your vision? 😊

    📂 Here, you will find a collection of my **projects**, **achievements**, and **insights** into the world of data science and artificial intelligence. 🌐 Explore and feel free to reach out if you have any questions or collaboration ideas!

    📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/ashish-dixit-ba587b200/) || [GitHub](https://github.com/01Ashish) ||  [Email](mailto:ashdixit2003@gmail.com)
    """)
    st.write("Here's my resume:")
    with open("/home/ashish-dixit/ashish/vscode/iit/speech2text/faster_gt/Ashish_cv(16 Nov).pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Ashish_cv(16 Nov).pdf",
            mime="application/pdf"
        )
    lottie_url = "https://lottie.host/f56472c3-2021-4eb8-92e2-39ea06345f42/1L7J5mRwno.json"
    lottie_animation = load_lottieurl(lottie_url)
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="home")
    else:
        st.error("Failed to load Lottie animation.")
    
# Experince Function --------------------------------------------------------------------------------------------------------------
def Experience():
    st.markdown("# 💼 Work Experience")
    
    # Work 1 Container
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/db13156d-fdc8-452f-9377-7be3cf91990b/uGa0YUaQmL.json"  # Replace with your Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="work1")
            else:
                st.error("Add your Lottie animation URL for Work Experience 1.")
        with text_col:
            st.write("### AI/ML Intern Intern")
            st.write("""
                    - **Company**: [Bikham Healthcare](https://www.bikham.com/)  
                    - **Duration**: Aug 2024 - Present  
                    - **Highlights**:
                        - Works in US Shifts and interacting with US Clients. Involved in backend development projects focused on AI-
                        driven automation, including chatbot development, and integrating APIs for data extraction and task
                        optimization for making credentialling task automated.  
                        - Collaborated with cross-functional teams to deploy scalable solutions using **TensorFlow** and **Streamlit**.  
                    """)
            st.write("[Explore Company Website](https://www.bikham.com/)")
    
    st.write("---")
    
    # Work 2 Container
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/0254e2d8-da78-4056-8c3e-24849b37090d/uONs9yKEH0.json"  # Replace with the Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="iit_delhi")
            else:
                st.error("Add your Lottie animation URL for IIT Delhi experience.")
        with text_col:
            st.write("### Research Intern")
            st.write("""
                    - **Institution**: (IIT Delhi)[https://home.iitd.ac.in/] 
                    - **Duration**: May 2024 - Nov 2024  
                    - **Highlights**:
                        - Coordinated with the frontend team to build an **Automatic Speech Recognition (ASR) API**.  
                        - Integrated **Diarization capabilities** for bilingual speech processing.  
                        - Contributed to research projects in cutting-edge AI technologies.
                    """)
            st.write("[Explore Company Website](https://home.iitd.ac.in/)")

    st.write("---")
    
    # Experience 2: Edulyt India
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/5fc47551-c865-4f0b-80ea-6ab745c0a3b1/esGXdLQPX8.json"  # Replace with the Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="edulyt_india")
            else:
                st.error("Add your Lottie animation URL for Edulyt India experience.")
        with text_col:
            st.write("### Data Analyst Intern")
            st.write("""
                    - **Company**: (Edulyt India)[https://edulyt.com/]  
                    - **Duration**: Jun 2024 - Sep 2024  
                    - **Highlights**:
                        - Performed **data cleaning**, **sanity checks**, and **analysis** for business insights.  
                        - Created impactful **visualizations** to support data-driven strategies.  
                        - Played a key role in decision-making processes by providing actionable insights.
                    """)
            st.write("[Explore Company Website](https://edulyt.com/)")

    st.write("---")
    
    # Experience 3: Pantech Prolabs India Pvt. Ltd.
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/0254e2d8-da78-4056-8c3e-24849b37090d/uONs9yKEH0.json"  # Replace with the Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="pantech_prolabs")
            else:
                st.error("Add your Lottie animation URL for Pantech Prolabs experience.")
        with text_col:
            st.write("### Artificial Intelligence Intern")
            st.write("""
                    - **Company**: (Pantech Prolabs India Pvt. Ltd.)[https://www.pantechsolutions.net/]  
                    - **Duration**: Aug 2023 - Sep 2023  
                    - **Highlights**:
                        - Mentored junior interns on **AI concepts** and programming best practices.  
                        - Built and optimized **deep learning models** using **TensorFlow** and **Keras**.  
                        - Provided debugging assistance to improve code reliability and system performance.
                    """)
            st.write("[Explore Company Website](https://www.pantechsolutions.net/)")
# Projects Function --------------------------------------------------------------------------------------------------------------
def Projects():
    st.title('My Projects')
    # Project 1 Container
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/968eeb96-ecab-4fe7-8345-445d0815cd91/QMeTBigFru.json"  # Replace with appropriate Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project1")
            else:
                st.error("Add your Lottie animation URL for ASR project.")
        with text_col:
            st.write("### Automatic Speech Recognition with Diarization")
            st.write("""
                    - **Model Building**: Built using Python and FasterWhisper (`Ctranslate2 transformer engine`) large-v2.  
                    - **Model Implementation**: Developed an interactive application using Python's Streamlit framework.  
                    - **Deployment**: Deployed the project using Pyngrok by creating secure tunneling from Colab localhost to public URLs, leveraging Colab's T-4 GPU.  
                    - **Repository**: [Explore the GitHub Repo](https://github.com/01Ashish/ASR-SpeakerDiarization).
                    """)
            if st.button("Know More ➡️", key="speech"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Streamlit")
                        st.write("- FasterWhisper")
                        st.write("- Flask")

                    with col2:
                        st.write("- Pyngrok")
                        st.write("- Colab (T-4 GPU)")
                
                with st.expander("Features", expanded=False):
                    st.write("""
                            - **Automatic Diarization**: Identifies and separates speakers in audio files.
                            - **Real-Time Speech Recognition**: Processes and converts bilingual speech to text.
                            - **User-Friendly Interface**: Easy-to-use Streamlit-based web app.
                            """)

    # Project 2: VedaVox Ayurveda Chatbot
    with st.container():
        st.write("---")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/68882159-ef9d-452d-b3af-5906fcd682cc/4SvphCphCS.json"  # Replace with appropriate Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project2")
            else:
                st.error("Add your Lottie animation URL for Chatbot project.")
        with text_col:
            st.write("### VedaVox: The Ayurveda Chatbot")
            st.write("""
                    - **STT and TTS Integration**: Users can query the chatbot without typing, using speech-to-text and text-to-speech.  
                    - **Knowledge Base**: Trained to provide accurate Ayurvedic information and recommendations.  
                    - **Repository**: [Explore the GitHub Repo](https://github.com/01Ashish/VedaVox---The-Ayurveda-Chatbot).  
                    """)
            if st.button("Know More 🚀", key="chatbot"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Speech-to-Text (STT)")
                        st.write("- Text-to-Speech (TTS)")
                    with col2:
                        st.write("- NLTK")
                        st.write("- Flask")
                
                with st.expander("Features", expanded=False):
                    st.write("""
                            - **Voice Interaction**: Fully voice-based interaction using STT and TTS.
                            - **Ayurveda Knowledge Base**: Provides detailed Ayurvedic insights and suggestions.
                            - **Custom Responses**: Dynamically generates accurate responses for various queries.
                            """)

    # Project 3: Abstractive Text Summarizer
    with st.container():
        st.write("---")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/35ecc059-3649-48fc-a898-b8f8a74a1b13/L0dvbbjXhd.json"  # Replace with appropriate Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project3")
            else:
                st.error("Add your Lottie animation URL for Summarizer project.")
        with text_col:
            st.write("### Abstractive Text Summarizer")
            st.write("""
                    - **Model Building**: Utilized the transformer model `facebook/bart-large-cnn` via Hugging Face API.  
                    - **Model Implementation**: Implemented using Flask for the backend and HTML/CSS for the frontend.  
                    - **Deployment**: Hosted the application on PythonAnywhere.  
                    - **Repository**: [Explore the GitHub Repo](https://github.com/01Ashish/Text-Summarizer).
                    - **Live Demo**: [Try the Summarizer](https://ashish11.pythonanywhere.com/).  
                    """)
            if st.button("Know More 🎂", key="summarizer"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Flask")
                        st.write("- HTML/CSS")
                    with col2:
                        st.write("- Hugging Face API")
                        st.write("- BART Transformer")
                
                with st.expander("Features", expanded=False):
                    st.write("""
                            - **Abstractive Summarization**: Generates concise and meaningful summaries.
                            - **Interactive Interface**: User-friendly design for ease of use.
                            - **Scalable Deployment**: Efficiently hosted on PythonAnywhere.
                            """)
# Research Function --------------------------------------------------------------------------------------------------------------
def ResearchPaper():
    st.title("📄 Research Paper")
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/6b336b2b-73e7-46d3-9378-9a61e537876c/JpXZtKXvWq.json"  # Replace with appropriate Lottie animation URL
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="research_paper")
            else:
                st.error("Add your Lottie animation URL for the Research Paper section.")
        with text_col:
            st.write("### Comparative Study of Recognition of Textual Data using EAST Model and OCR")
            st.write("""
                    - 📘 **Presented At**: 13th Conference of IRSD (I2OR - International Institute of Organized Research).  
                    - 📈 **Focus**: Enhancing text recognition accuracy and efficiency in image-based document analysis.  
                    - 🧠 **Methodology**:
                        - Combined the **EAST detection model** with advanced **OCR algorithms**.
                        - Aimed to achieve robust and reliable text extraction for complex datasets.  
                    - 🌍 **Impact**: Proposed solutions to improve performance in image-to-text conversion systems, setting new benchmarks in document analysis.
                    """)
# Achievements Function --------------------------------------------------------------------------------------------------------------
def Achievements():
    with st.container():
        st.write("# 🏆 My Achievements")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                        - 🏅 **2nd Runner-Up** in MAIT Technical Poster Competition. Secured **3rd Prize** for outstanding innovation and presentation.  
                        - 🧠 Solved **300+ questions on LeetCode**. I'm on a roll!  
                        - 🌟 Member of the **Datalect Society**, actively contributing to data-driven initiatives and events.    
                    """)
            st.markdown("""
                        I believe that every achievement, big or small, is a stepping stone towards success. I am always eager to learn and grow, and I am excited to see what the future holds for me. 🚀
                        """)
        with col2:
            lottie_url = "https://lottie.host/a7990eb1-5152-4cd1-a7fd-e0c592683b97/KOvlwaJ4uL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="achievements")
            else:
                st.error("Failed to load Lottie animation.")
        st.write("---")
        st.write("# 📚 I Like To Talk About")
        st.markdown("""
                    - **Data Science**
                    - **Machine Learning**
                    - **Deep Learning**
                    - **Artificial Intelligence**
                    - **Computer Vision**
                    - **Natural Language Processing**
                    - **Data Structures & Algorithms**
                    - **Self-Improvement** 
                    """) 

# Skills Function --------------------------------------------------------------------------------------------------------------
def Skills():
    
    with st.container():
        st.write("### 💼 My Skills")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                    - **Languages**: Python, Java, SQL, CSS, HTML
                    - **Development**: Flask, Gradio, Streamlit, HTML, Bootstrap CSS
                    - **Data Science**: Scikit-learn, Huggingface, Nltk, Langchain, Opencv, Generative AI, LLM
                    - **Tools**: Git, Jupyter Notebook, VS Code
                    - **Deep Learning**: Tensorflow, Keras, NLP & it's Libraries
                    - **Databases**: MySQL, Vector Databases                      
                    - **Soft Skills**: Teamwork, Communication, Problem-Solving, Time Management, Adaptability                    
                """)
        with col2:
            lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="skills")
            else:
                st.error("Failed to load Lottie animation.")

# Setting Sidebar Main Menu ------------------------------------------------------------------------------------------------------------
with st.sidebar:
    selected_page = option_menu(
        "Navigate Here", 
        ["Home","Experience", "Projects", "Research/Publication","Achievements","Skills"],
        icons = ['house', 'braces', 'trophy', 'code'],
        menu_icon = "cast",
        default_index = 0,
        )

# Displaying Selected Page --------------------------------------------------------------------------------------------------------------

if selected_page == "Home":
    Home()
elif selected_page == "Experience":
    Experience()
elif selected_page == "Projects":
    Projects()
elif selected_page == "Research/Publication":
    ResearchPaper()
elif selected_page == "Achievements":
    Achievements()
elif selected_page == "Skills":
    Skills()
