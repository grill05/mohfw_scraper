from selenium import webdriver;
import os,requests

options = webdriver.ChromeOptions();
options.add_argument('--ignore-certificate-errors');
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)  
driver.get('https://www.mohfw.gov.in/')
htm=driver.page_source
a=open('test.html','w');a.write(htm);a.close()

url = 'https://transfer.sh/'
file = {'{}'.format('test.html'): open('test.html', 'rb')}
response = requests.post(url, files=file)
download_link = response.content.decode('utf-8')
print('link to test.html',download_link)
