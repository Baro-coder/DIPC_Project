#!/usr/bin/python

# P3/p3.py

# ************************************************
# ****************** MODULES *********************
import sys
import socket
import xmlrpc.client
from time import sleep

# ************************************************
# ****************** GLOBALS *********************
# TCP Server address
HOST = "127.0.0.1"
PORT = 5003

# Consts
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
RESP_MSG = 'Forwarded'.encode('utf-8')
CONN_ERR_MAX = 15
CONN_ERR_DELAY = 2

# *************************************************
# ***************** MAIN DRIVE ********************
def main():
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
                conn_err_counter = 0

                # Receive data
                data = conn.recv(BUFFER_SIZE)
                # If there is no data
                if not data:
                    break
                
                # Decode data
                # data = data.decode(FORMAT)

                # Write received bytes count to STDERR
                print("%d" %(len(data)), file=sys.stderr)

                # Forward to XML-RPC Java Server
                while True:
                    try:
                        if conn_err_counter == CONN_ERR_MAX:
                            raise

                        xml_rpc_client.Server.deliver(data)
                        break
                    except KeyboardInterrupt:
                        raise
                    except ConnectionRefusedError as e:
                        conn_err_counter = conn_err_counter + 1
                        print("XML-RPC Server: Connection refused! Attempt %d of %d ..." %(conn_err_counter, CONN_ERR_MAX, ))
                        sleep(CONN_ERR_DELAY)

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
