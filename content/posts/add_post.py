from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Change of Plans, Django, and Full-Stack.
"""
content = """
Plans are meant to be changed. 

My original Final Product was to utilize a form of Machine Learning known as Photogrammetry, where a program utilizes a Neural Network and large amounts of data to map 2D figures onto a 3D model. However, after large amounts of research, I found two potential pathways: I could implement a highly efficient Neural Network that has already been created, where I would not be creating any new algorithms on my own, or I could create a new algorithm that will more than likely be less efficient than the industry standard, and therefore redundant. I didn’t like either of these options, so I decided to scrap the idea.

Instead, after tinkering with full-stack development in an Evidence of Learning, I knew I wanted to master this skill. As a result, I decided to create a web application that can create a Neural Network on any data provided. The program would also create the predictions for any new data. This would be a client-friendly website, allowing users without Machine Learning knowledge to make predictions using their data. I plan on utilizing a Python framework known as Django and a Javascript framework known as React to develop this web application. I have already completed the back-end difficulty of the project over the weekend, so all that’s left is developing an elegant front-end application. I’m disappointed in changing my project so last-minute, but I believe it will be worth the skills that I will end up learning.
"""

country_cities = {
        'title':title,
        'content':content
    }
with open('./content/posts/'+title.replace(' ','').replace('\n','')+'.md','w') as f:
    f.write('---\n')
    f.write('title: '+country_cities['title'].replace('\n',''))
    desc = country_cities['content'][0:100].replace('\n','')
    f.write('\ndescription: '+desc+'...')
    f.write('\ndate: '+d1)
    f.write('\ndraft: false')
    f.write('\nslug: /blog/'+title.replace(' ','-').replace('\n',''))
    f.write('\ntags: ')
    f.write('\n---\n')
    f.write(content)
    f.seek(0)