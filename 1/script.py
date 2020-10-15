#!C:\Users\Luis Castillo\Documents\Trabajo\python\python.exe
import cgi
import html
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'ano' in form:
    print('<h1>Por favor capture el año</h1>'
          )
else:
    ano = form['ano'].value
    numero = int(ano)
    if (numero % 400 == 0):
        print('<h1>El Año <i>%a</i> es bisiesto</h1>' % numero)
    elif(numero % 4 == 0 and numero % 100 != 0):
        print('<h1>El Año <i>%a</i> es bisiesto</h1>' % numero)
    else:
        print('<h1>El Año <i>%a</i> no es bisiesto</h1>' % numero)
