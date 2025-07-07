import streamlit as st
import pandas as pd

st.set_page_config(page_title="Internship Opportunities Portal", layout="wide")

st.markdown(
    """
    <div style='text-align: center; padding: 10px; margin-bottom: 30px;
                background: linear-gradient(135deg, #f4eaff, #e9dfff);
                border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
        <h1 style='font-family: "Segoe UI", sans-serif; color: #2c3e50;'>
            🎓 Find Internship Opportunities
        </h1>
        <p style='font-size: 16px; color: #34495e;'>
            Browse exciting internships across cities and domains!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load Data
df = pd.read_csv("data/cleaned_internship_data.csv") 
cat_choices = df['Category'].unique()
loc_choices = df['Location'].unique()

# Filter selections
selected_category = st.selectbox("Select Internship Category", options=['--Select Category--'] + sorted(list(cat_choices)))
selected_location = st.selectbox("Select Preferred Location", options=['--Select Location--'] + list(loc_choices))


if selected_category == '--Select Category--' and selected_location == '--Select Location--':
    st.subheader("📋 All Internship Listings")
    display_df = df[['Job Title', 'Company', 'Location', 'Job link']]
elif selected_category != '--Select Category--' and selected_location != '--Select Location--':
    st.subheader(f"📄 Job Listings for {selected_category} roles")
    display_df = df[(df['Category'] == selected_category) & (df['Location'] == selected_location)][['Job Title', 'Company', 'Location', 'Job link']]
elif selected_category != '--Select Category--':
    st.subheader(f"📄 Job Listings for {selected_category} roles")
    display_df = df[df['Category'] == selected_category][['Job Title', 'Company', 'Location', 'Job link']]
else:
    display_df = df[df['Location'] == selected_location][['Job Title', 'Company', 'Location', 'Job link']]

if display_df.empty:
    st.markdown(
        """
        <div style='text-align:center; margin-top:30px; color:grey; text-shadow: 0 0.5px 1.2px grey;'>
            <h4>No internships found for the selected filters.</h4>
        </div>
        """, unsafe_allow_html=True)
else:
    for _, row in display_df.iterrows():

        with st.container():
            st.markdown(
                f"""
                <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin: 10px 0;
                            background-color: #fdfbff; box-shadow: 0 1px 5px rgba(200, 150, 255, 0.3);'>
                    <h4 style='margin-bottom: 5px; color: #2c3e50;'>{row['Job Title']}</h4>
                    <p style='margin: 2px 0;'><strong>🏢 Company:</strong> {row['Company']}</p>
                    <p style='margin: 2px 0;'><strong>📍 Location:</strong> {row['Location']}</p>
                    <a href="{row['Job link']}" target="_blank" style='color: #0077cc; text-decoration: none; font-weight: bold;'>🔗 Apply Now</a>
                </div>
                """,
                unsafe_allow_html=True
            )