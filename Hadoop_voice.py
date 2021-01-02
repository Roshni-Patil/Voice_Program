import os
import pyttsx3
import speech_recognition as sr
import xml.etree.ElementTree as obj


def updateXML(filename):
		tree = obj.ElementTree(file=filename)
		root = tree.getroot()

		for value in root.iter("value"):
			port = input("Enter port : ")
			ip = input("Enter ip : ")
			value.text = "hdfs://{}:{}".format(ip, port)

		tree = obj.ElementTree(root)
		with open(filename, "wb")as fileupdate:
			tree.write(fileupdate)


def design1():
		os.system(" cls ")
		os.system(" tput bold ")
		print("=============================================================================================================================================================")
		os.system(" tput  setaf 1 ")
		print("\t\t\t\t----------------->Your welcome in this Hadoop Automation Menu Program<----------------\t\t")
		pyttsx3.speak("Your welcome in this Hadoop Automation Menu Program")
		os.system(" tput  setaf 3 ")
		print("=============================================================================================================================================================\n")
		os.system(" tput setaf 77 ")


def design2():
		os.system(" tput setaf 68 ")
		print("HADOOP SERVICES ")
		print(" ------------------------------------------------\n")
		os.system(" tput setaf 78 ")


def hadoop():
		print("""
		\t--------> Install java
		\t--------> Install hadoop
		\t--------> Configure data node
		\t--------> Configure master node
		\t--------> Start name node
		\t--------> Stop name node
		\t--------> Start data node
		\t--------> Stop data node
		\t--------> Hadoop Admin report



	""")


design1()
design2()
pyttsx3.speak("Are you sure that you have rpm file of hadoop and java ")
a = input(
	"Are you sure that you have rpm file of hadoop and java [yes/no] :  ")
b = 'yes'
if a != b:
		os.system("tput setaf 9")
		print("First get that file : ")
		pyttsx3.speak("First get that file :")
		exit()
hadoop()


pyttsx3.speak("Tell me your requirements...........I 'm listening to you ")

while True:
	design2()
	hadoop()
	r = sr.Recognizer()

	with sr.Microphone() as source:

		audio = r.listen(source)
		pyttsx3.speak('i got it... please wait..!!')
	try:
		ch = r.recognize_google(audio)
		# print(ch)
		ch = ch.lower()

	except Exception as e:
		print(e)
		print('Say that again please...\n')
		pyttsx3.speak('Say that again please...')

	if ("Install java" in ch):
		os.system("rpm -ivh jdk-8u171-linux-x64.rpm")

	elif ("Install hadoop" in ch ):
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")

	elif("Configure datanode " in ch):
		pyttsx3.speak("I am going to configure datanode")
		os.system("rm -rf /dn")
		os.system("mkdir /dn")
		os.system("cd /etc/hadoop")
		os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/dn</value>\n</property>\n</configuration> ' > /etc/hadoop/hdfs-site.xml")
		os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://IP:Port</value>\n</property>\n</configuration> ' > /etc/hadoop/core-site.xml")
		updateXML("/etc/hadoop/core-site.xml")

	elif("Configure NameNode" in ch):
		pyttsx3.speak("I am going to configure namenode")
		os.system("mkdir /nn")
		os.system("cd /etc/hadoop")
		os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration> ' > /etc/hadoop/hdfs-site.xml")
		os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://IP:Port</value>\n</property>\n</configuration> ' > /etc/hadoop/core-site.xml")
		updateXML("/etc/hadoop/core-site.xml")

	elif("Start namenode " in ch):
		os.system("hadoop namenode -format")
		os.system("hadoop-daemon.sh start namenode")
		os.system("jps")
		pyttsx3.speak("NameNode Started")

	elif ("Stop namenode " in ch):
		os.system("hadoop-daemon.sh stop namenode")
		os.system("jps")
		pyttsx3.speak("Namenode Stopped")
					
	elif ("Start datnode " in ch ):
		os.system("hadoop-daemon.sh start datanode ")
		os.system("jps")
		pyttsx3.speak("NameNode Started")
	
	elif("Stop datanode " in ch ):
		os.system("hadoop-daemon.sh stop datanode ")
		os.system("jps")
		pyttsx3.speak("DataNode Started")        	
	
	elif("hadoop report " in ch ):
		os.system("hadoop dfsadmin -report")
		pyttsx3.speak("Here is your hadoop admin report")
	pyttsx3.speak("Press enter to continue")
	input()
	pyttsx3.speak("Tell me ur next requirement")