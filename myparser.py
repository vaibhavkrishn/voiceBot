import io
import json

from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN

from rasa_core.interpreter import NaturalLanguageInterpreter
   
        
class MyParser(NaturalLanguageInterpreter):
	def parse(self,text):
		loaded_engine = SnipsNLUEngine.from_path("./model/")
		nlu_output = loaded_engine.parse(text)
		intnt={}
		intent_ranking = []
		if nlu_output['intent']:
			intnt = {
			'name':nlu_output['intent']['intentName'],
			'confidence':nlu_output['intent']['probability']
			}
			intent_ranking = [intnt]
		entities1 = []
		if nlu_output['slots']:
			for k in nlu_output['slots']:  #"range": {"start": 28,"end": 41}
				dic={
				'start':k['range']['start'],
				'end':k['range']['end'],
				'value':k['value']['value'],
				'entity':k['slotName']
				}
				entities1.append(dic)
		output ={
		'intent' : intnt,
		'entities' :entities1,
		'intent_ranking':intent_ranking,
		'text':text
		}
		print(output)
		return output

if __name__ == '__main__':
	demo = MyParser()
	demo.parse("how is the weather in london next week")