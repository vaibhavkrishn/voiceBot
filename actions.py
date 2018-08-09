from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '9dacdde0a438416bae2100609181907' #your apixu key
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location')
		current = client.getCurrentWeather(q=loc)
		
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionWiki(Action):
	def name(self):
		return 'action_wiki'
		
	def run(self, dispatcher, tracker, domain):
		import wikipedia
		wiki = tracker.get_slot('wikiInput')
		try:
			response = wikipedia.summary(wiki, sentences=2)	
		except Exception as e:
			response = 'Can you be more specific please.'
		
		dispatcher.utter_message(response)
		return [SlotSet('wikiInput',wiki)]