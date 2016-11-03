import nxppy
import time



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
def ReadMessage():
	ls = []
	for y in xrange(30):
		try:
			a = y+6
			time.sleep(.05)
			z = mifare.read_block(a)
			ls.append(z)
		except nxppy.ReadError:
			pass
		
	y = ''.join(ls)
	print y	

mifare = nxppy.Mifare()

while 1:
	try:
		uid = mifare.select()
		print uid
		break
	except nxppy.SelectError:
		pass


WriteMessage("Bradley, you are cool")

time.sleep(1)

ReadMessage()


