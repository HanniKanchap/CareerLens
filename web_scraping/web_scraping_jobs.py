import requests 
import pandas as pd
from bs4 import BeautifulSoup

all_jobs = []

for i in range(2,4):
    url = f"https://internshala.com/jobs/information-technology-jobs/page-{i}"
    response = requests.get(url,headers = {"User-Agent": "Mozilla/5.0"})
    print(response)
    soup = BeautifulSoup(response.text,'html.parser')
    cards = soup.find_all('div',class_ = 'individual_internship')

    for card in cards:
        title = card.find('a', class_='job-title-href')
        company = card.find('p', class_='company-name')
        location = card.find('div', class_='locations')
        salary = card.find('span',class_ = "mobile")
        experience_element = card.select('.row-1-item span')
        all_jobs.append({
        "Job Title": title.text.strip() if title else "",
        "Job link": f"https://internshala.com{title['href']}" if title and title.has_attr('href') else "",
        "Company": company.text.strip() if company else "",
        "Location" : location.text.strip() if location else "",
        "Category": "Job",
        "Salary" : salary.text.strip() if salary else "",
        "Experience" : experience_element[-1].text.strip() if experience_element else ""
        })

df = pd.DataFrame(all_jobs)
print(df)
p = input("Continue ? ")
if p == 'n':
    exit(0)
df.to_csv("./data/Jobs_data_.csv",index = False)
print("🌟 Saved data")