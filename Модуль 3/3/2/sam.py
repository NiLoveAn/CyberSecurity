from captcha.image import ImageCaptcha
import random

def generate_cap_text():
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    code = ""
    for i in range(7):
        code += random.choice(letters)
    return code

cap = ImageCaptcha(width= 200, height= 200)
rand = generate_cap_text()
cap = cap.create_captcha_image(rand, color='green', background='black')
cap.show()