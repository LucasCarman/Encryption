from tkinter import *
from tkinter import ttk
import aessend as send
import sys
import socket
import threading


key = b'Sixteen byte key'
#def sendKey():
#    #print(secret_key)
#    sentRoot = Tk()
#    sentFrm = ttk.Frame(sentRoot)
#    sentFrm.grid()
#    ttk.Label(sentFrm, text="Secret Key Sent").grid(column=0, row=0)
#    ttk.Label(sentFrm, text=secret_key.get()).grid(column=0, row=1)

stop_listen = False
def beginListenThread():
    global x 
    x = threading.Thread(target=beginListen)
    x.start()

def sendMessage():
    (columns, rows) = listenWidget.grid_size()
    ttk.Label(text=message.get()).grid(column=3, row=rows + 1)
    stop_listen = True
    send.connectSend(key, message.get())

def beginListen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on %s port %s' % server_address, file=sys.stderr) 
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)  
    while stop_listen == False:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr) 
        connection, client_address = sock.accept()
        try:
            fullMessage = bytearray(b'')
            print('connection from', client_address, file=sys.stderr)
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                #decrypted_message = rsa.decrypt(data, privkey)
                print('received "%s"' % data, file=sys.stderr)
                fullMessage += data
                #print(fullMessage)
                
                #messageReceived.set(fullMessage.decode('latin1'))

                if data:
                    print('sending data back to the client', file=sys.stderr)
                    connection.sendall(data)
                else:
                    print('no more data from', client_address, file=sys.stderr)
                    break       
        finally:
        # Clean up the connection
            #print(fullMessage)
            #decrypted_message = rsa.decrypt(fullMessage, privkey)
            #print(decrypted_message)
            (columns, rows) = listenWidget.grid_size()
            ttk.Label(text=fullMessage.decode('latin1')).grid(column=0, row=rows + 1)
            connection.close()
        #sock.close()
        #break

listenWidget = Tk()
listenFrame = ttk.Frame(listenWidget, padding=10)
listenFrame.grid()
messageReceived = StringVar()
message = StringVar()
sent_message = StringVar()
#ttk.Button(listenFrame, text="Listen", command=beginListenThread).grid(column=2, row=1)
ttk.Button(listenFrame, text="Send", command=sendMessage).grid(column=4, row=1)
ttk.Entry(listenFrame, textvariable=message).grid(column=2, row=1)
ttk.Label(listenFrame, text="Messages").grid(column=1, row=0)
#ttk.Label(listenFrame, textvariable=sent_message).grid(column=3, row=1)
messageHistory = ttk.Label(listenFrame, textvariable=messageReceived).grid(column=0, row=2)


#root = Tk()
#frm = ttk.Frame(root, padding=10)
#frm.grid()
beginListenThread()

#ttk.Label(frm, text="What's the message?").grid(column=0, row=0)
#secret_entry = ttk.Entry(frm, textvariable=message).grid(column=1, row=0)
#ttk.Button(frm, text="Send Key", command=sendMessage).grid(column=2, row=3)



#secret_key = StringVar()
#ttk.Label(frm, text="What is the secret key?").grid(column=0, row=0)
#secret_entry = ttk.Entry(frm, textvariable=secret_key).grid(column=1, row=0)
#ttk.Button(frm, text="Send Key", command=sendKey).grid(column=2, row=3)
#root.mainloop()
listenWidget.mainloop()