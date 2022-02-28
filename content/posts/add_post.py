from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Winter Showcase, Final Product, and Excitement,
"""
content = """
Learning is one challenge, but teaching is a whole different breed.

This last week, I participated in my very first Winter Showcase, since last year’s was canceled due to COVID-19. It was a wild experience; most of the time, I’ve had to explain Artificial Intelligence to younger students, like high-schoolers, or I’ve had to explain it to more technologically adept adults. However, at the ISM Winter Showcase I had to explain the complex field to a wide variety of people, from older couples to actual Software Engineers. However, after the first couple of meets, I got the hang of it. The trick is to begin by asking questions to get an idea of the audience’s knowledge in the subject. After that, I was able to categorize each group based on how much they knew. Then, I made the information simple for the given category. 

However, throughout my time speaking to random people, I had a lot of downtime, where I thought about my Final Product. Based on how difficult and unrealistic my previous idea for my Final Product was, I decided on a new idea. I still wanted to utilize Computer Vision and 3D-models, but I didn’t want to utilize Natural Language Processing because the overall concept did not make that much sense. My new Final Product idea is to create a program that simply looks at 3D-objects and generates 3D-models for them. This could be used to develop cheaper alternatives to a variety of tools in a variety of different fields. I’m excited to see how this Final Product goes.

"""

country_cities = {
        'title':title,
        'content':content
    }
with open('./content/posts/'+title.replace(' ','-').replace('\n','')+'.md','w') as f:
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