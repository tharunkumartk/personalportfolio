from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
CSS, Styled Components, and Career. 
"""
content = """
Maybe Data Science is not my future.

From this Final Product, I am realizing that I do not want to completely become a Data Scientist. The reason I love the field so much has less to do with the data within it, and more to do with the Artificial Intelligence algorithms that can be used with the data. I want to ensure that I still practice Artificial Intelligence in my career, but for my actual occupation, I feel that Data Science may be extremely repetitive and boring. My Final Product is helping me realize this because of how tedious constructing the database for my Final Product is. 

I believe that a Full Stack engineer is more akin to what I hope to do in the future. I enjoy most parts of Computer Science, including both front-end and back-end, but there are certain parts of both that I dislike. As a full-stack engineer, I would be able to do primarily the tasks I like, while the front-end/back-end experts can handle the tedious tasks that I dislike. 

My Final Product is still a work in progress. I have finally figured out a method of implementing the animation, so all I have to do is create the CSS through React’s Styled-Components module, and combine everything together. However, I am definitely cutting it close, since Final Presentation Night is just around the corner. But, I’m excited to see how my future ends up playing out. 
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