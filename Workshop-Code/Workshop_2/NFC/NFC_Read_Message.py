# Language: Python
# File name: NFC_Read_Message.py
# Description: this code will wait for a scan, and will terminate after reading
#              a card and printing its contents
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

while True:
	try:
		uid = mifare.select()
		break
	except nxppy.SelectError:
		pass


ReadMessage()
