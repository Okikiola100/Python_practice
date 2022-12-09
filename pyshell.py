#!/bin/python3
"""
Author: Oladapo Okikiola

Description: Code that 
1. get the current working directory
2. change the working directory
3. create a file and cd into the file
4. create a text file and write into it
"""
import os  # using the os python shell
print(os.getcwd())  # get the current working directory
os.mkdir('my_folder')  # make the folder "my_folder"
os.chdir("/storage/emulated/0/my_github_repo/Python_practice/my_folder")  # change the cwd to the my_folder dir
my_file = open("intro.txt", "w")  # open/create the intro.txt file
my_file.write("Its vitality coder\nFollow me at:\nHashnode: Okikiola100.hashnode.dev\nGithub: github.com/Okikiola100/\nLinkdein: www.linkdein.com/in/oladapo-okikiola-eniola\nTwitter: https://www.twitter.com/oladapookiki1\nGmail: okikiolaoladapo10@gmail.com\nWhatsapp: https://api.whatsapp.com/send/?phone=%2B2348168364293&text&type=phone_number&app_absent=Hi\n")  # writting into the text file
print("done")
my_file.close()
