import helpers.retrieve_txt
list = {'ip':'https://www.botvrij.eu/data/ioclist.ip-src',
        'ip':'https://www.botvrij.eu/data/ioclist.ip-dst',
        'domain':'https://www.botvrij.eu/data/ioclist.domain',
        'url':'https://www.botvrij.eu/data/ioclist.url'}

description = "botvrij.eu IOC Lists"

def start(ip_feed, domain_feed, url_feed):
    print("Updating botvrij IOC Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
        elif k == 'domain':
            domain_feed.write(f"#Source: {v}\n")
        elif k == 'url':
            url_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                try:
                    ioc, description_2 = line.split('#', 1)
                    new_line = ioc.strip() + ">>>" + description_2.strip() + "\n"
                except:
                    new_line = line.strip() + ">>>" + description.strip() + "\n"
                if k == 'ip':
                    ip_feed.write(new_line)
                elif k == 'domain':
                    domain_feed.write(new_line)
                elif k == 'url':
                    url_feed.write(new_line)