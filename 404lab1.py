import requests

def main():
    # print out the version of the requests library
    print(requests.__version__)

    # GET the Google homepage
    google = requests.get('https://google.com')
    print(google)

    # download this file from GitHub and prints out its own source code from GitHub
    var = requests.get('https://raw.githubusercontent.com/mingweiarthurli/CMPUT404-Lab1/master/404lab1.py')
    print(var.content)

main()