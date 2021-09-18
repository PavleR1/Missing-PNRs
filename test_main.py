import unittest
from main import Detector

class Test_main(unittest.TestCase):

	def test_conver(self):
		
		self.assertEqual(Detector().convert("111111"),54066636)
		self.assertEqual(Detector().convert("123489"),55656939)
		self.assertEqual(Detector().convert("AAAAAA"),540666360)
		self.assertEqual(Detector().convert("1A1A1A"),67583295)
		self.assertEqual(Detector().convert("ZAZAZA"),1854785985)
		self.assertEqual(Detector().convert("3Y1D7A"),208645930)

		self.assertRaises(ValueError,Detector().convert,"AAA")
		self.assertRaises(ValueError,Detector().convert,"AAA111AAA")
		self.assertRaises(ValueError,Detector().convert,"!DEE23")
		self.assertRaises(ValueError,Detector().convert,"ADEE03")
		self.assertRaises(ValueError,Detector().convert,"AdEE53")
		self.assertRaises(ValueError,Detector().convert,["!DEE23","Seaf"])
		self.assertRaises(ValueError,Detector().convert,[2,32,11])

	def test_check_order(self):
		self.assertEqual(Detector().check_order(54066636,54066637),(54066636,54066637))
		self.assertEqual(Detector().check_order(54066636,54066635),(54066635,54066636))

		self.assertRaises(ValueError,Detector().check_order,111111,111111)


	def test_find_missing_PNR(self):
		self.assertEqual(Detector().find_missing_PNR('AAAAAA','AAAAAZ'),24)
		self.assertEqual(Detector().find_missing_PNR('AAAAPA','AAAABE'),485)

		self.assertRaises(ValueError,Detector().find_missing_PNR,'111111','WWWWWW')






if __name__ == '__main__':
	unittest.main()