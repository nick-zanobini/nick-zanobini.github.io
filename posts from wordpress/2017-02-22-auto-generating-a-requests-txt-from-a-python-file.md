---
layout: post
title: Auto Generating a requests.txt from a Python File
date: 2017-02-22 04:06
author: nickzanobini
comments: true
categories: [Uncategorized]
---
If you ever wondered how to get a requirements.txt from a folder containing Python files, there's an easy solution.
[code language="bash" light="true"]
pip install pipreqs
pipreqs path_to_python_project
[/code]
There you go. You will have a requirements.txt that will encompass the files in your folder.
