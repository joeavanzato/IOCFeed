
import helpers.retrieve_txt
list = {'ip':'https://kriskintel.com/feeds/ktip_malicious_Ips.txt',
        'domain':'https://kriskintel.com/feeds/ktip_malicious_domains.txt'
        }
description = "kriskintel"

def start(ip_feed, domain_feed, url_feed):
    print("Updating KriskIntel List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                    new_line = line.strip() + ">>>" + description.strip()+ "\n"
                    ip_feed.write(new_line)
        elif k =='domain':
            domain_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                    new_line = line.strip() + ">>>" + description.strip()+ "\n"
                    domain_feed.write(new_line)