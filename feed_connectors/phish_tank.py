


import helpers.retrieve_txt
list = {'ip':'http://data.phishtank.com/data/online-valid.csv',
        }
description = "phishtank"

def start(ip_feed, domain_feed, url_feed):
    print("Updating PhishTank List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        url_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '' and not line.startswith("phish"): #Comments in banlist.txt
                data = line.split(",")
                new_line = data[1].strip() + ">>>" + description.strip()+ "\n"
                url_feed.write(new_line)
