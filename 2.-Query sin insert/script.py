#!C:\Users\Luis Castillo\Documents\Trabajo\python\python.exe
import cgi
import html
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'age' in form or not 'name' in form or not 'nControl' in form or not 'carrer' in form:
    print('<h1>Por favor capture los datos</h1>'
          )
else:
    name = form['name'].value
    age = form['age'].value
    nControl = form['nControl'].value
    carrer = form['carrer'].value
    print('<h1>INSERT INTO \'users\'(\'name\',\'age\',\'numControl\',\'carrer\') VALUES (\'',
          name, '\',\'', age, '\',\'', nControl, '\',\'', carrer, '\');</h1>')
