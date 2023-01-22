import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:5004')


data = 'Dupsko'

print('Sending data: "%s"' %(data))
resp = s.Server.store(data)

print('Response: "%s"' %(resp))
