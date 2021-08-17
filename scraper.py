from selenium import webdriver;
import os,requests,time,bs4,datetime

state_code_to_name={"an" : "Andaman and Nicobar Islands" ,"ap" : "Andhra Pradesh" ,
                    "ar" : "Arunachal Pradesh" ,"as" : "Assam" ,
                    "br" : "Bihar" ,"ch" : "Chandigarh" ,
                    "ct" : "Chhattisgarh" ,"dn" : "Dadra and Nagar Haveli and Daman and Diu" ,
                    "dl" : "Delhi" ,"ga" : "Goa" ,
                    "gj" : "Gujarat" ,"hr" : "Haryana" ,
                    "hp" : "Himachal Pradesh" ,"jk" : "Jammu and Kashmir" ,
                    "jh" : "Jharkhand" ,"ka" : "Karnataka" ,
                    "kl" : "Kerala" ,"la" : "Ladakh" ,    
                    "ld" : "Lakshadweep" , "mp" : "Madhya Pradesh" ,
                    "mh" : "Maharashtra" , "mn" : "Manipur" ,
                    "ml" : "Meghalaya" , "mz" : "Mizoram" ,       
                    "nl" : "Nagaland" ,  "or" : "Odisha" ,
                    "py" : "Puducherry" ,"pb" : "Punjab" ,    
                    "rj" : "Rajasthan" , "sk" : "Sikkim" ,                                  
                    "un" : "State Unassigned" ,"tn" : "Tamil Nadu" ,
                    "tg" : "Telangana" , "tr" : "Tripura" ,
                    "up" : "Uttar Pradesh" ,   "ut" : "Uttarakhand" ,      
                    "wb" : "West Bengal" , 'jk': 'Jammu and Kashmir'
                    }
              
state_name_to_code={}
for k in state_code_to_name: state_name_to_code[state_code_to_name[k]]=k

if __name__=='__main__':
  options = webdriver.ChromeOptions();
  options.add_argument('--ignore-certificate-errors');
  options.add_argument("--headless")
  driver = webdriver.Chrome(chrome_options=options)  
  driver.get('https://www.mohfw.gov.in/')
  driver.find_element_by_xpath('//a[@href="#state-data"]').click()
  time.sleep(3)
  htm=driver.page_source
  a=open('test.html','w');a.write(htm);a.close()
  
  #parse html file
  soup=bs4.BeautifulSoup(htm)
  t=soup('tbody')
  
  date=datetime.datetime.now();date_str=date.strftime('%d/%m/%Y')
  if t: 
    t=t[0]
    chunks=[];states=[i.lower() for i in list(state_code_to_name.values())]
    state_data={}
    
    a=open('data.csv','a')
    for idx in range(36):
      chunk=t('td')[8*idx:8*(idx+1)]
      state_name=chunk[1].text)
      state_active=int(chunk[2].text)
      state_recovered=int(chunk[4].text)
      state_deaths=int(chunk[6].text)
      state_cases=state_active+state_recovered+state_deaths
      info='%s,%s,%d,%d,%d,%d'
      a.write(info+'\n' %(state_name,date_str,state_cases,state_recovered,state_active,state_deaths)
      print(info)
    a.close()
  else: 
    print('Could not find element containing state-wise cases data!!')
    
  
  url = 'https://transfer.sh/'
  file = {'{}'.format('test.html'): open('test.html', 'rb')}
  response = requests.post(url, files=file)
  download_link = response.content.decode('utf-8')
  print('link to test.html',download_link)
  
