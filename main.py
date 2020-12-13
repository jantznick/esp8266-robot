# Main file run on micropython startup
# Used to download the /src folder from this repo and run robot instructions
# A faux CI/CD platform so once the robot is initialized it will always have the latest updates

import socket
import ujson as json
import network

r = open('config.json','r')
config = json.load(r)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
	print('connecting to network...')
	wlan.connect(config['wifi-name'], config['wifi-password'])
	while not wlan.isconnected():
		pass
print('network config:', wlan.ifconfig())

_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
while True:
	data = s.recv(100)
	if data:
		print(str(data, 'utf8'), end='')
	else:
		break
s.close()