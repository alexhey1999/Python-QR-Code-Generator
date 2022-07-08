# Python QR Code Generator

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/alexhey1999/Python-QR-Code-Generator.svg)](https://github.com/alexhey1999/Python-QR-Code-Generator/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


This allows for dynamic QR Codes to be created with images on top.

This is a Python 3 implementation using the qrcode library and PIL

<!-- <p align="center"><img width=95% src="https://github.com/alexhey1999/Python-QR-Code-Generator/blob/master/examples/exampleQR.png"></p> -->

<p align="center"><img width=35% src="https://raw.githubusercontent.com/alexhey1999/Python-QR-Code-Generator/master/examples/exampleQR.png"></p>


## Installation

```console
# clone the repo
$ git clone https://github.com/alexhey1999/Python-QR-Code-Generator.git

# change the working directory to Python QR Code Generator
$ cd Python-QR-Code-Generator

# install the requirements
$ python3 -m pip install -r requirements.txt
```
<br>
## Usage
```console
$ python3 QRGenerator.py --help
usage: QRGenerator.py [-h] --type TYPE [--image IMAGE] [--out OUT] [--colour COLOUR]
                      [--backgroundColour BACKGROUNDCOLOUR] [--scale SCALE] [--version VERSION] [--boxSize BOXSIZE]
                      [--firstName FIRSTNAME] [--lastName LASTNAME] [--organization ORGANIZATION] [--email EMAIL]
                      [--phone PHONE] [--address ADDRESS] [--postcode POSTCODE] [--url URL] [--text TEXT]

This program generates QR Codes for information provided. Allows images to be added to the QR Codes.

optional arguments:
  -h, --help            show this help message and exit
  --type TYPE
  --image IMAGE         Path to the image
  --out OUT             Change the output file name
  --colour COLOUR       Change the colour of the QR Code
  --backgroundColour BACKGROUNDCOLOUR
                        Change the background colour of the QR Code
  --scale SCALE         Change the scale of the image. 1 is the same resolution as raw image
  --boxSize BOXSIZE     Change the resolution of the final QR Code
  --firstname FIRSTNAME
  --lastName LASTNAME
  --organization ORGANIZATION
  --email EMAIL
  --phone PHONE
  --address ADDRESS
  --postcode POSTCODE
  --url URL
  --text TEXT
 ```
<br> 
To generate a QR Code with a single link and image

```
python3 QRGenerator.py --type url --image {image-file} --colour {hex-color} --url {url}
```

To generate a QR Code with contact information
```
python3 QRGenerator.py --type contact --image {image-file} --colour {hex-color} --firstname {firstname} --lastname {lastname} --organization {organization} --email {email} --phone {phone} --address {address} --postcode {postcode}
```

To generate a QR Code with simple text
```
python3 QRGenerator.py --type text --image {image-file} --colour {hex-color} --text {text}
```

<br>

## Special Thanks

Thanks to https://github.com/nkmk for the general guide found here https://note.nkmk.me/en/python-pillow-qrcode/

Thank you also to https://github.com/arasatasaygin for the open source template logo https://github.com/arasatasaygin/openlogos/issues/17

<br>



 