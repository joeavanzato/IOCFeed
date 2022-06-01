
import helpers.retrieve_txt
list = {'ip':'https://www.cruzit.com/xxwbl2txt.php',
        }
description = "cruzit-blocklist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Cruzit Blocklist...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.startswith(' ') and not line == '' and not line.startswith("ipaddress"): #Comments in banlist.txt
                    new_line = line.strip() + ">>>" + description.strip()+"\n"
                    ip_feed.write(new_line)