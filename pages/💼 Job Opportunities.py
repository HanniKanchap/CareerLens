import streamlit as st
import pandas as pd

st.set_page_config(page_title="Job Opportunities Portal", layout="wide")
 
st.markdown(
    """
    <div style='text-align: center; padding: 10px; margin-bottom : 30px; background: linear-gradient(135deg, #f4eaff, #e9dfff); border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
        <h1 style='font-family: "Segoe UI", sans-serif; color: #2c3e50;'>
            🌟 Find Job Opportunities
        </h1>
        <p style='font-size: 16px; color: #34495e;'>
            Explore roles in top tech companies!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
df = pd.read_csv("data/cleaned_job_data.csv")
cat_choices = df['Category'].unique()
exp = df['Experience(in yrs)'].unique()

selected_category = st.selectbox("Select Job Category",options = ['--Select Category--'] + list(cat_choices))
selected_experience = st.selectbox("Select Job Experience (in yrs)",options = ['--Select your Experience--'] + sorted(list(exp)))

if selected_category == '--Select Category--' and selected_experience == '--Select your Experience--':
    filtered_df = df
    st.subheader(f"📄 All Job Listings")
elif selected_category != '--Select Category--' and selected_experience != '--Select your Experience--':
    filtered_df = df[(df['Category'] == selected_category) & (df['Experience(in yrs)'] == selected_experience)][['Job Title', 'Company', 'Salary', 'Experience', 'Job link']]
    st.subheader(f"📄 Job Listings for {selected_category} roles")
elif selected_category != '--Select Category--' and selected_experience == '--Select your Experience--':
    filtered_df = df[(df['Category'] == selected_category)][['Job Title', 'Company', 'Salary', 'Experience', 'Job link']]
    st.subheader(f"📄 Job Listings for {selected_category} roles")
  
if filtered_df.empty:
    st.markdown("<div style = 'text-align:center;margin-top:30px;color:grey;text-shadow: 0 0.5px 1.2px grey'><h4>No jobs found for the selected category and experience level.</h4></div>",unsafe_allow_html=True)
else:
    for index, row in filtered_df.iterrows():
        with st.container():
            st.markdown(
                f"""
                <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin: 10px 0;
                            background-color: #fdfbff; box-shadow: 0 1px 5px rgba(200, 150, 255, 0.3);'>
                    <h4 style='margin-bottom: 5px; color: #2c3e50;'>{row['Job Title']}</h4>
                    <p style='margin: 2px 0;'><strong>🏢 Company:</strong> {row['Company']}</p>
                    <p style='margin: 2px 0;'><strong>💰 Salary:</strong> {row['Salary']}</p>
                    <p style='margin: 2px 0;'><strong>📊 Experience:</strong> {row['Experience']}</p>
                    <a href="{row['Job link']}" target="_blank" style='color: #0077cc; text-decoration: none; font-weight: bold;'>🔗 Apply Now</a>
                </div>
                """,
                unsafe_allow_html=True
            )