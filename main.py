Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Yan-BINCAT 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


Yan-BINCAT
/
File-Sorter
1
🔖 Custom notification settings
Looking for a little more control? Now you can choose which types of activity you’d like to be notified about per repository.

00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Create main.py

 main
@Yan-BINCAT
Yan-BINCAT committed 10 hours ago 
0 parents commit d3619aeb75cb5b58058ffa6d97edfd79e4ebe7a3
Showing  with 35 additions and 0 deletions.
 35  main.py 
@@ -0,0 +1,35 @@
import os
from os import path
#from tkinter import*
#rsplit
esc = '\L'
esc = esc.strip('L')
os.system('cls')
main_directory = os.getcwd() + esc #Папка в которой надо посортировать файлы
print(os.path.abspath(__file__).rsplit(esc)[-1])
if os.path.exists(main_directory) == 0:
        os.mkdir(main_directory)

File_extensions = []
files = os.listdir(main_directory)
print(files)
files_n = 0;
for f in files:
    if path.splitext(f)[1].lstrip('.') != '' and str(f) != os.path.abspath(__file__).rsplit(esc)[-1]:
        files_n+=1
        dir_name = str(path.splitext(f)[1].lstrip('.')).upper()
        if os.path.exists(main_directory + dir_name) == 0:
            os.mkdir(main_directory + dir_name)

        dyrectory_from = main_directory
        dyrectory_from = dyrectory_from + esc + str(f)
        dyrectory_in =  main_directory + str(path.splitext(f)[1].lstrip('.').upper())
        dyrectory_in = dyrectory_in + esc + str(f)
        os.rename(dyrectory_from, dyrectory_in)
        print(files_n, " файлов было россортировано!")

    else:

        print("Фойлов для сортировки нету!")

input()
