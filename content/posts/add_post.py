from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Final Product, Presentation, and Display Board.
"""
content = """
I feel like a kid again.

This week, I have been planning and completing my display board for the Winter Symposium. The name is kind of ironic, considering that the weather feels like its spring. I haven’t created any arts and crafts in nearly 3 years, particularly due to COVID, so planning out and creating such a display board brings a sense of nostalgia. I’m trying out a different style from the default “cut out letters and paste on board; I’m using the cutouts of the letters so that the actual letters end up being the actual board. I also used the same strategy for a variety of other shapes. As of right now, the display board is completed, but there is one small issue: my title is too long for the board. My solution for this issue is to just keep AI, and put my name next to it. Although this solution is a little bit lame, it gets the job done, so I’m not too disappointed. 

I also gave my 15-20 minute presentation this week, and I am somewhat proud of it. I did not rehearse the speech much, because I wanted to practice speaking on the spot, and I ended up doing exceptionally well in the speech. I didn’t talk too fast, nor did I fidget around like I usually do. The main component that I have left to add is a little bit of humor to the actual presentation. I can’t wait for the Winter Showcase, because I want to test out my Original Work on more people than just my friends.

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