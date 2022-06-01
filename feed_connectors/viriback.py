

import helpers.retrieve_txt

list = {'url':'http://tracker.viriback.com/dump.php'}

def start(ip_feed, domain_feed, url_feed):
    print("Updating Viriback URL List...")
    for k,v in list.items():
        description_ = "viriback-urldump"
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        url_feed.write(f"#Source: {v}\n")
        x = 0
        for line in data.text.splitlines():
            if x == 0:
                x = x + 1
                continue
            data = line.split(",")
            description = description_+"-"+data[0]
            new_line_ip = data[1].strip()+">>>"+description.strip()+"\n"
            url_feed.write(new_line_ip)