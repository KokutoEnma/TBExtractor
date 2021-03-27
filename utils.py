import os

class Utils:

	def __init__(self):
		
		self.data = []

		self.mou_f = 'MOU01-22.txt'
		self.article6_f = 'article_6.txt'
		self.out_f = 'output.txt'

	def load_input(self, input_f):
		with open(input_f, 'r', encoding='utf-8-sig') as f:
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
		temp = []

		def add_temp(temp_list, ans):
			a= {'list':[],'tag':'none'}
			i=0
			for item in temp_list:
				if item['text'] == '':
					a['list'].append(item['text'])
					i+=1
				else:
					break
			if len(a['list'])>0:
				ans.append(a)
			a= {'list':[],'tag':'none'}
			j=len(temp_list)
			for item in temp_list[::-1]:
				if item['text'] == '':
					a['list'].append(item['text'])
					j-=1
				else:
					break
			b= {'list':[],'tag':'body'}
			for ind in range(i, j):
				b['list'].append(temp_list[ind]['text'])

			if len(b['list'])>0:
				ans.append(b)

			if len(a['list'])>0:
				ans.append(a)
			return ans
			

		for i in range(len(data)):
			item = data[i]
			text, tag = item['text'], item['tag']

			if not tag == 'body':
				ans = add_temp(temp, ans)
				temp = []
				ans.append({
					'list':[text],
					'tag':tag
				})
			else:
				temp.append(item)
		
		ans = add_temp(temp, ans)

		res = []
		for item in ans:				
			if not item['tag']=='none':
				item['list'][0] = '<{}>{}'.format(item['tag'], item['list'][0])
				item['list'][-1] = '{}</{}>'.format(item['list'][-1], item['tag'])

			res+=[e for e in item['list']]

		with open(self.out_f, 'w') as f:
			f.write('\n'.join(res))
				


		print('done')
	
	def print_data(self):
		print('\n'.join(self.data))