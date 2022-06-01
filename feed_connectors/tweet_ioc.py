

import helpers.retrieve_txt

list = {'ip':'http://tweettioc.com/feed/ip','domain':'http://tweettioc.com/feed/domain','url':'http://tweettioc.com/feed/url'}
description = "tweetioc-feed"

def start(ip_feed, domain_feed, url_feed):
    print("Updating tweetioc.com Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == "ip":
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                new_line = line+">>>"+description+"\n"
                ip_feed.write(new_line)
        elif k == "domain":
            domain_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                new_line = line+">>>"+description+"\n"
                domain_feed.write(new_line)
        elif k == "url":
            url_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                new_line = line+">>>"+description+"\n"
                url_feed.write(new_line)
