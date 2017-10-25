import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '7df34bbf717b412d97b7056c110b967e'


def main():
	 while(1):
	    stringu=raw_input()
	    if(stringu=="exit"):
		break
	    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

	    request = ai.text_request()

	    request.lang = 'de'  # optional, default value equal 'en'

	    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

	    request.query = stringu
	    
	    response = request.getresponse()
	   
	    string = response.read().decode('utf-8')
	    json_obj = json.loads(string)

	    print(json_obj["result"]["fulfillment"]["speech"])

if __name__ == '__main__':
	main()
