import string
import sqlite3

class Detector():
	_d_s2n = {}		# dict symbol : number
	_d_n2s = {}		# dict number: symbol
	_base =  0      # base used to convert PNR to decimal 
	_conn = None	# connection to database
	_c = None		# cursor

	def __init__(self):
		self._d_s2n = {string.ascii_uppercase[i]:range(10,26+10)[i] for i in range(26)}
		self._d_s2n.update({str(i):i for i in range(0,10)})		# dict symbol : number
		self._d_n2s = dict(map(reversed, self._d_s2n.items()))	# dict number: symbol
		self._base =  35
		self.uspostavi_konekciju()

	def find_missing_PNR(self, x, y):

			a = self.convert(x)
			b = self.convert(y)

			a, b = self.check_order(a, b)
			n_missing = b - a - 1

			if n_missing > 1000: 
				raise ValueError('There are more than 1000 missing PNRs\n')
			
			list_of_missing_pnrs = [self.convert(i) for i in range(a+1,b)]
			self.save_to_db(x,y,list_of_missing_pnrs)
			
			return n_missing


	def convert(self, x):
		error = ValueError("\nWrong value is given \n ** PNR must contain 6(six) symbols(Uppercase letters [A-Z] and nubers [1-9]) **\n")
		if type(x) == str and len(x)==6:
			p = 0
			for char in x:
				if char == '0' or not(char in self._d_s2n.keys()) or char.islower(): 
					raise error
				p *= self._base
				p += self._d_s2n[char]	
			return p
		elif type(x) == int:
			p = []
			while x:
				x, n = divmod(x, self._base)
				p.append(self._d_n2s[n])
			return ''.join(reversed(p))
		raise error

	def check_order(self, x, y):
		if y > x:
			return x, y
		elif y == x:
			raise ValueError("Givend PNRs are the same")
		return y, x

	def uspostavi_konekciju(self):
		self._conn = sqlite3.connect('PNR.db')
		self._c = self._conn.cursor()
		try:
			self._c.execute("CREATE TABLE pnrs (pnrID integer PRIMARY KEY,PNR text,isMissing integer)")
			self._conn.commit()
		except :
			pass

	def save_to_db(self, first, second, missing):
		try:
			self._c.execute("INSERT INTO pnrs (PNR,isMissing) VALUES (?,?)",(first,0))
			self._c.execute("INSERT INTO pnrs (PNR,isMissing) VALUES (?,?)",(second,0))
			for m in missing:
				self._c.execute("INSERT INTO pnrs (PNR,isMissing) VALUES (?,?)",(m,1))
			self._conn.commit()
		except Exception as e:
			print(e)
			self._conn.rollback()
	
	def close_conection(self):
		self._conn.close()


if __name__ == '__main__':
	d = Detector()
	while(True):
		print("Type exit to stop runing program\n")
		a = input("First PNR : ") 
		if a.lower() == "exit" : 
			d.close_conection()
			break
		b = input("Second PNR : ")
		if b.lower() == "exit" : 
			d.close_conection()
			break
		try:
			print(d.find_missing_PNR(a,b))
		except Exception as e:
			print(e)
