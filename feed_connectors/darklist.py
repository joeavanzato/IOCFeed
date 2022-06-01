
import helpers.retrieve_txt

list = {'ip':'http://www.darklist.de/raw.php'}
description = "darklist"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Darklist...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line == "":
                new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                ip_feed.write(new_line_ip)
