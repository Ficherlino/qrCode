import qrcode
from PIL import Image

link = "https://www.google.com/maps" #Inserir aqui o Link que quer transformar em QRCode

qr = qrcode.QRCode(version = 1, box_size = 20, border = 4)
qr.add_data(link)
qr.make(fit=True)

imagem = qr.make_image(fill="black", back_color="white")

imagem.save("qrCode.png") #Nome do arquivo
imagem.show()