import smtplib,ssl  #que se puede usar para comunicarse con los servidores de correo para enviar correo
from email.mime.multipart import MIMEMultipart   #Este módulo es parte de la Compat32API de correo electrónico heredada ( ). Su funcionalidad se reemplaza parcialmente por la contentmanagerde la nueva API
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  #obtiene una estructura de objeto de mensaje al pasar un archivo o alguna imagen a un analizador, que analiza la imagen y devuelve el objeto de mensaje raíz 

enviador = 'nethesimz@gmail.com'
receptor = 'perlaaceneth@gmail.com'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = '¡Alerta!'
msgRoot['From'] = enviador
msgRoot['To'] = receptor
#msgRoot.preamble = 'Esto es el preambulo.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

# Envío en texto plano
msgText = MIMEText('La persona a intentado ingresar sin cubrebocas. Mantener las medidas pertinentes para desinfección.  ')
            
msgAlternative.attach(msgText)






s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()  
s.starttls()  
s.login(user = enviador, password = 'Huelum12')
s.sendmail(enviador, receptor, msgRoot.as_string())
s.quit()  
print (" Ya se ha enviado el correo :)")