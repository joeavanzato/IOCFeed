
import helpers.retrieve_txt

list = {'ip':'https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst','ip':'https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst'}
description = "secops-institute-tor"

def start(ip_feed, domain_feed, url_feed):
    print("Updating SecOps Institute Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            new_line_ip = line.strip()+";"+description.strip()+"\n"
            ip_feed.write(new_line_ip)