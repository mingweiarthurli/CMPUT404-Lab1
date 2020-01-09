import requests

def main():
    print(requests.__version__)

    google = requests.get('https://google.com')
    print(google)

main()