import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('0.0.0.0', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='hiamy.txt'
    f = open(filename,'rb')
    l = f.read()
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read()
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()