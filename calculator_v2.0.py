#///////////////////////////////////////////////////////////////////////// 
#TKalc Copyright (c) 2017 Copyright Inje Kim All Rights Reserved. 
#///////////////////////////////////////////////////////////////////////// 

from tkinter import * 

# Main Class 
class Main: 
	def __init__(self, master): 
		self.calc=Calculator() 

# Graphic_Interface class 
class Graphic_Interface: 
	def layout(self): 
		# values 
		self.button_width=3 # width of buttons 

		# display 
		self.display=Entry(justify="right", width=17) 
			#Entry : 간단한 텍스트(한 줄)을 입력받거나, 간단한 텍스트를 표시할 때 사용됨
			#justify : Entry위젯의 문자열에 대한 정렬방법
			#출처 : https://m.blog.naver.com/PostView.nhn?blogId=dudwo567890&logNo=130168372346&proxyReferer=https%3A%2F%2Fwww.google.com%2F
		self.display.grid(row=0, column=0, columnspan=3) #tkinter grid() Method : 위젯 배치

		# AC button 
		self.button_ac=Button( 
		text="AC", 
		width=self.button_width, 
		command=self.reset) 
		self.button_ac.grid(row=0, column=3) 

		# 7 button 
		self.button_7=Button( 
		text="7", 
		width=self.button_width, 
		command=lambda:self.add_to_display("7")) 
		self.button_7.grid(row=1, column=0) 

		# 8 button 
		self.button_8=Button( 
		text="8", 
		width=self.button_width, 
		command=lambda:self.add_to_display("8")) 
		self.button_8.grid(row=1, column=1) 

		# 9 button 
		self.button_9=Button( 
		text="9", 
		width=self.button_width, 
		command=lambda:self.add_to_display("9")) 
		self.button_9.grid(row=1, column=2) 

		# \ button 
		self.button_d=Button(
		text="/", 
		width=self.button_width, 
		command=lambda:self.pre_calculate("/")) 
		self.button_d.grid(row=1, column=3) 

		# 4 button 
		self.button_4=Button( 
		text="4", 
		width=self.button_width, 
		command=lambda:self.add_to_display("4")) 
		self.button_4.grid(row=2, column=0) 

		# 5 button 
		self.button_5=Button( 
		text="5", 
		width=self.button_width, 
		command=lambda:self.add_to_display("5")) 
		self.button_5.grid(row=2, column=1) 

		# 6 button 
		self.button_6=Button( 
		text="6", 
		width=self.button_width, 
		command=lambda:self.add_to_display("6")) 
		self.button_6.grid(row=2, column=2) 

		# * button 
		self.button_t=Button( 
		text="*", 
		width=self.button_width, 
		command=lambda:self.pre_calculate("*")) 
		self.button_t.grid(row=2, column=3) 

		# 1 button 
		self.button_1=Button( 
		text="1", 
		width=self.button_width, 
		command=lambda:self.add_to_display("1")) 
		self.button_1.grid(row=3, column=0) 

		# 2 button 
		self.button_2=Button( 
		text="2", 
		width=self.button_width, 
		command=lambda:self.add_to_display("2")) 
		self.button_2.grid(row=3, column=1) 

		# 3 button 
		self.button_3=Button( 
		text="3", 
		width=self.button_width, 
		command=lambda:self.add_to_display("3")) 
		self.button_3.grid(row=3, column=2) 

		# - button 
		self.button_m=Button( 
		text="-", 
		width=self.button_width, 
		command=lambda:self.pre_calculate("-")) 
		self.button_m.grid(row=3, column=3) 

		# 0 button 
		self.button_0=Button( 
		text="0", 
		width=self.button_width, 
		command=lambda:self.add_to_display("0")) 
		self.button_0.grid(row=4, column=0) 

		# . button 
		self.button_dot=Button( 
		text=".", 
		width=self.button_width, 
		command=lambda:self.add_to_display(".")) 
		self.button_dot.grid(row=4, column=1) 

		# = button 
		self.button_e=Button( 
		text="=", 
		width=self.button_width, 
		command=self.post_calculate) 
		self.button_e.grid(row=4, column=2) 

		# + button 
		self.button_p=Button( 
		text="+", 
		width=self.button_width, 
		command=lambda:self.pre_calculate("+")) 
		self.button_p.grid(row=4, column=3) 

# Calculator class 
class Calculator(Graphic_Interface): #상속받음
	def __init__(self): 
		self.layout() 
		self.refresh_display('0') 

		# values 
		self.first=1 # indecates first input 
		self.symbol="" # current calculating symbol 

	# clear display 
	def clear_display(self): 
		self.display.delete(0, 'end') # clear display 

	# replace text on display 
	def refresh_display(self, text): 
		self.clear_display() # clear display 
		self.display.insert(0, text) # add text to display 

	# reset display 
	def reset(self): 
		if self.display.get()=="0": # AC 
			self.symbol="" 
		self.refresh_display("0") # replace text in display to 0
		self.button_ac["text"]="AC" # replace text in button_ac to AC 

	# add to existing text in display
	def add_to_display(self, text): 			
		current=self.display.get() # get text from display 
		if current=="0" and text!=".": # remove 0 when adding numbers
			current="" 
		if "." in current and text==".": # prevent more then one dots 
			text="" 
		if self.first==0: # initial input 
			self.first=1 
			self.refresh_display(text) 
		else: # after the initial input 
			self.refresh_display(current+text)
		self.button_ac["text"]="C" 

	# after pressing symbol keys 
	def pre_calculate(self, symbol): 
		if self.symbol!="": # continuous calculation 
			self.pre=self.post_calculate() 
		else: # initial calculation 
			self.pre=float(self.display.get()) 
		self.first=0 
		self.symbol = symbol 

	# after pressing equals key 
	def post_calculate(self): 
		if self.symbol!="": 
			self.post=float(self.display.get()) 
			result = { # calculation cases 
			'/': lambda : self.pre/self.post, 
			'*': lambda : self.pre*self.post, 
			'+': lambda : self.pre+self.post, 
			'-': lambda : self.pre-self.post 
			}[self.symbol]() 
			if result%1==0: # remove .0 
				result=int(result) 
			self.refresh_display(result) 
			self.symbol="" 
			self.first=0 # reverts indicator 
			return result 

# Initialize Tkinter 
root = Tk() 
root.title("TKalc ver 1.2") 
root.configure(padx=5, pady=5) 
Main(root) 
root.mainloop()
