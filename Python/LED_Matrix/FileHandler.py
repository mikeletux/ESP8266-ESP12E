class FileHandler:
	def __init__(self, filename):
		self.filename = filename
		
	def getMessageFromFile(self):
		message = ''
		try:
			f = open(self.filename,'r')
			message = f.readline()
		except (NameError):
			print('File not defined')
		finally:
			f.close()
		return message
		
	def setMessageToFile(self, newMessage):
		try:
			f = open(self.filename, 'w')
			f.write(newMessage)
		except (NameError):
			f = open(self.filename, 'x')
			f.write(newMessage)
		finally:
			f.close()

			
		
		