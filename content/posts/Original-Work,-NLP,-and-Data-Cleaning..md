---
title: Original Work, NLP, and Data Cleaning.
description: It’s finally coming together. 

I began actually putting my Original Work together, starting with co...
date: 2021-11-29
draft: false
slug: /blog/Original-Work,-NLP,-and-Data-Cleaning.
tags: 
---
It’s finally coming together. 

I began actually putting my Original Work together, starting with collecting the training data required for the project. My plan is to utilize text data found on subreddits about mental disorders as training data for a Machine Learning Model that is able to diagnose neurological illnesses through Natural Language Processing of text. This week I utilized the Reddit API, Python’s NLTK module, and Python’s scikit-learn module in order to obtain the key words located throughout conversations regarding people’s depressions. 

I first had to actually figure out which subreddits to utilize and what type of posts to search for. I used the NLTK module in order to determine the general tone of each of the posts, and since most of these posts are about depression, there is a high probability that, if it has a negative tone, the post is about a person’s own depression. After that, I used scikit-learn to obtain the keywords across all of the depressive posts, and created a function that returns all of the relevant words in an input sentence.

The plan going forward is to utilize this data to construct a neural network with five nodes: four nodes about tone, and the last one about how similar in meaning that the key words of the input sentence are to the meaning of the keywords of the training data. This neural network will end up being my Original Work, and I am excited to say that I am finally back on track to completing it on time.

