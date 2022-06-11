# Scraping Real Website
# latest published job advertisements from a website

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')



jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    job_published_date = job.find('span', class_='sim-posted').span.text
    if not 'few' in job_published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        # print(job_published_date)
        print(f'''
        Company Name: {company_name}
        Required skills: {skills}
        ''')


