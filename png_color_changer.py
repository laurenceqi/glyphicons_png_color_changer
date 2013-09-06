from PIL import Image

color='#1EABE3'

def main():
     files = glob.glob("glyphicons/png/*.png")
     for filename in files:
         maskfile = Image.open(filename)
         newfile = Image.new('RGBA',maskfile.size,(255,255,255,0))
         colorfile = Image.new('RGB',maskfile.size,color)
         newfile.paste(colorfile,None,maskfile)
         newfile.save(color+filename)


if __name__ == '__main__':
    main()


