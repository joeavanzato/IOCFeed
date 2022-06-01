import helpers.retrieve_txt

list = {'ip':'https://feeds.dshield.org/top10-2.txt'}
description = "dshield-top10"

def start(ip_feed, domain_feed, url_feed):
    print("Updating DShield List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        domain_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '':
                ip, domain = line.split('\t')
                new_line_ip = ip.strip()+">>>"+domain+","+description.strip()+"\n"
                new_line_domain = domain.strip()+">>>"+ip+","+description.strip()+"\n"
                ip_feed.write(new_line_ip)
                if domain != "":
                    domain_feed.write(new_line_domain)
