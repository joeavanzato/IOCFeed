

import helpers.retrieve_txt

list = {'ip':'https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt'}
description = "myip-ms-blacklist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating myip.ms block list...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.strip() == "":
                splits = line.split(" ")
                new_line_ip = splits[2].strip()+">>>"+description.strip()+"\n"
                ip_feed.write(new_line_ip)
