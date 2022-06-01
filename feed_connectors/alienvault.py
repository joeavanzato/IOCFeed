
import helpers.retrieve_txt
list = {'ip':'https://reputation.alienvault.com/reputation.generic',
        }
description = "alienvault-generic"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Alienvault Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                data = line.split("#")
                new_line = data[0].strip() + ">>>" + description.strip()+ "\n"
                ip_feed.write(new_line)
