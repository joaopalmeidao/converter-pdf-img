from pdf2image import convert_from_path

path = r'C:\\Program Files\\poppler\\Library\\bin'

images = convert_from_path(r'arquivos\\NF BOX DELIVERY 23646.pdf', poppler_path=path)

for i in range(len(images)):
    images[i].save(r'imagens\\page'+ str(i) +'.jpg', 'JPEG')
