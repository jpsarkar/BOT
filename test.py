import os.path
import sys
import json
import os

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'bcc66103500c45ec8bda56917db33377'


def main():
 os.system('clear')
 while(1):
    
    stringu=raw_input().strip("/")
    if(stringu=="exit"):
	print("Thank You for chatting :)")
	zzz=raw_input()
	os.system('clear')
	break
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = stringu
    
    response = request.getresponse()
 
    string = response.read().decode('utf-8')   #get response from api
    json_obj = json.loads(string)

    print(json_obj["result"]["fulfillment"]["speech"]) #extract from string

if __name__ == '__main__':
	main()
