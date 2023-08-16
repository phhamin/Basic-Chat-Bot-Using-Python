import speech_recognition
import pyttsx3

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm hearing")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio,language='vi-VN')
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "I can't hear you"
	elif you == "Hello":
		robot_brain = "Hello Phương Hà"
	elif you == "I want to listen to music":
		robot_brain = "Which singer do you want to listen to?"
	elif you == "Sơn Tùng":
		robot_brain = "Is Making My Way song okay?"
	elif you == "OK":
		robot_brain = "I will play the song"
	else:
		robot_brain = "Thank you for talking with me"

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()