from transformers import pipeline, set_seed
import pandas as pd
import fitz  # PyMuPDF
from pathlib import Path

# Step 1: Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.lower()

# Step 2: Extract keywords from resume
def extract_skills(text, keywords):
    return [word for word in keywords if word in text]

# Step 3: Load skill database and extract relevant keywords
def load_skill_database(csv_path, role):
    df = pd.read_csv(csv_path)
    df['Role'] = df['Role'].str.lower()
    role = role.lower()

    filtered_df = df[df['Role'] == role]
    if filtered_df.empty:
        print(f"🚫 No entries found for role: '{role}'.")
        return set()

    keywords_series = pd.concat([
        filtered_df["ATS Keywords"].dropna().str.split(","),
        filtered_df["Skills"].dropna().str.split(",")
    ]).explode().str.strip().dropna()

    return set(keywords_series)

# Step 4: Compare skills and generate score
def evaluate_resume(extracted_skills, expected_keywords, role):
    extracted_set = set(extracted_skills)
    matched = extracted_set & expected_keywords
    suggestions = expected_keywords - extracted_set
    match_score = round((len(matched) / len(expected_keywords)) * 10, 2) if expected_keywords else 0

    return [{
        "Role": role,
        "Score (out of 10)": match_score,
        "Matched Keywords": list(matched),
        "Suggested Improvements": list(suggestions)
    }]

# Step 5: Generate GPT-style suggestions
gpt_generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_gpt_suggestions(missing_keywords):
    suggestions = []
    for keyword in missing_keywords:
        prompt = f"To improve your resume, consider highlighting experience with {keyword}. For example,"
        output = gpt_generator(prompt, max_new_tokens=50, num_return_sequences=1, pad_token_id=50256)[0]['generated_text']
        suggestion = output.strip().split("\n")[0]
        suggestions.append(suggestion)
    return suggestions

# Step 6: Main pipeline
def main(resume_path, skill_db_path, role):
    print("🔍 Parsing resume...")
    resume_text = extract_text_from_pdf(resume_path)

    print("📚 Loading skill database...")
    expected_keywords = load_skill_database(skill_db_path, role)
    print(f"✅ Loaded {len(expected_keywords)} keywords for role '{role}'\n")

    print("🧠 Extracting skills...")
    extracted = extract_skills(resume_text, expected_keywords)
    print(f"✅ Extracted {len(extracted)} potential skills\n")

    print("📊 Evaluating resume...\n")
    report = evaluate_resume(extracted, expected_keywords, role)

    for entry in report:
        print(f"📌 Role: {entry['Role']}")
        print(f"⭐ Score: {entry['Score (out of 10)']} / 10")
        print(f"✅ Matched Keywords: {', '.join(entry['Matched Keywords']) or 'None'}")
        if entry['Suggested Improvements']:
            print("💡 Suggestions:")
            gpt_suggestions = generate_gpt_suggestions(entry['Suggested Improvements'])
            for suggestion in gpt_suggestions:
                print("   •", suggestion)
        else:
            print("💯 No major skill gaps found. Your resume is strongly aligned!")
        print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    resume_path = Path("module") / "Resume.pdf"
    skill_db_path = Path("data/skills_data.csv")
    role = "Data Analyst"
    main(resume_path, skill_db_path, role)