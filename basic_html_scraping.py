# basic web scrapping from local basic html file

from bs4 import BeautifulSoup

with open("basic_html_1.html", 'r') as html_file:
    content = html_file.read()
    #print(content)
    print('--------------------------------')

    # print h5 tags
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tags = soup.find_all('h5')



    #print(tag for tag in tags)

    # tag = [i for i in tags]
    # print(tag)

    # for tag in tags:
    #     print(tag)


    # print all the courses in the html file

    soup = BeautifulSoup(content, 'lxml')
    courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    for course in courses_html_tags:
        print(course.text)

    # print the prices
    soup = BeautifulSoup(content, 'lxml')
    prices_html_tags = soup.find_all('a')

    for price in prices_html_tags:
        print(price.text)

    # print the prices for corresponding courses by my method
    for course, price in zip(courses_html_tags, prices_html_tags):
        print(course.text + ': '+price.text)
    print('------------------------------------')



    # print the prices for corresponding courses by Jim

    soup = BeautifulSoup(content, 'lxml')
    couse_cards = soup.find_all('div', class_='card')
    for course in couse_cards:
        #print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # prints only the last 20$ like
        print(f'{course_name}costs {course_price}')

