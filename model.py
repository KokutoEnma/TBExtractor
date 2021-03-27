import re

class Model:
	def __init__(self):
		self.tags = ['title','subtitle','body']
		self.data=[]

	def predict(self, data):

		self.data = [{'text':item, 'tag':None} for item in data]
		title, subtitle, body = self.tags	
		self.detect_page_tag()

		for i in range(len(self.data)):
			item = self.data[i]
			sentence = item['text']

			if self.predict_title(sentence):
				item['tag'] = title
			
			elif self.predict_subtitle(sentence):
				item['tag'] = subtitle
			else:
				item['tag'] = body

					
		return self.data

	
	def predict_title(self, sentence):
		return True if re.match('^ARTICLE \d+\.\d+ [A-Z\s]+', sentence) else False

	
	def predict_subtitle(self,sentence):
		roman_num = 'M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
		return re.match('^Section {}.*'.format(roman_num), sentence)

	
	def detect_page_tag(self):

		sentence_table = {}
		page_indexes = []

		for i in range(len(self.data)):

			text = self.data[i]['text']
			if text == '':
				continue

			if re.match('^\d+$', text):
				page_indexes.append(i)
			elif text not in sentence_table:
				sentence_table[text]=1
			else:
				sentence_table[text]+=1
		
		max_count_sentence = ''
		max_count = - float('inf')
		for item in sentence_table:
			if sentence_table[item] > max_count:
				max_count = sentence_table[item]
				max_count_sentence = item
		
		remains = []
		for i in range(len(self.data)):
			text = self.data[i]['text']
			if text == max_count_sentence:
				continue

			elif i in page_indexes and self.data[i+1]['text'] == max_count_sentence:
				continue

			else:
				remains.append(self.data[i])

		self.data = remains		



	
