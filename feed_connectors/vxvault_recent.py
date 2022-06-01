
import helpers.retrieve_txt

list = {'url':'http://vxvault.net/URL_List.php'}
description = "vxvault-last100-url"

def start(ip_feed, domain_feed, url_feed):
    print("Updating VXVault Recent URL List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        url_feed.write(f"#Source: {v}\n")
        x = 0
        for line in data.text.splitlines():
            if line.startswith("http"):
                new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                url_feed.write(new_line_ip)
