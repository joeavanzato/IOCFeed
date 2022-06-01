
import helpers.retrieve_txt
list = {'ip':'https://dataplane.org/dnsrd.txt',
        'ip2':'https://dataplane.org/dnsrdany.txt',
        'ip3': 'https://dataplane.org/dnsversion.txt',
        'ip4': 'https://dataplane.org/sipinvitation.txt',
        'ip5': 'https://dataplane.org/sipquery.txt',
        'ip6': 'https://dataplane.org/sipregistration.txt',
        'ip7': 'https://dataplane.org/smtpdata.txt',
        'ip8': 'https://dataplane.org/smtpgreet.txt',
        'ip9': 'https://dataplane.org/sshclient.txt',
        'ip0': 'https://dataplane.org/sshpwauth.txt',
        'ip11': 'https://dataplane.org/telnetlogin.txt',
        'ip12': 'https://dataplane.org/vncrfb.txt',
        }
description = "dataplane-feeds"

def start(ip_feed, domain_feed, url_feed):
    print("Updating Dataplane DNS Lists...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '': #Comments in banlist.txt
                data = line.split("|")
                new_line = data[2].strip() + ">>>" + description.strip()+ "\n"
                ip_feed.write(new_line)
