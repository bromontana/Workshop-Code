import nxppy
import time

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
		break
	except nxppy.SelectError:
		pass


ReadMessage()


