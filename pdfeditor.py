from pdf2image import convert_from_path
from PIL import Image,ImageDraw
import sys

def replaceImage(path,im):
  conver_image=convert_from_path(path,poppler_path='C:\\Users\\User\\Desktop\\kedar\\poppler-0.68.0\\bin')
  finpdf=[]
  for n,image in enumerate(conver_image):
      image.save(path+str(n)+'.jpg','JPEG')
      header = Image.open(im)
      open_image = Image.open(path+str(n)+'.jpg')
      width,height= open_image.size
      patch_height=0
      if width>height:
          patch_height=251
      else:
          patch_height=190
      shape=[(25,26),(width,patch_height)]

      basewidth = width-100
      wpercent = (basewidth / float(header.size[0]))
      hsize = int((float(header.size[1]) * float(wpercent)))
      header = header.resize((basewidth, hsize))

      area= (50,50)
      img1 = ImageDraw.Draw(open_image)
      img1.rectangle(shape,fill='white',outline='white')
      open_image.paste(header,area)
      finpdf.append(open_image)
  finpdf[0].save(path + 'edited' + '.pdf',save_all=True, append_images=finpdf[1:]
)

replaceImage(sys.argv[1],sys.argv[2])
#replaceImage('C:\\Users\\User\\PycharmProjects\\pdfeditor\\ilovepdf_merged.pdf','C:\\Users\\User\\PycharmProjects\\pdfeditor\\Header.jpg')