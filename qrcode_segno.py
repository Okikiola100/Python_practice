import segno
Info = "Name: Oladapo Okikiola Eniola\nPhone: +2348168364293\nAddress: 53 Falikat Ajoke Street Ijede Ikorodu Lagos State\nGmail: okikiolaoladapo10@gmail.com\nWebsite: oladapookikiola.bio.link"
qrcode = segno.make(Info)
qrcode.save("qrcode_segno.png", dark="yellow", light="#323524", scale=5)
