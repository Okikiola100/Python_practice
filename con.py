#!/bin/python
# get the python shell
import os
# using the os python shell
print(os.getcwd())  # get the current working directory
os.mkdir('acmd')  # make the folder "acmd"
os.chdir("/storage/emulated/0/my_github_repo/Python_practice/acmd")  # change the cwd to the acmd dir
ap = open("pyshf.txt", "w")  # open/create  the pyshf.txt file
ap.write("Its vitality coder")  # write into the file
print("done")
ap.close()
