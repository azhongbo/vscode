#!/usr/bin/python3
import os

user = input("user: ")

str1 = f"git config --global user.email  {user}\@gmail.com"
str2 = f"git config --global {user}"
os.system(str1);
os.system(str2);
os.system("git add *");
os.system("git commit -m *");
os.system("git push origin master");
