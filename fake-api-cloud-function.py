import functions_framework
import time
import os

@functions_framework.http
def fake_api(request):
        try: 
                time.sleep(float(os.environ.get("SLEEP_TIME")))
                return "Leo is my favorite cat!!!" 
        except:
                return "SLEEP_TIME environment variable does not exist", 500
