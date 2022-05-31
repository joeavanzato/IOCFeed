import helpers.retrieve_txt

list = {'ip':'http://charles.the-haleys.org/ssh_dico_attack_hdeny_format.php/hostsdeny.txt'}
description = "the-haleys_ssh_attacks"

def start(ip_feed, domain_feed, url_feed):
    print("Updating the-haleys SSH Brute Force List...")
    for k,v in list.items():
        print(f"Checking: {v}")
        data = helpers.retrieve_txt.get_remote_text(v)
        ip_feed.write(f"#Source: {v}\n")
        for line in data.text.splitlines():
            if not line.startswith("#") and not line.startswith(' ') and not line == '':
                _, ioc = line.split(':')
                new_line = ioc.strip()+";"+description.strip()+"\n"
                ip_feed.write(new_line)