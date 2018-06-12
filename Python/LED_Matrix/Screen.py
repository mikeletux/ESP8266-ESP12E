from array import array

class Screen:
	"""Class to set and control the matrix led"""
	def __init__(self,width,messageToShow):
		self.height = 8 #No support for different height led matrix for now
		self.width = width
		screen = array('H', [0x0] * width)
		self.messageToShow = messageToShow
		self.messageToShowHex = array('H', [])
	
	def fromStringToHexBuffer(self):
		for i in self.messageToShow:
			letterHexList = self.getHexFromLetter(i)
			for j in letterHexList:
				self.messageToShowHex.append(j) #Putting hex letter representation into the buffer
			self.messageToShowHex.append(0x00) #Putting a line of space in buffer
		
	@staticmethod
	def getHexFromLetter(letter):
		alphabet = {
			'a' : [0x00, 0x20, 0x74, 0x54, 0x54, 0x7C, 0x78, 0x00],
			'b' : [0x00, 0x7E, 0x7E, 0x48, 0x48, 0x78, 0x30, 0x00],
			'c' : [0x00, 0x38, 0x7C, 0x44, 0x44, 0x44, 0x00, 0x00],
			'd' : [0x00, 0x30, 0x78, 0x48, 0x48, 0x7E, 0x7E, 0x00],
			'e' : [0x00, 0x38, 0x7C, 0x54, 0x54, 0x5C, 0x18, 0x00],
			'f' : [0x00, 0x00, 0x08, 0x7C, 0x7E, 0x0A, 0x0A, 0x00],
			'g' : [0x00, 0x98, 0xBC, 0xA4, 0xA4, 0xFC, 0x7C, 0x00],
			'h' : [0x00, 0x7E, 0x7E, 0x08, 0x08, 0x78, 0x70, 0x00],
			'i' : [0x00, 0x00, 0x48, 0x7A, 0x7A, 0x40, 0x00, 0x00],
			'j' : [0x00, 0x00, 0x80, 0x80, 0x80, 0xFA, 0x7A, 0x00],
			'k' : [0x00, 0x7E, 0x7E, 0x10, 0x38, 0x68, 0x40, 0x00],
			'l' : [0x00, 0x00, 0x42, 0x7E, 0x7E, 0x40, 0x00, 0x00],
			'm' : [0x00, 0x7C, 0x7C, 0x18, 0x38, 0x1C, 0x7C, 0x78],
			'n' : [0x00, 0x7C, 0x7C, 0x04, 0x04, 0x7C, 0x78, 0x00],
			'o' : [0x00, 0x38, 0x7C, 0x44, 0x44, 0x7C, 0x38, 0x00],
			'p' : [0x00, 0xFC, 0xFC, 0x24, 0x24, 0x3C, 0x18, 0x00],
			'q' : [0x00, 0x18, 0x3C, 0x24, 0x24, 0xFC, 0xFC, 0x00],
			'r' : [0x00, 0x7C, 0x7C, 0x04, 0x04, 0x0C, 0x08, 0x00],
			's' : [0x00, 0x48, 0x5C, 0x54, 0x54, 0x74, 0x24, 0x00],
			't' : [0x00, 0x04, 0x04, 0x3E, 0x7E, 0x44, 0x44, 0x00],
			'u' : [0x00, 0x3C, 0x7C, 0x40, 0x40, 0x7C, 0x7C, 0x00],
			'v' : [0x00, 0x1C, 0x3C, 0x60, 0x60, 0x3C, 0x1C, 0x00],
			'w' : [0x00, 0x1C, 0x7C, 0x70, 0x38, 0x70, 0x7C, 0x1C],
			'x' : [0x00, 0x44, 0x6C, 0x38, 0x38, 0x6C, 0x44, 0x00],
			'y' : [0x00, 0x9C, 0xBC, 0xA0, 0xE0, 0x7C, 0x3C, 0x00],
			'z' : [0x00, 0x44, 0x64, 0x74, 0x5C, 0x4C, 0x44, 0x00],
			#'ñ' : [0x00, 0x7A, 0x7A, 0x09, 0x09, 0x7A, 0x72, 0x00],
			#'€' : [0x00, 0x18, 0x3C, 0x7E, 0x99, 0x99, 0x42, 0x00],
			'+' : [0x00, 0x08, 0x08, 0x3E, 0x3E, 0x08, 0x08, 0x00],
			'\la' : [0x00, 0x18, 0x3C, 0x7E, 0x18, 0x18, 0x18, 0x18],
			' ' : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
			'!' : [0x00, 0x00, 0x00, 0x4F, 0x4F, 0x00, 0x00, 0x00],
			'"' : [0x00, 0x07, 0x07, 0x00, 0x00, 0x07, 0x07, 0x00],
			'$' : [0x00, 0x24, 0x2E, 0x6B, 0x6B, 0x3A, 0x12, 0x00],
			'%' : [0x00, 0x63, 0x33, 0x18, 0x0C, 0x66, 0x63, 0x00],
			'&' : [0x00, 0x32, 0x7F, 0x4D, 0x4D, 0x77, 0x72, 0x50],
			'/' : [0x00, 0x40, 0x60, 0x30, 0x18, 0x0C, 0x06, 0x02],
			'(' : [0x00, 0x00, 0x1C, 0x3E, 0x63, 0x41, 0x00, 0x00],
			')' : [0x00, 0x00, 0x41, 0x63, 0x3E, 0x1C, 0x00, 0x00],
			'*' : [0x08, 0x2A, 0x3E, 0x1C, 0x1C, 0x3E, 0x2A, 0x08],
			',' : [0x00, 0x00, 0x80, 0xE0, 0x60, 0x00, 0x00, 0x00],
			'-' : [0x00, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00],
			'.' : [0x00, 0x00, 0x00, 0x60, 0x60, 0x00, 0x00, 0x00],
			'0' : [0x00, 0x3E, 0x7F, 0x49, 0x45, 0x7F, 0x3E, 0x00],
			'1' : [0x00, 0x40, 0x44, 0x7F, 0x7F, 0x40, 0x40, 0x00],
			'2' : [0x00, 0x62, 0x73, 0x51, 0x49, 0x4F, 0x46, 0x00],
			'3' : [0x00, 0x22, 0x63, 0x49, 0x49, 0x7F, 0x36, 0x00],
			'4' : [0x00, 0x18, 0x18, 0x14, 0x16, 0x7F, 0x7F, 0x10],
			'5' : [0x00, 0x27, 0x67, 0x45, 0x45, 0x7D, 0x39, 0x00],
			'6' : [0x00, 0x3E, 0x7F, 0x49, 0x49, 0x7B, 0x32, 0x00],
			'7' : [0x00, 0x03, 0x03, 0x79, 0x7D, 0x07, 0x03, 0x00],
			'8' : [0x00, 0x36, 0x7F, 0x49, 0x49, 0x7F, 0x36, 0x00],
			'9' : [0x00, 0x26, 0x6F, 0x49, 0x49, 0x7F, 0x3E, 0x00],
			';' : [0x00, 0x00, 0x80, 0xE4, 0x64, 0x00, 0x00, 0x00],
			'=' : [0x00, 0x14, 0x14, 0x14, 0x14, 0x14, 0x14, 0x00],
			':' : [0x00, 0x00, 0x00, 0x24, 0x24, 0x00, 0x00, 0x00],
			'?' : [0x00, 0x02, 0x03, 0x51, 0x59, 0x0F, 0x06, 0x00],
			'A' : [0x00, 0x7C, 0x7E, 0x0B, 0x0B, 0x7E, 0x7C, 0x00],
			'B' : [0x00, 0x7F, 0x7F, 0x49, 0x49, 0x7F, 0x36, 0x00],
			'C' : [0x00, 0x3E, 0x7F, 0x41, 0x41, 0x63, 0x22, 0x00],
			'D' : [0x00, 0x7F, 0x7F, 0x41, 0x63, 0x3E, 0x1C, 0x00],
			'E' : [0x00, 0x7F, 0x7F, 0x49, 0x49, 0x41, 0x41, 0x00],
			'F' : [0x00, 0x7F, 0x7F, 0x09, 0x09, 0x01, 0x01, 0x00],
			'G' : [0x00, 0x3E, 0x7F, 0x41, 0x49, 0x7B, 0x3A, 0x00],
			'H' : [0x00, 0x7F, 0x7F, 0x08, 0x08, 0x7F, 0x7F, 0x00],
			'I' : [0x00, 0x00, 0x41, 0x7F, 0x7F, 0x41, 0x00, 0x00],
			'J' : [0x00, 0x20, 0x60, 0x41, 0x7F, 0x3F, 0x01, 0x00],
			'K' : [0x00, 0x7F, 0x7F, 0x1C, 0x36, 0x63, 0x41, 0x00],
			'L' : [0x00, 0x7F, 0x7F, 0x40, 0x40, 0x40, 0x40, 0x00],
			'M' : [0x00, 0x7F, 0x7F, 0x06, 0x0C, 0x06, 0x7F, 0x7F],
			'N' : [0x00, 0x7F, 0x7F, 0x0E, 0x1C, 0x7F, 0x7F, 0x00],
			'O' : [0x00, 0x3E, 0x7F, 0x41, 0x41, 0x7F, 0x3E, 0x00],
			'P' : [0x00, 0x7F, 0x7F, 0x09, 0x09, 0x0F, 0x06, 0x00],
			'Q' : [0x00, 0x1E, 0x3F, 0x21, 0x61, 0x7F, 0x5E, 0x00],
			'R' : [0x00, 0x7F, 0x7F, 0x19, 0x39, 0x6F, 0x46, 0x00],
			'S' : [0x00, 0x26, 0x6F, 0x49, 0x49, 0x7B, 0x32, 0x00],
			'T' : [0x00, 0x01, 0x01, 0x7F, 0x7F, 0x01, 0x01, 0x00],
			'U' : [0x00, 0x3F, 0x7F, 0x40, 0x40, 0x7F, 0x3F, 0x00],
			'V' : [0x00, 0x1F, 0x3F, 0x60, 0x60, 0x3F, 0x1F, 0x00],
			'W' : [0x00, 0x7F, 0x7F, 0x30, 0x18, 0x30, 0x7F, 0x7F],
			'X' : [0x00, 0x63, 0x77, 0x1C, 0x1C, 0x77, 0x63, 0x00],
			'Y' : [0x00, 0x07, 0x0F, 0x78, 0x78, 0x0F, 0x07, 0x00],
			'Z' : [0x00, 0x61, 0x71, 0x59, 0x4D, 0x47, 0x43, 0x00]
			#'Ñ' : [0x00, 0x7A, 0x7A, 0x11, 0x21, 0x7A, 0x7A, 0x00]
			}
		return alphabet[letter]
	
	