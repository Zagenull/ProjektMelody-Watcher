A program to watch if ProjektMelody is streaming on chaturbate.

Compiling:

 - Install Python 3.7.6 from [https://www.python.org/downloads/release/python-376/] along with the needed* modules using PIP (included in the default python installation) 
   You can install Python modules in CMD using the command {pip install (module name)}, check out the documentation at [https://pip.pypa.io/en/stable/quickstart/]

 - In order to compile, use the py_compile library, follow the directions on their website/documentation at [https://docs.python.org/3/library/py_compile.html]

Modules:
 - PyQt4
 - subprocess
 - requests
 - smtplib
 - webbrowser
 - pynput
 

Extra Notes: 
 - The program uses ALT+F4 in order to close whatever you're looking at. If the program ignores this command the code won't work as intended.
 - The program searches if Melody is online every 60 seconds. Change the (60) on line 20 to a different number before compiling if a quicker time is desired.
 - Have fun! 


Program By: @Zagethemage, inspired by @ProjektMelody on twitter.

