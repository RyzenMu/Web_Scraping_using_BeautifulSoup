# Adding features to scraping Real Website
# latest published job advertisements from a website
import time

from bs4 import BeautifulSoup
import requests


print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')




    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').span.text
        if not 'few' in job_published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    # print(job_published_date)
                    # print(f'''
                    # Company Name: {company_name}
                    # Required skills: {skills}
                    # ''')

                    print(f'Company Name:  {company_name.strip()}')
                    print(f'Required skills: {skills.strip()}')
                    print(f'More Info: {more_info}')
                    print()
                    


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait*60)