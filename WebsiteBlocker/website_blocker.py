import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.twitter.com", "twitter.com", "pornhub.com", "www.pornhub.com", "https://www.pornhub.com/"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + '\n')

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()  #  Deletes everything that lies after the cursor
    time.sleep(5)
