import re
import wolframalpha

# Look up declarative knowledge with Wolfram
def wolframLookUp(a_string):
	client = wolframalpha.Client(keyring.get_password('wolfram','27732G-AK8G3EUHLX'))
	pattern = re.compile('([^\s\w]|_)+')
	b_string = re.sub(pattern, '', a_string)
	phrase=b_string
	pattern = re.compile("\\b(what|is)\\W", re.I)
	phrase_noise_removed = [pattern.sub("", phrase)]
	try:
		res= client.query(a_string)
		return next(res.results).text
	except:
return "Sorry"

print(wolframLookUp("where is berlin"))