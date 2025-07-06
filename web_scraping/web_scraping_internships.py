import requests
from bs4 import BeautifulSoup
import pandas as pd

all_jobs = []
for i in range(2,6):
    url = f"https://internshala.com/internships/information-technology-internship/page-{i}"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    print(r)
    soup = BeautifulSoup(r.text, "html.parser")

    cards = soup.find_all('div', class_='individual_internship')

    for card in cards:
        title = card.find('a', class_='job-title-href')
        company = card.find('p', class_='company-name')
        location = card.find('div', class_='locations')

        all_jobs.append({
        "Job Title": title.text.strip() if title else "",
        "Job link": f"https://internshala.com{title['href']}" if title and title.has_attr('href') else "",
        "Company": company.text.strip() if company else "",
        "location" : location.text.strip() if location else "",
        "Category": "Internship"
    })

df = pd.DataFrame(all_jobs)
print(df)
df.to_csv("career_lens_jobs.csv", index=False)
print("✅ Data saved to career_lens_jobs.csv")