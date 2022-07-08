import sys, random, argparse
import qrcode
import json
import csv
from PIL import Image

def generateQRCode(data, imageAdd, image, colour, backgroundColour, scale, out, boxSize):
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,box_size = boxSize,border = 1)
    # Adding data to the instance 'qr'
    qr.add_data(data)
    qr.make()
    #Change this to change QR Colours
    img = qr.make_image(fill_color = colour,back_color = backgroundColour)
    print(img.size)    
    
    if imageAdd:
        logo = Image.open(image)
        if scale:
            logo = logo.resize((int(logo.size[0]*scale),int(logo.size[1]*scale)))
        #attempt to auto calculate scale of logo to be 30% of img size while maintaining aspect ratio
        else:
            logoScale = (img.size[0]/logo.size[0])*0.3
            logo = logo.resize((int(logo.size[0]*logoScale),int(logo.size[1]*logoScale)))
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo,pos)

    imageName = out + "QR.png"
    img.save(imageName)
    print("QR Code saved as: ", imageName)


def main():
    # PARSER
    description = 'This program generates QR Codes for information provided. Allows images to be added to the QR Codes.'

    parser = argparse.ArgumentParser(description=description)
    
    # ARGS
    #Required
    parser.add_argument('--type', dest='type', required=True)

    # Optional
    parser.add_argument('--image', dest='image', required=False,help='Path to the image')
    parser.add_argument('--out', dest='out', required=False,help='Change the output file name')
    parser.add_argument('--colour', dest='colour', required=False,help='Change the colour of the QR Code')
    parser.add_argument('--backgroundColour', dest='backgroundColour', required=False,help='Change the background colour of the QR Code')
    parser.add_argument('--scale', dest='scale', required=False,help='Change the scale of the image. 1 is the same resolution as raw image')
    parser.add_argument('--boxSize', dest='boxSize', required=False,help='Change the resolution of the final QR Code')
    
    #Contact args
    parser.add_argument('--firstname', dest='firstname', required=False)
    parser.add_argument('--lastName', dest='lastName', required=False)
    parser.add_argument('--organization', dest='organization', required=False)
    parser.add_argument('--email', dest='email', required=False)
    parser.add_argument('--phone', dest='phone', required=False)
    parser.add_argument('--address', dest='address', required=False)
    parser.add_argument('--postcode', dest='postcode', required=False)

    #URL args
    parser.add_argument('--url', dest='url', required=False)

    #Text args
    parser.add_argument('--text', dest='text', required=False)

    # PARSE ARGS
    args = parser.parse_args()
   
    # Assign args to variables
    image = None
    imageAdd = False
    if args.image:
        image = args.image
        imageAdd = True

    out = 'NewGenerated'
    if args.out:
        out = args.out

    colour = '#000000'
    if args.colour:
        colour = args.colour

    backgroundColour = '#ffffff'
    if args.backgroundColour:
        backgroundColour = args.backgroundColour
    
    validTypes = ['contact', 'text', 'url']
    if args.type not in validTypes:
        print('Error: type must be one of the following: ', validTypes)
        quit()
    
    scale = None
    if args.scale:
        try:
            scale = float(args.scale)
        except:
            print('Error: version must be an integer')
            quit()

    boxSize = 10
    if args.boxSize:
        try:
            boxSize = int(args.boxSize)
        except:
            print('Error: boxSize must be an integer')
            quit()

    # CONTACT

    # Generate QR Code
    if args.type == 'contact':
        firstName = args.firstName
        lastName = args.lastName
        organization = args.organization
        email = args.email
        phoneNum = args.phone
        addressLine = args.address
        postcode = args.postcode

        #Format "BEGIN:VCARD\nVERSION:3.0\nN:"+firstName+" "+lastName+";\nORG:"+organization+"\nEMAIL;TYPE=INTERNET:"+email+"\nTEL:"+phoneNum+"\nADR:;;"+addressLine+";"+postcode+"\nEND:VCARD"
        contactFormat = "BEGIN:VCARD\nVERSION:3.0\nN:"+firstName+" "+lastName+";\nORG:"+organization+"\nEMAIL;TYPE=INTERNET:"+email+"\nTEL:"+phoneNum+"\nADR:;;"+addressLine+";"+postcode+"\nEND:VCARD"
        # generateQRCode()
        pass
    elif args.type == 'text':
        # generateQRCode(data, imageAdd, image, colour, backgroundColour, scale, out, version, boxSize)
        text = args.text
        generateQRCode(text, imageAdd, image, colour, backgroundColour, scale, out, boxSize)
        
    elif args.type == 'url':
        url = args.url
        generateQRCode(url, imageAdd, image, colour, backgroundColour, scale, out, boxSize)


# main
if __name__ == '__main__':
    main()