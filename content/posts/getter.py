import requests
from bs4 import BeautifulSoup
import os
import sys
while True:
    link = input()
    main_blog = requests.get(link)
    main_blog_soup = BeautifulSoup(main_blog.content, 'html.parser')

    month_to_number = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12,
    }

    title = main_blog_soup.find(class_='blog-post-title-font').text
    date = main_blog_soup.find(class_='time-ago')
    dateMonth = str(month_to_number[date.text[0:3].lower()])
    if len(dateMonth)==1:
        dateMonth = '0'+dateMonth
    dateDay = date.text[3:6].strip().replace(',','')
    if len(dateDay)==1:
        dateDay = '0'+dateDay
    dateYear = date.text[len(date.text)-4:len(date.text)]
    formatted_date = dateYear+'-'+dateMonth+'-'+dateDay
    posts = main_blog_soup.find_all('p')
    content = ''
    for i in posts:
        texts = i.find_all('span')
        for j in texts:
            content=content+j.text+'\n\n'

    country_cities = {
        'title':title,
        'content':content
    }
    file_name = title.replace(' ','').replace('.','').replace('\n','')+'.md'
    save_path = 'content\posts\\'+file_name
    content = content.replace('�','\'')
    complete_path = os.path.join(save_path,file_name)
    with open(save_path,'w') as f:
        f.write('---\n')
        f.write('title: '+country_cities['title'])
        desc = country_cities['content'][0:100]
        desc = desc.replace('\n', '').replace('�','\'')
        f.write('\ndescription: '+desc+'...')
        f.write('\ndate: '+formatted_date)
        f.write('\ndraft: false')
        f.write('\nslug: /blog/'+title.replace(' ','-'))
        f.write('\ntags: ')
        f.write('\n---\n')
        f.write(content)
        f.seek(0)
    


