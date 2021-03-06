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

CLIENT_ACCESS_TOKEN = 'fd0fdd40aea6465cbd6f7f07ce69df54'


def main():
 os.system('clear')
 while(1):
    
    stringu=raw_input().strip("/")
    if(stringu=="exit"):
	print("Thank You for chatting ")
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

    print("duration: "+json_obj["result"]["parameters"]["duration"])
    print("hotel-type: "+json_obj["result"]["parameters"]["hotel-type"])
    print(json_obj["result"]["parameters"]["location"])
    print("numberofroom: "+json_obj["result"]["parameters"]["number-of-rooms"])
    print("type-of-reservations: "+json_obj["result"]["parameters"]["type-of-reservations"])

if __name__ == '__main__':
	main()
