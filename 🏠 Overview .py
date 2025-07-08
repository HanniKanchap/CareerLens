import streamlit as st
import urllib.parse

# ---- Page Config ----
st.set_page_config(
    page_title="CareerLens – Smarter Career Moves",
    page_icon="📄",
    layout="wide"
)

# ---- Custom CSS Styling ----
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
.floating-button {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background-color: #7A288A; /* Purplish color */
  color: white !important;
  padding: 12px 20px;
  border-radius: 30px;
  text-align: center;
  font-weight: bold;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  z-index: 100;
  text-decoration: none !important;
}
.floating-button:hover {
  background-color: #8E44AD; /* Slightly lighter hover */
  color: white !important;
}
}
</style>

<div class="main-title">
    <h1>📄 CareerLens</h1>
    <h3>💬 Talk Careers. Land Roles. Stay Ahead.</h3>
    <p>Your intelligent career assistant for resume feedback, real-time chat guidance, and tailored job/internship discovery.</p>
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
### 📢 *Why CareerLens?*

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
### 🚀 *How to Get Started*

1. **Upload your resume** (PDF supported)  
2. **Chat with CareerLens** about your goals  
3. **Discover role-matched openings**  
4. **Analyze your skill alignment**  
5. **Download insights as a shareable PDF**  

🎯 Designed for job seekers, career coaches & resume reviewers.
""")

# ---- Features with Links to Pages ----
st.markdown("---")
st.markdown("### 🌟 *Platform Features*")

st.markdown("""
 ✅ Resume Analyzer powered by FLAN-T5, GPT  
 ✅ Interactive Career Chat Assistant  
 ✅ Skill-Role Match Score & Insights  
 ✅ Curated Job Opportunities  
 ✅ Curated Internship Listings  
 ✅ Stylized PDF Generator for Feedback Reports
""")

# ---- Sidebar CTA ----
st.sidebar.success("👈 Start your career journey using the sidebar modules!")
st.sidebar.markdown("✨ CareerLens combines resume intelligence, chat guidance, and opportunity discovery.")
 
# Q/A section
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")

with st.expander("📄 What file formats are supported for resume upload?"):
    st.markdown("We currently support **PDF** files. Future updates may include support for DOCX and TXT.")

with st.expander("💬 Can I talk to CareerLens about any industry role?"):
    st.markdown("Absolutely! Whether you're targeting tech, marketing, design, or even unconventional paths—CareerLens adapts based on your uploaded resume and chat input.")

with st.expander("🧠 What is CareerLens and how does it work?"):
    st.markdown("CareerLens is your AI-powered career assistant designed to analyze your resume, offer tailored guidance, and help you discover opportunities that fit your skills. Think of it as a smart career navigator that combines AI resume feedback, skill-role matching, and interactive guidance—all within a sleek Streamlit interface.")

with st.expander("💼 Where do the job and internship recommendations come from?"):
    st.markdown("Our listings are intelligently **scraped from Internshala**—a trusted portal for internship and job opportunities in India. Recommendations are filtered and ranked based on your profile and preferences.")

with st.expander("📝 Can I share the PDF report externally?"):
    st.markdown("Yes! The stylized PDF feedback reports are perfect for sharing with mentors, career coaches, or recruiters.")


# ---- Feedback Form ----

st.markdown("---")
st.markdown("### 💌 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    user_email = st.text_input("Your Email")
    query = st.text_area("Your Message", height=150)
    submitted = st.form_submit_button("📨 Create Email")

    if submitted:
        if name and user_email and query:
            subject = urllib.parse.quote("CareerLens Inquiry / Suggestion")
            body = urllib.parse.quote(f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{query}")
            mailto_link = f"mailto:hannikanchap11@gmail.com?subject={subject}&body={body}"

            st.markdown(f"[👉 Click here to open your email client and send](<{mailto_link}>)", unsafe_allow_html=True)
            st.info("✅ Your message has been pre-filled. Just hit send from your mail app.")
        else:
            st.warning("⚠️ Please complete all fields before submitting.")

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

# ---- Floating Chat Button ----
st.markdown("""
<a href="Career_Chat" class="floating-button">💬 Chat Now</a>
""", unsafe_allow_html=True)