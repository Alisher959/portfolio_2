import math

soat1= int(input('soat1 '))
minut1= int(input('minut1 '))
sekund1= int(input('sekund1 '))
soat2= int(input('soat2 '))
minut2= int(input('minut2 '))
sekund2= int(input('sekund2 '))

sekund=((soat1-soat2)*3600)+((minut1-minut2)*60)+((sekund1-sekund2)*1)
print('sekund',format(sekund))