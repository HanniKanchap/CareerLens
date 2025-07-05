import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="CareerLens – Smarter Career Moves",
    page_icon="📄",
    layout="wide"
)

# ---- Custom Styles ----
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #fce4ec, #ffffff);
}

@keyframes fadeSlideUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.main-title {
    text-align: left;
    margin-bottom: 20px;
    animation: fadeSlideUp 1.2s ease-out forwards;
}

.main-title h1 {
    color: #6a1b4d;
    font-size: 50px;
    font-family: 'Poppins', sans-serif;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.main-title h3 {
    color: #ad1457;
    font-size: 26px;
    margin-top: 10px;
    animation: fadeSlideUp 1.6s ease-out forwards;
}

.main-title p {
    color: #6d6d6d;
    font-size: 17px;
    font-style: italic;
    animation: fadeSlideUp 2s ease-out forwards;
}
</style>

<div class="main-title">
    <h1>📄 CareerLens</h1>
    <h3>💬 Talk Careers. Land Roles. Stay Ahead.</h3>
    <p>
        Your intelligent career assistant for resume feedback, real-time chat guidance, and tailored job/internship discovery.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- Hero Banner ----
st.image(
    "assets/hero_banner.jpg",
    use_container_width=True,
    caption="Smarter career choices begin with clarity and confidence."
)

# ---- Why CareerLens ----
st.markdown("---")
st.markdown("""
## 📢 *Why CareerLens?*

Whether you're a **student**, **switching roles**, or **scaling up your career**, CareerLens helps you:

- 📄 **Refine your resume** with actionable AI feedback  
- 🤖 **Chat with your AI Career Buddy** for role-specific advice  
- 💼 **Explore jobs & internships** that align with your skills  
- 🧠 **Understand your profile better** with skill-to-role mapping  
- 📈 **Download branded reports** that showcase your fit

✨ Built to empower you at every stage of your career journey.
""")

# ---- How It Works ----
st.markdown("---")
st.markdown("""
## 🚀 *How to Get Started*

1. **Upload your resume** (PDF/DOCX supported)  
2. **Chat with CareerLens** about your goals  
3. **Discover role-matched openings** (jobs & internships)  
4. **Analyze your skill alignment**  
5. **Download insights as a shareable PDF**

🎯 Designed for job seekers, career coaches & resume reviewers.
""")

# ---- Key Features ----
st.markdown("---")
st.markdown("""
## 🌟 *Platform Features*

- ✅ **Resume Analyzer** powered by FLAN-T5, GPT  
- ✅ **Interactive Career Chat Assistant**  
- ✅ **Skill-Role Match Score & Insights**  
- ✅ **Curated Job & Internship Recommendations**  
- ✅ **Stylized PDF Generator for Feedback Reports**
""")

# ---- Sidebar CTA ----
st.sidebar.success("👈 Start your career journey using the sidebar modules!")
st.sidebar.markdown("✨ CareerLens combines resume intelligence, chat guidance, and opportunity discovery.")

# ---- Final CTA ----
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3 style="color:#6a1b4d; font-size: 26px; font-weight: bold; animation: fadeIn 2s;">
        🚀 Ready to take the next step?<br>
        Talk, analyze, apply — with CareerLens at your side.
    </h3>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
# ---- Footer with Social Links ----
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: grey; font-size: 15px; line-height: 1.6;">
    Created with 💼 and ☕ by <b>HANNI</b> · CareerLens © 2025<br>
    Have a question or want to connect?
    <a href="https://www.linkedin.com/in/hanni-kanchap" target="_blank" style="color: #ad1457; text-decoration: none;">
        🔗 LinkedIn
    </a> &nbsp;|&nbsp;
    <a href="https://github.com/HanniKanchap" target="_blank" style="color: #ad1457; text-decoration: none;">
        💻 GitHub
    </a>
</div>
""", unsafe_allow_html=True)