from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Drones, Ideas, and Final Product.
"""
content = """
Our future is in drones.

For the past week, I have been working with drones; I implemented a variety of object/facial detection algorithms for the drone to effectively follow a face without any remote control. My purpose for exploring usages of Data Science and Artificial Intelligence is because I am a part of a district-wide non-profit known as Frisco Ignite, where I will be giving a speech to hundreds of middle/elementary schoolers across the district about technology. I decided to discuss the topic of drones to engage the young students into the fields of STEM early-on, and throughout my research of how drones are used today, I made discoveries of use-cases that I couldn’t even imagine.

From delivering medical supplies to tracking animals in ecosystems, drones are an essential part of humanity’s future. While exploring how to integrate Python’s OpenCV computer vision algorithms, I came up with a variety of Final Product ideas dealing with the drone. My primary idea is to utilize a drone’s camera to circle around any face it detects, and create a 3D representation of their facial features. Its purpose could be security in corporate buildings, or even just home-security to identify any potential threats. The drone’s easy maneuverability means that the human its analyzing is not required to move whatsoever; they can be minding their own business, and the drone will pick up the facial features, identifying the person. I’m excited to further research the topic.

"""

country_cities = {
        'title':title,
        'content':content
    }
with open(title.replace(' ','-').replace('\n','')+'.md','w') as f:
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