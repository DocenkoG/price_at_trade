# -*- coding: utf-8 -*-
import urllib
import urllib.request
import os, os.path

filePrice = u'.\\tmp\\Price_Stock.zip'  
urlPrice  = 'http://www.attrade.ru/pr30fe16ff-24c4-4bd1-be40-69cbd4593924/TempFolder/Price_Stock.zip'

sss = urllib.request.urlopen(urlPrice).read()       #Скачиваем сначала страницу
print(len(sss))

if os.path.exists(filePrice):   os.remove(filePrice)
f = open(filePrice, 'wb')                    #Теперь записываем файл
f.write(sss)
f.close()
