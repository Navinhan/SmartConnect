from threading import *
try:
	from Tkinter import *
except ImportError:
	from tkinter import *
import time*

class CreateAccount(Frame, Thread):
	def __ini__(self, event):
	Thread.__init__(self, event)
	Frame.__init__(self, event)
	
	#Creating a Frame
	self.f = Frame(root, height=768, width=1360, bg="white")
