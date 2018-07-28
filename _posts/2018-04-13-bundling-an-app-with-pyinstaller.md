---
layout: single
comments: true
title: Bundling PyQt5 with PyInstaller
date: 2017-11-13 23:59:59
tags: python PyQt
---


Bundling with PyInstaller  
1) Create a virtual enviorment for your app   

{% highlight bash %}
cd my_app_folder
pip install virtualenv
virtualenv my_app_env
source my_app_env/bin/activate
{% endhighlight %}
Now your terminal should have (my_app_env) Computer_Name Current_Directory username$
3) install all the necessary packages for your app

{% highlight bash %}
pip install PyQt5
pip install qdarkstyle
{% endhighlight %}
3)Check to see your program works in the virtual enviroment

{% highlight bash %}
python my_app.py
{% endhighlight %}
4) Call `pyinstaller` any specific paths for your app (ie. PyQt5)

{% highlight bash %}
pyinstaller --paths ../PyQt5/Lib/site-packages/PyQt5/Qt/bin -w my_app.py
{% endhighlight %}
5) If you have any data files that need to be bundled with the app then this alone wont work. Modify the `my_app.spec` file to include the necessary data files. [Reference](http://helloworldbookblog.com/distributing-python-programs-part-2-the-harder-stuff/)
{% highlight python %}
# -*- mode: python -*-
block_cipher = None
a = Analysis(['my_app.py'],
             pathex=['../PyQt5/Lib/site-packages/PyQt5/Qt/bin', '/path/to/folder/containing/my_app'],
             binaries=[],
             datas=[('additional_file.py', '/path/to/additional_file.py', 'DATA')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
ui_file =  [('my_app_ui.ui', '/path/to/ui/file/my_app_ui.ui', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='AppName',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='aduro.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas + ui_file,
               strip=False,
               upx=True,
               name='AppName')
app = BUNDLE(coll,
             name='AppName.app',
             icon='./icon.icns',
             bundle_identifier=None)
{% endhighlight %}
6) Call `pyinstaller` with the spec file
    a. `pyinstaller AppName.spec`

8) Test your app.

7) A couple more tricks for single-file EXE’s
If you want to turn programs like LunarLander or TempConv into single-file executables, there’s one more thing you need to know about, and some changes you need to make to the code.

When PyInstaller makes a single-file executable, what it’s really making is a self-extracting zip file with all the necessary supporting files inside it.  Graphics, font files, .UI files, etc.  When it runs, that gets unzipped to a temporary folder and run from there.  When the program stops, the temporary folder gets deleted.  It’s all transparent to the user.  This means two things:

A single-file executable will usually take a little longer to start up, because it has to extract the zip file first.
The python code needs to know where that temp folder is, so it can find the files it needs (fonts, graphics, etc.).
The temporary folder location that PyInstaller uses can be found with `sys._MEIPASS`.  So, to make sure your program can find what it needs, you can use something like this:

{% highlight python %}
if hasattr(sys, '_MEIPASS'):
    ui_path = os.path.join(sys._MEIPASS, "tempconv_menu.ui")
else:
    ui_path = "tempconv_menu.ui"

form_class = uic.loadUiType(ui_path)[0]     # Load the UI
{% endhighlight %}