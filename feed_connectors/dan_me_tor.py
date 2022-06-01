
import helpers.retrieve_txt

list = {'ip':'https://www.dan.me.uk/torlist/'}
description = "dan-me-torlist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating dan.me Tor Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            new_line_ip = line.strip()+">>>"+description.strip()+"\n"
            ip_feed.write(new_line_ip)
