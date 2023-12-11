import requests

def get_access_token(api_key):
    base_url =  f"http://{given_ip}:{given_port}/api/token"

    login_url = f"{base_url}?api_key={api_key}"

    response  = requests.get(login_url).json()
    access_token = response.get("access_token")
    return access_token