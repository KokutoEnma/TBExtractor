import sys
from utils import Utils
from model import Model

inputs = [1,2,3,4]

class App:
	def __init__(self, mode):
		self.mode = mode
		self.utils = Utils()
		self.model = Model()

		self.modes = [
			('1. generate article 6 from MOU01-22.txt', 'generate_article_6'),
			('2. predict article 6', 'predict_article_6'),
			('3. predict all of MOU01-22.txt', 'predict_mou'),
			('4. predict another file', 'predict_other'),
			('5. set output file path/name', 'set_out_f')
		]
	
	def generate_article_6(self):
		self.utils.generate_article_6()
	
	def predict_article_6(self):
		self.utils.load_article_6()
		res = self.model.predict(self.utils.data)
		self.utils.make_output(res)
	
	def predict_mou(self):
		self.utils.load_input(self.utils.mou_f)
		res = self.model.predict(self.utils.data)
		self.utils.make_output(res)
	
	def predict_other(self):
		path = input('Enter file path to predict:')
		self.utils.load_input(path)
		res = self.model.predict(self.utils.data)
		self.utils.make_output(res)
	
	def set_out_f(self):
		path = input('Enter file path of output:')
		self.utils.out_f = path
	
	def print_menu(self):
		print('Enter number')
		print('\n'.join([item[0] for item in self.modes]))

	def run(self):
		while not self.mode:
			self.print_menu()
			m = eval(input())
			self.mode = None if m not in inputs else m
		
		getattr(self, self.modes[self.mode-1][1])()
			




if __name__ == '__main__':
	mode = None if len(sys.argv)==1 or eval(sys.argv[1]) not in inputs else sys.argv[1]
	app = App(mode)
	app.run()
