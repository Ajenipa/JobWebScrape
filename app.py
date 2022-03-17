import time
from bs4 import BeautifulSoup
import requests
unwanted_skills = input('Enter Unwanted Skills:...')
print(f"filtering {unwanted_skills}..")
def find_job():
    page = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(page, 'lxml')


    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").text
        if 'few' in published_date :
            company_name = job.find('h3', class_="joblist-comp-name").text.replace('','')
            skills = job.find("span", class_="srp-skills").text.replace('','')
            job_link = job.header.h2.a['href']
            if unwanted_skills not in skills:
                with open(f'data/{index}.txt', 'w') as f:
                    f.write(f"Company Name:{company_name.strip()} \n")
                    f.write(f"Skills:{skills.strip()}\n")
                    f.write(f"Links:{job_link.strip()}")
                print(f'file saved in data {index}')
if __name__ == '__main__':
    while True:
        find_job()
        wait_time = 10
        time.sleep(600*wait_time)
        print(f'waiting {wait_time} minutes')
        