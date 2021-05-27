import PyPDF2, pyttsx3

libro = open('Gente_Altamente_Efectiva.pdf', 'rb')

lector_pdf = PyPDF2.PdfFileReader(libro)
paginas = lector_pdf.numPages

voz = pyttsx3.init()
rate = voz.getProperty('rate')
voz.setProperty('rate', rate-80)

for p in range(paginas):
    pagina = lector_pdf.getPage(p)
    texto =  pagina.extractText()
    voz.say(texto)
    voz.runAndWait()

#Las siguietnes lineas realizan la lecutura de una pagina especifica
# pagina = lector_pdf.getPage(7)
# texto =  pagina.extractText()
# voz.say(texto)
# voz.runAndWait()
