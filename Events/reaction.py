import time, discord
from Config._functions import grammar_list

class EVENT:
	LOADED = False
	RUNNING = False

	param = { # Define all the parameters necessary
		"CHANNEL": "",
		"EMOJIS": []
	}


	# Executes when loaded
	def __init__(self):
		self.LOADED = True


	# Executes when activated
	def start(self, TWOW_CENTRAL, PARAMS): # Set the parameters
		self.RUNNING = True

	
	# Executes when deactivated
	def end(self): # Reset the parameters
		self.param = {
			"CHANNEL": "",
			"EMOJIS": []
		}
		self.RUNNING = False
	

	# Function that runs on each message
	async def on_message(self, message, PERMS):
		if message.channel.mention != self.param["CHANNEL"]:
			return # Only messages that are in the channel

		for emoji in self.param["EMOJIS"]:
			try: # Add the reactions
				await message.add_reaction(emoji)
			except Exception: # If a reaction is invalid, skip it
				continue
	

	# Change a parameter of the event
	async def edit_event(self, message, new_params):
		incorrect = []
		correct = []
		for parameter in new_params.keys():
			try:
				self.param[parameter] = new_params[parameter]
				correct.append(parameter)
			except KeyError:
				incorrect.append(parameter)
		
		if len(correct) > 0:
			await message.channel.send(f"Successfully changed the parameters: {grammar_list(correct)}")
		if len(incorrect) > 0:
			await message.channel.send(f"The following parameters are invalid: {grammar_list(incorrect)}")
		
		return