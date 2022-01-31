# IGNORE THIS FILE !!!





# import requests
# import json
# import os

# os.remove("index.html")

# url = "https://api.github.com/users/QuantumByteStudios/received_events"
# r = requests.get(url)
# r = r.text 

# data = r.replace(",", "\n")
# data2 = data.replace("{", " ")
# data3 = data2.replace("}", " ")
# data4 = data3.replace('"type"', '<p class="type">"TYPE"</p>')
# data5 = data4.replace('"login"', '<p class="login">"LOGIN"</p>')
# data6 = data5.replace('"display_login"', '<p class="login">"DISPLAY_LOGIN"</p>')
# data7 = data6.replace('"action"', '<p class="action">"ACTION"</p>')
# data8 = data7.replace('"html_url"', '<p class="html_url">"URL"</p>')
# data9 = data8.replace('"repo"', '<p class="repo">"REPO"</p>')
# data10 = data9.replace('"', ' ')
# data11 = data10.replace('name', '<p class="name">NAME</p>')

# # print(data4)

# final = data11
# f = open("index.html", "a")

# stylesheet = '''
# <head>
#     <link rel="stylesheet" type="text/css" href="style.css">
# </head>
# '''
# f.write(stylesheet)
# f.write(final)

# f.close()


# trash = input("Ho Gaya Bhai..!")