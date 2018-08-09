from Tkinter import *
from pyDes import *
root=Tk()
root.wm_title("ENCRYPTION")
label_1=Label(root,text="Enter Plain Text")
label_1.grid(row=0,sticky=E)
entry_1=Entry(root)
entry_1.grid(row=0,column=1)
a=[]
b=[]
c=[]
def clear(): 
	msg = Message(root, text ="                          ",justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=13)
def clear1():   
	msg = Message(root, text ="                    ",justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=13,column=2)
for i in range(15):
	a.append(".")
	b.append(".")   
	c.append(".")
def plaintext(event):
	global str1
	str1=entry_1.get()
	#str1=raw_input("enter the plain text: ")	
button_1= Button(root,text="ACCEPT INPUT")
button_1.grid(row=3)
button_1.bind("<Button-1>",plaintext)
def rf(event):
	i=0
	global str1
	#print str1
	while(i<len(str1)):
		if(i<len(str1)):
			a[i]=str1[i]
			i=i+1
		if(i<len(str1)):
			b[i]=str1[i]
			i=i+1
		if(i<len(str1)):
			c[i]=str1[i]
			i=i+1
		if(i<len(str1)):
			b[i]=str1[i]
			i=i+1
	global result
	result=""
	for i in range(15):
		if(a[i]!='.'):
			result=result+a[i]
	for i in range(15):
		if(b[i]!='.'):
			result=result+b[i]
	for i in range(15):
		if(c[i]!='.'):
			result=result+c[i]
	print result
	button_7.config(state = DISABLED)
	button_9.config(state = DISABLED)
	button_10.config(state = DISABLED)
button_2= Button(root,text="RAILFENCE")
button_2.grid(row=5)
button_2.bind("<Button-1>",rf)
def decryptrf(event):
	c1=[]
	c2=[]
	c3=[]
	k=0
	global orig
	global str2
	orig=[]
	l=len(result)
	for i in range(l):
		orig.append('*')
	i=0
	while(i<l):
		c1.append(i)
		i=i+4
	i=1
	while(i<l):
		c2.append(i)
		i=i+2
	i=2
	while(i<l):
		c3.append(i)
		i=i+4
	for j in range(len(c1)):
		orig[int(c1[j])]=result[k]
		k+=1
	
	for j in range(len(c2)):
		orig[int(c2[j])]=result[k]
		k+=1
		
	for j in range(len(c3)):
		orig[int(c3[j])]=result[k]
		k+=1
	str2=""
	for j in range(len(orig)):
		str2+=orig[j]
	
	print "decrypted is: ",str2
	button_7.config(state = ACTIVE)
	button_9.config(state = ACTIVE)
	button_10.config(state = ACTIVE)
button_3= Button(root,text="DECRYPT RAILFENCE")
button_3.grid(row=5,column=1)
button_3.bind("<Button-1>",decryptrf)
def showencrypted(event):
	clear()
	global result
	msg = Message(root, text = result,justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=13)
button_4= Button(root,text="SHOW ENCRYPTED")
button_4.grid(row=11)
button_4.bind("<Button-1>",showencrypted)
def showdecrypted(event):
	clear1()
	global str2
	msg = Message(root, text = str2,justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=13,column=2)
button_5= Button(root,text="SHOW DECRYPTED")
button_5.grid(row=11,column=2)
button_5.bind("<Button-1>",showdecrypted)

##########
def playfair(event):
	global str1,result
	result=""
	a=[['k','e','y','a','b'],['c','d','f','g','h'],['i','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','z']]
	for i in range(len(str1)):
		if(str1[i]=='j'):
			str1=str1+'l'
		for j in range(5):
			for k in range(5):
				if(a[j][k]==str1[i]):
					if(k!=4):
						result=result+a[j][k+1];
					else:
						result=result+a[j][0]
	button_3.config(state = DISABLED)
	button_9.config(state = DISABLED)
	button_10.config(state = DISABLED)
	
button_6= Button(root,text="PLAYFAIR")
button_6.grid(row=6)
button_6.bind("<Button-1>",playfair)
def decplayfair(event):
	global result, str2
	str2=""
	a=[['k','e','y','a','b'],['c','d','f','g','h'],['i','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','z']]
	for i in range(len(result)):
		if(result[i]=='j'):
			str2=str2+'l'
		for j in range(5):
			for k in range(5):
				if(a[j][k]==result[i]):
					if(k!=0):
						str2=str2+a[j][k-1];
					else:
						str2=str2+a[j][4]
	button_3.config(state = ACTIVE)
	button_9.config(state = ACTIVE)
	button_10.config(state = ACTIVE)
button_7= Button(root,text="DECRYPT PLAYFAIR")
button_7.grid(row=6,column=1)
button_7.bind("<Button-1>",decplayfair)
	
#########
####
def ceaser(event):
	global str1, result
	result=""
	for i in range(len(str1)):
		result=result+chr((ord(str1[i])+4)%256)
	button_3.config(state = DISABLED)
	button_7.config(state = DISABLED)
	button_10.config(state = DISABLED)
button_8= Button(root,text="CEASER")
button_8.grid(row=8)
button_8.bind("<Button-1>",ceaser)
def decceaser(event):
	global str2,result
	str2=""
	for i in range(len(result)):
		str2=str2+chr((ord(result[i])-4)%256)
	button_3.config(state = ACTIVE)
	button_7.config(state = ACTIVE)
	button_10.config(state = ACTIVE)
button_9= Button(root,text="DECRYPT CEASER")
button_9.grid(row=8,column=1)
button_9.bind("<Button-1>",decceaser)
####
def des1(event):
	global str1,result
	result=""
	k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
	result=k.encrypt(str1)
	result="%r"%result
	#print result
	button_3.config(state = DISABLED)
	button_7.config(state = DISABLED)
	button_9.config(state = DISABLED)
button_10= Button(root,text="DES")
button_10.grid(row=9)
button_10.bind("<Button-1>",des1)
def decdes(event):
	global str2,result,str1
	str2=""
	k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
	result=k.encrypt(str1)
	#print result
	str2=k.decrypt(result)
	button_3.config(state = ACTIVE)
	button_7.config(state = ACTIVE)
	button_9.config(state = ACTIVE)
button_10= Button(root,text=" DECRYPT DES")
button_10.grid(row=9,column=1)
button_10.bind("<Button-1>",decdes)
root.mainloop()
