
import helpers.retrieve_txt

list = {'ip':'https://data.netlab.360.com/feeds/dga/dga.txt'}
description = "netlab-360-dgas"

def start(ip_feed, domain_feed, url_feed):
    print("Updating netlab-360-DGA List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        domain_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '':
                try:
                    splits = line.split('\t')
                except:
                    pass
                new_line = splits[1].strip()+";DGA-Family-"+splits[0]+"\n"
                domain_feed.write(new_line)