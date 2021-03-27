import os

class Utils:

	def __init__(self):
		
		self.data = []

		self.mou_f = 'MOU01-22.txt'
		self.article6_f = 'article_6.txt'
		self.out_f = 'output.txt'

	def load_input(self, input_f):
		with open(input_f, 'r',encoding='utf-8') as f:
			self.data = [item.strip() for item in f.readlines()]

	def load_article_6(self):
		if self.article6_f not in os.listdir():
			self.generate_article_6()

		with open(self.article6_f, 'r') as f:
			self.data = [item.strip() for item in f.readlines()]

	def generate_article_6(self):

		print('generating article 6 from {}'.format(self.mou_f))

		self.load_input(self.mou_f)

		is_6 = False
		ans = []
		for item in self.data:
			if 'ARTICLE 6.0' in item:
				is_6 = True
			elif 'ARTICLE 7.0' in item:
				is_6 = False
			if is_6:
				ans.append(item)

		with open(self.article6_f, 'w') as f:
			f.write('\n'.join(ans))
		
		print('done')
	
	def make_output(self, data):
		print('making output file')
		

		ans = []
		temp_body = []

		def add_to_ans(a1, a2, ans):
			if len(temp_body)>0:
				a1[0]['text'] = '<{}>{}'.format(a1[0]['tag'], a1[0]['text']) 
				a1[-1]['text'] = '{}</{}>'.format(a1[-1]['text'], a1[-1]['tag'])
			a2['text'] = '<{}>{}</{}>'.format(a2['tag'], a2['text'], a2['tag'])
			ans+=[item['text'] for item in a1]
			ans.append(a2['text'])
			return ans
		
		for i in range(len(data)):
			item = data[i]
			prev = data[i-1] if not i==0 else None
			text, tag = item['text'], item['tag']

			if not tag == 'body':
				ans = add_to_ans(temp_body, item, ans)
				temp_body = []
			else:
				temp_body.append(item)

		with open(self.out_f, 'w') as f:
			f.write('\n'.join(ans))
				


		print('done')
	
	def print_data(self):
		print('\n'.join(self.data))