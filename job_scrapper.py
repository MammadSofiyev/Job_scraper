from curses.ascii import isdigit
from sys import orig_argv
from turtle import color
from unicodedata import numeric
from zlib import adler32
import attr
import attrs
from bs4 import BeautifulSoup
from netaddr import P
import pyfiglet
from pymysql import NULL
import requests
from termcolor import colored
import time
from colorama import Fore,Back,Style
import re

def main__a(): 
  print(colored(pyfiglet.figlet_format('Xos gelmisiniz,  Hamiya Ugurlar!\n',font='slant'),color = 'red'))
  print(colored(pyfiglet.figlet_format('by Mammad Sofiyev',font='slant',width=80),color = 'white'))

  smart_job = colored('1.SmartJob','red')
  hello_job = colored('2.HelloJob','blue')
  job_search = colored('3.JobSearch' + Back.GREEN)
  all_l = colored('4.ALL','white')
  print(smart_job.center(178,'/'))  
  print(hello_job.center(178,'/'))
  print(job_search.center(178,'/'))    
  print(all_l.center(178,'/'))


  

 
 
  
def main_b(): 

 def smart_job(axtar):
 
 
 
 
  
      pagescrape = requests.get(f"https://smartjob.az/vacancies?search={axtar}")
  
      soup = BeautifulSoup(pagescrape.text,'html.parser')
  
      main = soup.find_all('div',attrs={'class':'brows-job-list'})
      mm = soup.find_all('div',attrs={'class':'col-md-12'})
      ff = soup.find_all('div',attrs={'class':'item-click'})
      
 
      for k in ff:
          
        basliq = k.find('div',attrs={'class':'brows-job-position'})
        
   
   
        price = k.find('div',attrs={'class':'salary-val'})
        if axtar not in (basliq.find('h3')).text:
               continue
        else:              
          print(colored("Şirkətin adı:",'white') + str(k.find('span',attrs={'class':'company-title'}).text).strip())   
  
          print(colored("Vəzifənin adı:",'white') + str(basliq.find('h3').text).strip())
  
          print(colored("Maaş:",'blue') + str(price.text).strip())
  
          tarix = k.find('div',attrs={'class':'created-date'})

         
          print(colored('Elanın yerləşmə tarixi:','red') + tarix.text[15:])
 
 
  
          x=k.find('h3')
 
 
  
          for a in x.find_all('a', href=True):
  
           ee = "Vakansiya üçün LINK:"
  
           href=a['href']
  
           lpp = colored(ee + href ,'yellow')
  
           print(lpp)
  
           print(colored('\n*************************************************************\n','white'))
 
 def jobsearch(axtar):
      jobser = requests.get(f"https://classic.jobsearch.az/?q={axtar}")
      soup = BeautifulSoup(jobser.text,'html.parser')
      main = soup.find_all('section',attrs={'class':'vacancies'})
      ff =soup.find_all('div',attrs={'id':'vacancies'})
      basliq = soup.find_all('ul',attrs={'data-id':'57062'})
      for t in ff:
         ll = (t.find_all('ul',attrs={'class':'vacancies__item'}))
         for u in ll:
           zz = u.find('h2')
           if axtar not in zz.text:
                  continue
           else:
             print(colored("Vəzifənin adı:",'white') + zz.text )
            
             ee = u.find('span')
             print(colored("Şirkətin adı:",'white') + ee.text + '\n')
             lk = u.find('span',attrs={'class':'vacancies__dead-line'})
             print(colored('Elanın yerləşmə tarixi:','red') + (u.find_all('li')[2]).text + '\n')
             print(colored('Elanın bitmə tarixi:','red') + (u.find_all('li')[3]).text + '\n')
             fgf = u.find('a',attrs={'class':'vacancies__provided'})
             print(colored('Vakansiya üçün LINK:' + fgf.get('href'),'yellow'))
             print(colored('\n*************************************************************\n','white'))
             
 
   
   
      
  
     
 def hellojob(axtr):
           pagescrap = requests.get(f"https://www.hellojob.az/search?query={axtar}&search_type=keyword&searched=")
       
           soup = BeautifulSoup(pagescrap.text,'html.parser')
       
           mainpage = soup.find_all('section',attrs={'class':'vacancies inner mb-0 mt-4'})
           mainjob = soup.find_all('div',attrs={'class':'col-md-8'}) 
           aaa = soup.find_all('a',class_='vacancies__item')
           for l in aaa:
              price = l.find('div',class_='vacancies__item__right')
              ll = price.find('span',attrs={'class':False})
         
              sol = l.find('span',class_='vacancies__price')
               
              if axtar not in l.find('h3').text:
                continue
              else:   
                print(colored('Vəzifənin adı:','white'),l.find('h3').text + '\n')
                print(colored('Şirkətin adı:','white'),l.find('p').text + '\n')
               
                print(colored('Elanın yerləşmə tarixi:','red') + ll.text + '\n')     
                
                   
                if sol is not None:
                 print(colored('Maaş:','blue') + sol.text + '\n')
 
                print(colored('Vakansiya üçün LINK:','yellow') + 'www.hellojob.az' + l.get('href'))
                
                             
                print(colored('\n*************************************************************\n','white'))
 
 
 
 
 
 
 
 
 
 
 
           
   
    
 
      
       #while re.search(r'\d', axtar):
       #  axtar = input('\n' + colored('[*]','red' + '') + colored('' + ' Zəhmət olmasa axtarış etmək istədiyiniz peşəni yazın:(Çıxış üçün "exit" yazın,əsas menu üçün "esas" yazın):','white'))
         
         
          
 while True:     
    txt = "HelloJob Vakansiyaları"  
    smrt = 'SmartJob Vakansiyaları'  
    jb = 'JobSearch Vakansiyaları'
       
  
 
    while True:
        sayt_secimi = input('\n' + colored('[*]', 'red') + colored(' Hansı saytda axtarış etmək istədiyinizi seçin(1,2,3,4)(Çıxış üçün "9" yazın,əsas menu üçün "0" yazın): ', 'white'))
        if sayt_secimi.isdigit():
                break           
        else:
             print('\nZəhmət olmasa 1,2,3 və ya 4 seçin')
      
    if int(sayt_secimi) == 0:
          main__a()  
    elif int(sayt_secimi) == 9:
                print("\nÇıxış edirsiniz. Proqram bağlanır.\n")
                time.sleep(3)
                print(pyfiglet.figlet_format('Yeniden Gorusmek Umidi ile :)\n',font='slant'))  
                exit()  
    else:
     while True:
      axtar = (input(colored('\n[*]','red' + '') + colored('' + ' Zəhmət olmasa axtarış etmək istədiyiniz peşəni yazın:','white' ))).capitalize()
      if axtar.isnumeric():
           
           print('\nZəhmət olmasa axtarış etmək istədiyiniz peşəni yazın:)') 
          
      else:
             break   
          
    
     time.sleep(3)
    
     if axtar == 'esas':
                      time.sleep(1)
                      print("\nƏsas menyuya qayıdırsınız.")
                      time.sleep(2)
                                           
                      main__a()
       
     if int(sayt_secimi) > 4:
          print('\nSayt seçimi olaraq 1,2,3 və ya 4 seçin')
     else:
        if int(sayt_secimi) == 1:  
                print(colored('\n[*]','red' + '') + colored('' + ' Məlumat axtarılır...\n','white'))
     
                print(colored('\n' + smrt.center(169,'-') + '\n','white'))  
                time.sleep(1)  
                smart_job(axtar)  
        if int(sayt_secimi) == 2:
                print(colored('\n[*]','red' + '') + colored('' + ' Məlumat axtarılır...\n','white'))
     
         
          
                print(colored('\n' + txt.center(169,'-')+ '\n','white'))
         
         
          
                time.sleep(2)
         
         
          
                hellojob(axtar)
         
        if int(sayt_secimi) == 3:
               print(colored('\n[*]','red' + '') + colored('' + ' Məlumat axtarılır...\n','white'))
             
               print(colored('\n' + jb.center(169,'-')+ '\n','white'))
         
               time.sleep(2)
         
               jobsearch(axtar)
          
        if int(sayt_secimi) == 4:
         
                print(colored('\n[*]','red' + '') + colored('' + ' Məlumat axtarılır...\n','white'))
     
          
                time.sleep(2)
         
         
          
                print(colored(smrt.center(169,'-')+ '\n','white'))
         
         
      
                time.sleep(2)
         
         
          
                smart_job(axtar)
         
                time.sleep(2)
         
                print(colored(jb.center(169,'-')+ '\n','white'))
           
                jobsearch(axtar)
          
          
                print(colored(txt.center(169,'-')+ '\n','white'))
         
         
                time.sleep(2)
       
                hellojob(axtar)
        
main__a()
main_b()   