from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
title = """
Final Product, Google Colab, and Persevering.
"""
content = """
The most important step in innovation is perseverance.

This week, I focused on bringing my Final Product to life, but I found several issues. Firstly, the Artificial Intelligence algorithms that I planned on using required a tool known as CUDA. This tool operates on NVIDIA’s Graphical Processing Unit, which is built into some high-end computers, but definitely not either of mine. The reason that CUDA is used is because of its optimization of GPU cores to quickly compute graphical calculations, such as the ones required to map a 2D picture to a 3D model. 

My first attempt to circumvent this problem is to utilize a VM (Virtual Machine). This uses the local system resources to create a separate virtual system that modulates the required components. However, since the CUDA tool required specific CUDA processors only found on NVIDIA GPUs, this plan did not work. However, I found a virtual coder called Google Colab, which offers unlimited virtual machines that run off of NVIDIA GPUs. The only drawback to utilizing Google Colab is the large amount of set-up time required to just work on the project. However, with this tool, I will be able to complete my Final Product before its due date. 

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