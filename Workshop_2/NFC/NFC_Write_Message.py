import nxppy
import time
import sys

def WriteMessage(msg):
	msgl=[]
	msgl.append(msg)
	if len(msg)%4 != 0:
		
		o = len(msg)%4
		for g in xrange(5-o):
			msgl.append(' ')
	msg = ''.join(msgl)
	for l in xrange(30):
		try:
			time.sleep(.05)
			mifare.write_block(l+6,'    ')
		except nxppy.WriteError:
			pass
	for y in xrange(20):

		buff = msg[y*4:(y+1)*4]
		try:
			a = y + 6
			time.sleep(.05)
			mifare.write_block(a,buff)
		except nxppy.WriteError:
			pass

mifare = nxppy.Mifare()

print "Enter Message:"

Message = raw_input('>')

while 1:
	print "Place tag to write on"
	while 1:
		try:
			uid = mifare.select()
			break
		except nxppy.SelectError:
			pass
	break

WriteMessage(Message)



