---
title: New Discovery, Original Work, and Interviews.
description: I’m almost done.

Last week, I began constructing the Neural Network for my Original Work, but quick...
date: 2021-12-04
draft: false
slug: /blog/New-Discovery,-Original-Work,-and-Interviews.
tags: 
---
I’m almost done.

Last week, I began constructing the Neural Network for my Original Work, but quickly I realized an issue with my logic: I had found and stored depression text data, along with their respective tonal scores, but I did not have a non-depressive text for the Neural Network to compare with. Undoubtedly, I will continue using Reddit, due to its large number of posts and users, but the issue is figuring out the best subreddit to use for this data. I am planning on sifting through positive stories in a Reddit where real life people tell stories about their life, and filtering the positive stories out utilizing the same tonal arrangement as I did for the depressive stories.

In addition, I realized that there are not many methods to determine key words in a text, but I managed to find one. It utilizes a TF-IDF algorithm, where all of the words across all of the documents are looked at, and the most common words in both lexical spelling and literal meaning are extracted. I still have to implement the “literal meaning” functionality, but the lexical spelling methodology works perfectly fine right now. The Neural Network will require these scores in order to sort new texts between depressive and non-depressive. In addition, I do not think I will be able to utilize the program to determine other mental illnesses, because after research, I realized that there is a very limited amount of people with mental disorders that post on Reddit (Schizophrenia, Autism, etc.). I think I will just have to perfect this depression algorithm, which by itself is an incredible feat.

