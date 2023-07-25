import requests

response = requests.get('https://www.hdwallpapers.in/download/colorful_glowing_shape_lines_4k_8k_hd_abstract-HD.jpg')
with open('img.jpg', 'wb') as picture:
    picture.write(response.content)


response = requests.get('https://api.github.com/user/repos', auth=('smartiqa-user', '3b7cbc8bbe0c7866ccd003c1ba21add68f6ddb31'))
print(response.json())

