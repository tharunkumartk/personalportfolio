from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Frisco Ignite, Drones, and Real World.
"""
content = """
The real world makes everything harder.

This week, I focused on preparing my presentation for Frisco Ignite. My group was in charge of the Technology part of STEAM, where we have to give a 15 minute presentation and demonstration to students across the district. We decided on utilizing Drones, particularly showing how it can be combined with Artificial Intelligence for mind-blowing applications. The presentation part was easy; the most difficult aspect was the demonstration, since I had to come up with a way to program the drone to run the Artificial Intelligence algorithm that follows the football around while showing the drone’s camera to the big screen. 

The day before the event, everything was finally working. However, on the day of the event, the drone's batteries malfunctioned and would not charge. As a result, the drone did not work. I had to code up an on-the-spot solution for the demo. I decided on saying that “Elmo (the drone’s nickname) got tired from transporting the goods across the stage (our previous demo)” and showing the Artificial Intelligence algorithm run using a basic camera. The kids loved it, and the presentation ended up being a success, but the last-minute failure really revealed to me how random the real world could be. I learned the importance of being prepared for anything because of Frisco Ignite, and I hope to utilize this skill in my coding.

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