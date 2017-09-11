# -*- coding: utf-8 -*-
import urllib
import os, os.path

filePrice = u'.\\tmp\\Price_Stock.zip'  
urlPrice  = 'http://www.attrade.ru/files/TempFolder/Price_Stock.zip'

sss = urllib.urlopen(urlPrice).read()       #Скачиваем сначала страницу

if os.path.exists(filePrice):   os.remove(filePrice)
f = open(filePrice, 'wb')                    #Теперь записываем файл
f.write(sss)
f.close()
