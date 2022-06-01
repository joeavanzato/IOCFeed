
import helpers.retrieve_txt

list = {'ip':'https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt',
        'blackbook':'https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.csv'}
description = "stamparm"

def start(ip_feed, domain_feed, url_feed):
    print("Updating stamparm level 3 list...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        if k == 'ip':
            ip_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.strip() == "":
                    new_line_ip = line.strip()+">>>"+description.strip()+"\n"
                    ip_feed.write(new_line_ip)
        elif k == 'blackbook':
            domain_feed.write(f"#Source: {v}\n")
            for line in data.text.splitlines():
                if not line.startswith("#") and not line.strip() == "" and not line.startswith("Domain"):
                    data = line.split(",")
                    new_line_ip = data[0].strip()+">>>"+description.strip()+"-"+data[1]+"\n"
                    domain_feed.write(new_line_ip)