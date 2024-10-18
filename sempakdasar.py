import requests
from tqdm import tqdm
import time

def verify_license(url_id):
    url = f'https://run.mocky.io/v3/{url_id}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "KNTOL"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if response.text == "U2FsdGVkX18jIXzMRGh/Ao/w1k/QaSGhCSj//tJAq2I=":
            print("SCRIPT BY KRAZY BRAZY")
            for char in tqdm("Request was successful!", total=len("Request was successful!"), ncols=100):
                time.sleep(0.1)
            print()
            return True
        else:
            print("Response text is not as expected. Please enter the URL ID again.")
    elif response.status_code == 404:
        print("Request failed with status code: 404. Please enter the LICENSE KEY again.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    return False
