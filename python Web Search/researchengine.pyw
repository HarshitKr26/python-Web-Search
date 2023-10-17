"""
#from cProfile import label
#from html import entities
from tkinter import *
#from tkinter import *font,
from tkinter import Entry
import webbrowser
from selenium import webdriver
root = Tk()
root.title("search ")


def search():
        url=enter_box.get()
        webbrowser.open(url)
        browser1 = webdriver.Chrome('chromedriver')
        for i in range(1):
            matched_elements = browser1.get("https://www.google.com/search?q=" +
                                     url + "&start=" + str(i))


label=Label(root,
               text = "enter url ", 
               font = ("arial",15,"bold"))
label.grid(row=0,column=0)
enter_box = Entry(root, width = 35)
enter_box.grid(row=0,column=1)
btn= Button(root,
text ="Search ",
bg="blue",
fg= "white",
font = ("arial", 15,"bold"))
btn.grid(row=1, column=0)
root.mainloop()
"""



import sys
import os
from tkinter import *
import webbrowser


root=Tk()
root.title("Quick Search")
#root.minsize(100, 500)
#root.maxsize(400, 50)
def voicesearch():
 os.system('D:\\python\\AI1\\fastest.py')
def search(self):
    url1= ".com"
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open('http://docs.python.org/')

   
    #url=entry.get().open(url)
    url=entry.get()
    #url +=url1
    webbrowser.open("https://en.wikipedia.org/wiki/"+url)
    webbrowser.open("https://www.youtube.com/results?search_query="+url)
    webbrowser.open("https://www.google.com/search?q="+url)

lable1=Label(root,text="Search Anyting:",font=("arial",15,"bold"))
lable1.grid(row=0,column=0)
entry=Entry(root,width=35)
entry.grid(row=0,column=1)
btn=Button(root,text="Search",command=search,bg="black",fg="white",font=("arial",14,"bold"))
btn.grid(row=1,column=0,columnspan=4,pady=10)
btn2=Button(root,text="  🎙️",command=voicesearch,bg="white",fg="black",font=("arial",14,"bold"))
btn2.grid(row=1,column=1,columnspan=1,pady=8)
entry.bind('<Return>', search)
root.mainloop()