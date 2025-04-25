import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Aniket's Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding: 1.5rem;
    }
    
    .profile-header {
        text-align: center;
        margin-bottom: 1.5rem;
        padding: 0.5rem;
    }
    
    .profile-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    
    .profile-header h2 {
        font-size: 1.5rem;
        font-weight: 500;
        color: #4a4a4a;
    }
    
    .section {
        background-color: #f8f9fa;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 0.75rem;
        border: 1px solid #e9ecef;
    }
    
    .section h1 {
        font-size: 1.75rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 1rem;
    }
    
    .section h2 {
        font-size: 1.25rem;
        font-weight: 500;
        color: #2a2a2a;
        margin-bottom: 0.75rem;
    }
    
    .section p {
        font-size: 1rem;
        line-height: 1.6;
        color: #333333;
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 0.75rem;
    }
    
    .social-links a {
        color: #0066cc;
        text-decoration: none;
        font-weight: 500;
    }
    
    .social-links a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Profile Header
st.markdown('<div class="profile-header">', unsafe_allow_html=True)
st.title("Aniket Mahangare")
st.subheader("Software Engineer at Uber")
st.markdown("</div>", unsafe_allow_html=True)

# About Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("About Me")
st.write("""
I'm a Software Engineer at Uber with a strong focus on building scalable and efficient systems. 
With expertise in Go, Java, and Python, I specialize in developing high-performance applications 
that power millions of rides daily. My work at Uber involves building robust systems that ensure 
reliable transportation services for users worldwide.

I'm passionate about leveraging AI and machine learning to enhance development workflows and 
create more intelligent systems. My approach combines technical excellence with a deep 
understanding of how technology can solve real-world problems.

When I'm not coding, I'm exploring new technologies and contributing to open-source projects.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Professional Experience
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Professional Experience")
st.subheader("Software Engineer at Uber")
st.write("""
• Developing and maintaining critical software systems that power millions of rides daily\n
• Collaborating with cross-functional teams to deliver high-impact features\n
• Implementing best practices in software engineering and system design\n
• Contributing to Uber's mission of making transportation as reliable as running water\n
• Working on scalable and efficient solutions using Go, Java, and Python\n
""")
st.markdown("</div>", unsafe_allow_html=True)

# Skills
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming Languages")
    st.write("• Go")
    st.write("• Java")
    st.write("• Python")
    st.write("• SQL")

with col2:
    st.subheader("Technologies & Frameworks")
    st.write("• FastAPI")
    st.write("• gRPC")
    st.write("• AWS")
    st.write("• Docker")
    st.write("• Kubernetes")

with col3:
    st.subheader("Tools & Practices")
    st.write("• Git")
    st.write("• CI/CD")
    st.write("• Agile Methodologies")
    st.write("• System Design")
    st.write("• Microservices")
st.markdown("</div>", unsafe_allow_html=True)

# Contact Information
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Get in Touch")
st.markdown("""
<div class="social-links">
    <a href="https://www.linkedin.com/in/aniket-mahangare/" target="_blank">LinkedIn</a>
    <a href="https://github.com/Niket1997" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

