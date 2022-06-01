
import helpers.retrieve_txt

list = {'ip':'http://cinsscore.com/list/ci-badguys.txt'}
description = "cinsscore-ci-badguys"

def start(ip_feed, domain_feed, url_feed):
    print("Updating cinsscore CI Badguys List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                new_line = line.strip()+">>>"+description.strip()+"\n"
                ip_feed.write(new_line)