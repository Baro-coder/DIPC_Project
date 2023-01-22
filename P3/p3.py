#!/usr/bin/python

# P3/p3.py

# ************************************************
# ****************** MODULES *********************
import sys
import socket
import xmlrpc.client


# ************************************************
# ****************** GLOBALS *********************
# TCP Server address
HOST = "127.0.0.1"
PORT = 5005

# Consts
BUFFER_SIZE = 512
FORMAT = 'utf-8'
RESP_MSG = 'Forwarded'.encode(FORMAT)

# *************************************************
# ***************** MAIN DRIVE ********************
def main():
    # Redirect STDERR to file
    sys.stderr = open('/var/log/ppr_p3_py.err.log', 'w')

    # XML-RPC Client
    xml_rpc_client = xmlrpc.client.ServerProxy('http://localhost:5004')

    # Socket
    global sock
    #   * Create
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #   * Bind
    sock.bind((HOST, PORT))
    sock.listen()

    # Listening
    print('P3: TCP Server is listening at %s:%d\n' %(HOST, PORT))
    while True:
        conn, addr = sock.accept()
        # Connection
        with conn:
            # Session
            while True:
                # Receive data
                data = conn.recv(BUFFER_SIZE)
                # If there is no data
                if not data:
                    break

                # Decode data
                data = data.decode(FORMAT)
                
                # Write received bytes count to STDERR
                print(len(data), file=sys.stderr)

                # Forward to XML-RPC Java Server
                xml_rpc_client.Server.store(data)
                
                # Send response
                conn.sendall(RESP_MSG)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('-- Manually interrupted --')

    except Exception as e:
        print('-- Unexpected Exception --')
        print(type(e))
        print(e)
    
    finally:
        sock.close()
