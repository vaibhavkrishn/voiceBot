from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-402121436784-402701988851-403874540375-a35f162b9d128e415149a5cd7853032f', #app verification token xoxp-401248561904-401248562224-401831886835-fb428b11e802c70ef64998edab3f50b5
							'xoxb-402121436784-402975752565-mkWaCIpfjXcgWFy6SXplwASh', # bot verification token xoxb-401248561904-401831887907-BUgv4Du1glWqdcx7UIaC4aTO
							'82qVOIokMaQVGXx11R5OfQyd', # slack verification token  C9V9Don0CAjG1WyKxT0H9GiP
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

 
