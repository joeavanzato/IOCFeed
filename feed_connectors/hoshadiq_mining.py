
import helpers.retrieve_txt

list = {'domain':'https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt'}
description = "hoshadiq-mining"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Hoshsadiq Mining Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        domain_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line == "":
                line = line.split(' ')[1]
                new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                domain_feed.write(new_line_ip)
