#!/usr/bin/python3
"""
script to send post request to passed url with email and display
body as response
"""

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
    print(response.text)
