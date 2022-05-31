import os, requests

import feed_connectors.binary_defense
import feed_connectors.botvrij
import feed_connectors.cinsscore_ci_badguys
import feed_connectors.greensnow
import feed_connectors.the_haleys_ssh
import feed_connectors.netlab_dgas
import feed_connectors.dshield

url_list = {}
url_list['blocklist_de'] = 'http://lists.blocklist.de/lists/all.txt'
url_list['malcode'] = 'http://malc0de.com/bl/IP_Blacklist.txt'
url_list['rutgers'] = 'http://report.rutgers.edu/DROP/attackers'
url_list['emergingthreats_ciarmy'] = 'http://rules.emergingthreats.net/blockrules/emerging-ciarmy.rules'
url_list['emergingthreats_compromised'] = 'http://rules.emergingthreats.net/blockrules/emerging-compromised.rules'
url_list['emergingthreats_fwrules'] = 'http://rules.emergingthreats.net/fwrules/emerging-PF-CC.rules'
url_list['emergingthreats_bots'] = 'http://rules.emergingthreats.net/open/suricata/rules/botcc.rules'
url_list['emergingthreats_compromised2'] = 'http://rules.emergingthreats.net/open/suricata/rules/compromised-ips.txt'
url_list['sblam_blacklist'] = 'https://sblam.com/blacklist.txt'
url_list['tor_exits'] = 'https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst'
url_list['tor_nodes'] = 'https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst'
url_list['binary_defense'] = 'https://www.binarydefense.com/banlist.txt'
url_list['maxmind_highrisk'] = 'https://www.maxmind.com/en/high-risk-ip-sample-list'
url_list['myip_blacklist'] = 'https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt'
url_list['firehol_proxies'] = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/proxyspy_1d.ipset'
url_list['scriptzteam_badips'] = 'https://raw.githubusercontent.com/scriptzteam/badIPS/main/ips.txt'
url_list['talos_intel'] = 'https://www.talosintelligence.com/documents/ip-blacklist'
url_list['torproject'] = 'https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1'
url_list['urlhaus_urls'] = 'https://urlhaus.abuse.ch/downloads/text/'
url_list['loki_signatures'] = 'https://raw.githubusercontent.com/Neo23x0/signature-base/master/iocs/c2-iocs.txt'

def main():
    with open('main_ip_feed.txt', 'w') as ip_feed:
        with open('main_domain_feed.txt','w') as domain_feed:
            with open('main_url_feed.txt','w') as url_feed:
                feed_connectors.binary_defense.start(ip_feed, domain_feed, url_feed)
                feed_connectors.botvrij.start(ip_feed, domain_feed, url_feed)
                feed_connectors.cinsscore_ci_badguys.start(ip_feed, domain_feed, url_feed)
                feed_connectors.greensnow.start(ip_feed, domain_feed, url_feed)
                feed_connectors.the_haleys_ssh.start(ip_feed, domain_feed, url_feed)
                feed_connectors.netlab_dgas.start(ip_feed, domain_feed, url_feed)
                feed_connectors.dshield.start(ip_feed, domain_feed, url_feed)


main()