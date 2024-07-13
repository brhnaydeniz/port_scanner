import socket
import time
from queue import Queue
import threading

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print(f"Port {port} is open")
            try:
                banner = s.recv(1024)
                banner = banner.decode().strip()
                if banner:
                    print(f"  Banner: {banner}")
                else:
                    print("  Banner: Banner bilgisi bulunamadı")
            except:
                print("  Banner: Banner bilgisi bulunamadı")
            try:
                protocol = s.recv(1024)
                protocol = protocol.decode().strip()
                if protocol:
                    print(f"  Protocol: {protocol}")
                else:
                    print("  Protocol: Bilinmiyor")
            except:
                print("  Protocol: Bilinmiyor")
            try:
                version = s.recv(1024)
                version = version.decode().strip()
                if version:
                    print(f"  Version: {version}")
                else:
                    print("  Version: Bilinmiyor")
            except:
                print("  Version: Bilinmiyor")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

target = input('Taramak istediğiniz adresi giriniz: ')
t_IP = socket.gethostbyname(target)
print ('Bu IP adresinde arama başlatıldı: ', t_IP)

startTime = time.time()

q = Queue()

for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start_port = int(input("Başlangıç port numarası girin: "))
end_port = int(input("Bitiş port numarası girin: "))

for worker in range(start_port, end_port):
    q.put(worker)

q.join()

print('Harcanan Süre', time.time() - startTime)
