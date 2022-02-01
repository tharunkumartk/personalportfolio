---
title: Stage 4, Mapping, and Grind time.
description: My Final Product was due this week, but due to the carbon dioxide value issue from the last blog pos...
date: 2021-04-22
draft: false
slug: /blog/Stage-4,-Mapping,-and-Grind-time.
tags: 
---
My Final Product was due this week, but due to the carbon dioxide value issue from the last blog post, I am forced to turn in my Final Product a couple days late. That means it’s time to grind.

My final step was to learn how the Plotly Express module works in Python, and how to convert my several lists of output into a mappable format. In order to this, I had to export the data into a .geojson format, so that Plotly can read it. It took me a while to understand how the .geojson format works, but I think I have a solid grasp of it now. It is essentially a JSON file with the following attributes: a list of feature objects, which each have the following attributes: Geometry, ID, and Properties. I had to convert my lists into a set of dictionaries (a friend of mine in college advised me in this area), and export the dictionary into JSON file using the json module. 

After this, I used the Plotly module to read the JSON file, along with the specific colors for each value (red for wind, blue for solar, etc). I created a GeoMapper object, and exported this object into an HTML file with the actual map. Ultimately, the map turned out looking good; the major components of the map include wind power and solar power, with small areas of natural gas and water turbines. I am quite pleased with how the project turned out.

