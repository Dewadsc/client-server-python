import socket

ip = socket.gethostname()
port = 5055

sc = socket.socket()
sc.bind((ip, port))
print ("Server diaktifkan")

sc.listen(5)
conn, addr = sc.accept()
print ("Terhubung dengan ", addr)

while 1:
    pesan = input(str(">>Anda : "))
    pesan = pesan.encode()
    conn.send(pesan)

    inbox = conn.recv(1024)
    inbox = inbox.decode()
    print ("Client :", inbox)