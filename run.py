import pyspeedtest
import time
import sys

st = pyspeedtest.SpeedTest()

if len(sys.argv) == 1:
	print('speedtest in a loop. usage: python run.py <name-of-setup>')
	sys.exit(0)

while True:
	print('{},{:.0f},{},{},{}'.format(sys.argv[1],time.time(),st.ping(),st.download(),st.upload()))
	time.sleep(30)	
