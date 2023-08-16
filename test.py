from PIL import Image,ImageDraw,ImageFont
import qrcode


def print_card():

 id=input("enter id:")
 Name=input("enter name:")
 Jop=input("enter jop:")

 qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
    
 )

 qr.add_data(f"Id: {id} Name: {Name} Jop:{Jop}")
 qr.make(fit=True)
 qr_img=qr.make_image(fill="black",back_color="white")
 qr_img.save("21510857.png")


 re_qrcode=Image.open("21510857.png").resize((120,120))
 re_qrcode.save("21510857.png")

 print("done making qr_code")

 img=Image.open("wh.png")
 logo_img=Image.open("21510857.png")
 d=ImageDraw.Draw(img)

 fnt=ImageFont.truetype("micross.ttf",25)

 d.text((0,10),"Id: 21510857",font=fnt ,fill=(0,0,0))

 d.text((0,50),"Name: Ahmed Ramadan Abd Elnaser",font=fnt ,fill=(0,0,0))

 d.text((0,100),"Jop: Software Engineer",font=fnt ,fill=(0,0,0))

 d.text((0,150),"Email: ahmedramadan5452332@gmail.com",font=fnt ,fill=(0,0,0))


 img.paste(logo_img,(0,180))
 img.save("p.png")

