#This code is for MAC-OS.

import os
import pyttsx3
import re, uuid
import socket
from datetime import date
from datetime import datetime
import webbrowser

pyttsx3.speak("Welcome to the Menu")

	
while True :

	print()
	print("***************************************************")
	print()
	usrInput = str ( input("Enter your requirements : ") )
	print()

	# input is CONVERTED to lower case for simplifications 
	# such as, if CAPSLOCK is ON while entering input
	usrInput = usrInput.lower()

	#This BLOCK for OPENING GUI's and WEBSITES..
	if ("run" in usrInput) or ("open" in usrInput) or ("launch" in usrInput) or ("execute" in usrInput):
		
		#For opening Safari Browser
		if "safari" in usrInput:
			# "open -a Safari" is used in MAC to open safari using system module.
			os.system("open -a Safari")
			print("Safari Opened..")
			print()
			
		
		elif "photos" in usrInput:
			#For opening Photos in MAC
			os.system("open -a Photos")
			print("Photos Opened..")
			print()
			
		
		elif "text edit" in usrInput:
			#TextEdit is like text editor on MAC
			os.system("open -a TextEdit")
			print("Text Editor Opened..")
			print()
			
		
		elif "sublime" in usrInput:
			#Open SUBLIME Text
			os.system("open -a Sublime\\ Text")
			print("Sublime Opened..")
			print()
			
		#Opening a website for user, URL provided by user himself.
		elif ("website" in usrInput) or ("google" in usrInput):
			webbrowser.open("https://www.google.com", new=2)
			print("Google Opened..")
			print()
		
		elif ("website" in usrInput) or ("facebook" in usrInput):
			webbrowser.open("https://www.facebook.com", new=2)
			print("Facebook Opened..")
			print()

		elif ("website" in usrInput) or ("wikipedia" in usrInput):
			webbrowser.open("https://www.wikipedia.com", new=2)
			print("Wikipedia Opened..")
			print()

		elif "launchpad" in usrInput:
			#Running the Launchpad in MAC
			os.system("open -a launchpad")
			print("Launchpad Opened..")
			print()
			

		elif "siri" in usrInput:
			#Opening Siri..
			os.system("open -a Siri")
			print("Siri Opened..")
			print()


		elif ("audio player" in usrInput) or ("music" in usrInput):
			#Opening MUSIC Player , named as Music in MAC
			os.system("open -a Music")
			print("MUSIC Opened..")
			print()


		elif ("media player" in usrInput) or ("vlc" in usrInput) or ("video player" in usrInput):
			#Opening VLC Player
			os.system("open -a VLC")
			print()


		elif ("app store" in usrInput) :
			#Opening App Store of MAC
			os.system("open -a App\\ Store")
			print("App Store Opened..")
			print()
		
		#Opening  BLUETOOTH from MAC	
		elif ("bluetooth" in usrInput):
			os.system("open -a Bluetooth\\ File\\ Exchange")
			print("Bluetooth Opened..")
			print()

		#Opening Eclipse 
		elif "eclipse" in usrInput:
			os.system("open -a  Eclipse\\ Java")
			print("Eclipse Opened..")
			print()

		#Opening WEB CAM.. It is named as Photo Booth on MAC.
		elif ("camera" in usrInput) or ("photobooth" in usrInput) or ("web cam" in usrInput ):
			os.system("open -a Photo\\ Booth")
			print("Webcam Opened..")
			print()
		
			
		#Opening a file to write content for user. Predefined File 
		elif ("file" in usrInput):
			file1 = open('/Users/apple/Desktop/myfile.txt', 'w') 
			print("Enter content to write in a file: ")
			inp = input();
			file1.write(inp) 
			file1.close()
		
		#if there are spelling mistakes then..
		else:
			print()
			print("Whatever you have stated does'nt exist!!")
			print()
			print("Or you can check for SPELLING MISTAKES in your requirements..!!")
			print()
	
	#This BLOCK for WRITING to a file & READING from it..
	elif "read" in usrInput or "write" in usrInput:
		
		
		#Reading the contents of a file, file name should be provided by user.
		if ("file" in usrInput):
			try:
				file = open("/Users/apple/Desktop/myfile.txt",'r')
				print(file.read())
				file.close()
			except:
				print()
				print("File not present")
				print("Please enter the proper path.")
				print()


	#This BLOCK for showing IP Address , MAC Address , DATE & TIME.
	elif "show" in usrInput or "display" in usrInput or "print" in usrInput:
		
		#Display IP Address of your PC.
		if "ip" in usrInput or "ip address" in usrInput:
			try:
				hostname = socket.gethostname()
				IPaddress = socket.gethostbyname(hostname)
				print("Your IP Address is : ", IPaddress)
				print()
			except:
				print("Unable to load your IP Address right now, please try again later")
				print()
		
		#Display Mac Address of your PC.
		elif "macaddress" in usrInput or "mac address" in usrInput: 
			#Displaying Mac Address of your system.
			print()
			print("Your MAC ADDRESS is : ")
			print ( ':'.join( re.findall('..', '%012x' % uuid.getnode() )))
			print()
		
		#Display Current Date
		elif "date" in usrInput :
			today = date.today()
			print()
			print("Today's Date is : ",today)
			print()
		
		#Display current Time
		elif "time" in usrInput:
			now = datetime.now()
			currTime = now.strftime("%H:%M:%S")
			print()
			print("Current Time is : ",currTime)
			print()
		
		#if spelling mistakes, then print this..
		else:
			print()
			print("**Please check SPELLING MISTAKES**")
			print("for mac address , TYPE 'Mac Address'")
			print("for date , TYPE 'todays date'")
			print()

	#This BLOCK is to RECORD your AUDIO and Save it to folder.
	elif "record" in usrInput or "record my audio" in usrInput or "record me" in usrInput or "record voice" in usrInput:
		import sounddevice as sd
		from scipy.io.wavfile import write

		audioFile = input("Please enter file name to store your audio(EG: fileName.wav) -  ")
		fs = 44100
		#Manually records for 3 second. Below you can change the time..
		seconds = 3
		print("Recording for 3 seconds..")
		myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
		sd.wait()
		write(audioFile, fs, myrecording)

	
	#This BLOCK takes SCREENSHOT of the SCREEN on MAC-OS only..
	elif "take screenshot" in usrInput or ("screenshot" in usrInput):
		os.system("open -a Screenshot")

	#This BLOCK SENDS AND EMAIL....
	elif "compose email" in usrInput or "mail" in usrInput or "email" in usrInput:
		import smtplib 
		
		try:
			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls() 

			emailId = input("Enter your Email ID: ")
			pwd = input("Enter your password: ")
				
			s.login(emailId,pwd)

			message = input("Enter your content of mail: ")

			recieverEmailID = input("Enter reciever's email id : ")

			s.sendmail(emailId, recieverEmailID, message)
			s.quit()
		except:
			print()
			print("Error in sending mail...try again later ")
			print()

	#This BLOCK SEND an SMS to someone, Using TEXT-MAGIC API.
	elif ("send message" in usrInput) or ("message" in usrInput) or ("msg" in usrInput):
		from textmagic.rest import TextmagicRestClient
  
		try:
			# YOU need a TEXT MAGIC Account, sign-in for free..
			# I can't enter my credentials as it will get known..
			username = "your_own_textmagic_username"
			token = "your_own_api_key"
			
			client = TextmagicRestClient(username, token)
	  
			message = client.messages.create(phones="9990001001", text="Hello TextMagic")
		except:
			print()
			print("Enter your own username and token for sending the message")
			print()
	
	#This BLOCK to SHUT DOWN the PC...
	elif ("shut down" in usrInput):
		#You should be root
		try:
			os.system("shutdown -h now")
		except:
			print("You should be logged as root for shuting down the pc from Terminal")

	#This BLOCK to CLOSE our PROGRAM, ENDs WHILE loop
	elif ("exit" in usrInput) or ("quit" in usrInput) or ("stop" in usrInput) or ("close" in usrInput):
		pyttsx3.speak("Closing our program....")
		print("CLOSED.......")
		break;

	#Lastly, to check SPELLING MISTAKES in main command
	else:
		print()
		print("Whatever you have stated does'nt exist!!")
		print()
		print("Or you can check for SPELLING MISTAKES in your requirements..!!")
		print()
		print("")
	
	
	