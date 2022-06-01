import helpers.retrieve_txt


def start(ip_feed, domain_feed, url_feed):
    try:
        data = helpers.retrieve_txt.get_remote_text('https://api.github.com/repos/firehol/blocklist-ipsets/contents/')
    except:
        return
    list_dict = {}
    for item in data.json():
        if item['name'].endswith('.ipset'):
            list_dict[item['name']] = item['download_url']

    print("Updating myip.ms block list...")
    for k,v in list_dict.items():
        description = f"firehol-{k.replace('.ipset','')}"
        print(f"Checking: {v}")
        try:
            data = helpers.retrieve_txt.get_remote_text(v)
        except:
            pass
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.strip() == "":
                new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                ip_feed.write(new_line_ip)