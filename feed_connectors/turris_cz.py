
import helpers.retrieve_txt
list = {'ip':'https://view.sentinel.turris.cz/greylist-data/greylist-latest.csv',
        }
description = "turris-cz-greylist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Sentinel Turris CZ List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.startswith(' ') and not line == '' and not line.startswith("Address"): #Comments in banlist.txt
                    data = line.split(",", 1)
                    new_line = data[0].strip() + ">>>" + description.strip()+"-"+data[1].strip().replace('\"','')+"\n"
                    ip_feed.write(new_line)