import socket 
import os
import time
ip = "127.0.0.4"
port = 1240


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,port))
while (True):
    string = input("What do you want to perform Encryption or Decryption\n Write E for Encryption\n Write D for Decryption\nElse write EXIT for quitting the connection")

    if(string!="E" and string!="D" and string!="EXIT"):
        print("Please enter Valid Response")
        continue


    server.send(bytes(string,"utf-8"))
    ack = server.recv(1024)
    ack = ack.decode("utf-8")
    print(ack)

    if(string=="E"):
        # print("Enter a 16 length multiple string to encrypt")

        toenc = input("Enter a message in hex form: ")
        print("OK!!!Sending your data to encrypt")
        time.sleep(1)
        server.send(bytes(toenc,"utf-8"))


        text = server.recv(1024)
        text = text.decode("utf-8")
        print("this is a message from server.......")
        print(text)
        print()
        # client.close()


    if(string=="D"):

        todec = input("Enter the encrypted message")
        key = input("Enter the key")
        sender = str(todec) + " " + str(key)
        print("OK!!!Sending your data to decrypt")
        time.sleep(1)
        server.send(bytes(sender,"utf-8"))


        text = server.recv(1024)
        text = text.decode("utf-8")
        print("this is a message from server.......")
        print(text)
        print()
        # server.close()


    if(string=="EXIT"):
        print("OK THANKS FOR BEING THERE")
        # print("CLOSING")

        server.close()
        exit()


        








