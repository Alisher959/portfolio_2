nom1=str(input('Ijtimoiy tarmoq nomini kiriting: '))
a1, b1, c1=map(float, input('3ta qiymatni kiriting: ').split())
nom2=str(input('Ijtimoiy tarmoq nomini kiriting: '))
a2, b2, c2=map(float, input('3ta qiymatni kiriting: ').split())
nom3=str(input('Ijtimoiy tarmoq nomini kiriting: '))
a3, b3, c3=map(float, input('3ta qiymatni kiriting: ').split())

import pygal

line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = [nom1, nom2, nom3]
line_chart.add(nom1, [a1, b1, c1])
line_chart.add(nom2, [a2, b2, c2])
line_chart.add(nom3, [a3, b3, c3])
line_chart.render_in_browser()