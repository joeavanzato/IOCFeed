

import helpers.retrieve_txt

list = {'url':'https://urlhaus.abuse.ch/downloads/text/'}
description = "urlhaus"

def start(ip_feed, domain_feed, url_feed):
    print("Updating urlhaus list...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        url_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.strip() == "":
                new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                url_feed.write(new_line_ip)
