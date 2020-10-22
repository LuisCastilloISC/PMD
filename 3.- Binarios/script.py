#!C:\Users\Angel\anaconda3\python.exe
import cgi
import html
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')

numero = int(form['number'].value)
bitn = int(form['bitn'].value) - 1
binDecimal = format(numero, '04b')
antiBinDecimal = binDecimal[::-1]
bitLess = binDecimal[len(binDecimal) - 1]

i = 0
newBin = ''
for bit in antiBinDecimal:
    if(i == bitn):
        newBin += '1'
    else:
        newBin += bit
    i += 1
newBin = newBin[::-1]

print('<h1>Binarios</h1>')
print('<h2>Numero:',numero,' Binario:',binDecimal,'</h2>')
print('<h2>Bit menos significativo:',bitLess,'</h2>')
print('<h2>N:',bitn + 1,'    Nuevo Binario:',newBin,'</h2>')
