import requests

base_url = 'https://www.hacienda.go.cr/tica/web/Captcha/images/'
init_url = 'https://www.hacienda.go.cr/tica/web/Captcha/images/1.jpg'

response = requests.get(init_url)
i = 1

while response.ok:
    file_name = response.url.split('/')[-1]
    if i == 1:
        with open('/home/andres/Documents/JupyterNBs/MHCR_DUAS/Captchas/' + file_name, 'wb') as f:
            f.write(response.content)
    else:
        with open('/home/andres/Documents/JupyterNBs/MHCR_DUAS/Captchas/' + file_name, 'wb') as f:
            f.write(response.content)

    i += 1

    response = requests.get(base_url + f'{i}' + '.jpg')
    if response.ok == False:
        break

print('Job Done!')
