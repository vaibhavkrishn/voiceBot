from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weathernlu')
	# print(interpreter.parse("What do you know about vietnam history ?"))
	# print(interpreter.parse("Tell me about ancient india"))
	# print(interpreter.parse("How is weather"))
	# print(interpreter.parse("How is the weather in India's capital city ?"))
	# print(interpreter.parse("where is chennai city located"))
	print(interpreter.parse("sing a song for me"))
	print(interpreter.parse("what is 2+3"))
	print(interpreter.parse("Describe Newton laws of motion"))
	print(interpreter.parse("who is Barack obama"))
if __name__ == '__main__':
	train_nlu('./data/data.json', 'config.yml', './models/nlu')
	run_nlu()