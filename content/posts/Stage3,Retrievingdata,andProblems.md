---
title: Stage 3, Retrieving data, and Problems.
description: This week, I focused on finishing stage 3 of my Final Product, which involved finding and retrieving...
date: 2021-04-22
draft: false
slug: /blog/Stage-3,-Retrieving-data,-and-Problems.
tags: 
---
This week, I focused on finishing stage 3 of my Final Product, which involved finding and retrieving the appropriate data for my Final Product. This process was by far the longest because of my unfamiliarity with the JSON file format. I had to learn how to easily and effectively read from and write into JSON files, because most of the data found on the internet came in the JSON format. In addition, I had to learn how to use the various Python modules for web scraping required to obtain the data, since the actual APIs were extremely outdated. After several hours of research and coding, I was able to retrieve and write all of the data required into several csv files. The reason I wrote them into csv files was so that I could easily read them whenever I needed (using the Pandas read_csv() function). 

After obtaining the data, I had to create the carbon output functions, as well as the minimization functions for each energy source. I also had to come up with a logical method of recording energy consumption at each location. I ended up having to figure out the population density at each county, multiply it by my sub-regions to get the population in the sub-region, and multiply the population by the per-capita energy consumption in Texas. However, once I ran my code to test it out, I noticed that my program’s output did not seem accurate. I realized that my actual carbon output values were inaccurate, due to the lack of information available online. But, I managed to come up with different data from a 60 page study by a research paper published by Princeton University. In the end, the output looked somewhat accurate, so I decided to move onto Stage 4.

