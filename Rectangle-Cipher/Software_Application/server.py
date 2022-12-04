import socket 
import encryptor
import decryptor
import os

s = "server"
ip = "127.0.0.4"
port = 1240

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)

client,address = server.accept()


while(True):
    print(f"connection est - {address[0]} : {address[1]}")
    string = client.recv(1024)
    string = string.decode("utf-8")
    print("GOT RESp")
    client.send(bytes("OK","utf-8"))
    # searching for the file in the server 

    if(string=="E"):
        toenc = client.recv(1024)
        toenc = toenc.decode("utf-8")

        l = encryptor.encryption(toenc)

        sendtext = f"the encrypted text is {l[0]} and the key is {l[1]}!!\n Keep the key secret"

        client.send(bytes(sendtext,"utf-8"))
        # client.close()

    if(string=="D"):
        todec = client.recv(1024)
        todec = todec.decode("utf-8")


        x = todec.split()
        print(x)
        l = decryptor.decryption(x[0],x[1])

        sendtext = f"the decrypted text is : {l}"

        client.send(bytes(sendtext,"utf-8"))


        # client.close()

    if(string=="EXIT"):

        client.close()
        exit()
        

        


    