---
author: nickzanobini
comments: true
date: 2017-02-22 04:06:21+00:00
layout: post
link: https://nickzanobini.wordpress.com/2017/02/22/auto-generating-a-requests-txt-from-a-python-file/
slug: auto-generating-a-requests-txt-from-a-python-file
title: Auto Generating a requests.txt from a Python File
wordpress_id: 705
---

If you ever wondered how to get a requirements.txt from a folder containing Python files, there's an easy solution.
[code language="bash" light="true"]
pip install pipreqs
pipreqs path_to_python_project
[/code]
There you go. You will have a requirements.txt that will encompass the files in your folder.
