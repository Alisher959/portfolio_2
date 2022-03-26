a=input('sonni kiriting ')
if a.isdigit():
    a=int(a)
    if a>0 and a<30:
        q=a%10
        if q==1:
            l='bir'
        if q==2:
            l='ikki'
        if q==3:
            l='uch'
        if q==4:
            l='to`rt'
        if q==5:
            l='besh'
        if q==6:
            l='olti'
        if q==7:
            l='yetti'
        if q==8:
            l='sakkiz'
        if q==9:
            l='to`qqiz'
        if a>9 and a<20:
            l2='o`n'
        if a>19 and a<30:
            l2='yigirma'
        print(l2,l)
    else:
        print('1 dan 30 gacha son kiritish kerak')
else:
    print('son kiritish kerak')