
import helpers.retrieve_txt
list = {'ip':'https://danger.rulez.sk/projects/bruteforceblocker/blist.php',
        }
description = "danger-rulez-blocklist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating danger.rulez.sk Blocklist...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.startswith(' ') and not line == '' and not line.startswith("ipaddress"): #Comments in banlist.txt
                    data = line.split("#")
                    new_line = data[0].strip() + ">>>" + description.strip()+"\n"
                    ip_feed.write(new_line)