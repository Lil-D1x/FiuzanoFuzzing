#!/usr/bin/python
import socket,time,sys

if len (sys.argv) != 2:
	print "FUZZING - Lil D1x"
	print "Use: python fiuzanofuzzing.py IP"
	sys.exit()

s = socket.socket(socket.AF_INET, sokcet.SOCK_STREAM)
s.connect((sys.argv[1],21))
time.sleep (2)
r = s.recv(4096)
s.send("USER anonymous\r\n")
r = s.recv(1024)
s.send("PASS anonymous\r\n")
r = s.recv(1024)

buffer=["A"]
count=100
while len(buffer) <= 25:
	buffer.append("A"*count)
	count=count+200

commands=["CWD","LIST","PWD"]

for command in commands:
	for string in buffer:
		print "Fuzzing Command %s with %s bytes"%(command,len(string))
		s.send("%s %s\r\n"%(command,string))
		r = s.recv(1024)
