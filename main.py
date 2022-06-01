import os
import sqlite3

import requests

import helpers.dedup_iocs
import feed_connectors.binary_defense
import feed_connectors.botvrij
import feed_connectors.cinsscore_ci_badguys
import feed_connectors.greensnow
import feed_connectors.the_haleys_ssh
import feed_connectors.netlab_dgas
import feed_connectors.dshield
import feed_connectors.tweet_ioc
import feed_connectors.de_blocklist
import feed_connectors.tor_project
import feed_connectors.rutgers
import feed_connectors.emerging_threats
import feed_connectors.secops_institute
import feed_connectors.myip_blacklist
import feed_connectors.firehol
import feed_connectors.scriptzteam
import feed_connectors.talos
import feed_connectors.urlhaus
import feed_connectors.dan_me_tor
import feed_connectors.hoshadiq_mining
import feed_connectors.darklist
import feed_connectors.vxvault_recent
import feed_connectors.viriback

# TODO
# https://www.maxmind.com/en/high-risk-ip-sample-list
# https://raw.githubusercontent.com/Neo23x0/signature-base/master/iocs/c2-iocs.txt
# https://reputation.alienvault.com/reputation.generic
# https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.csv
# https://danger.rulez.sk/projects/bruteforceblocker/blist.php
# https://www.cruzit.com/xxwbl2txt.php
# https://dataplane.org/dnsrd.txt
# https://dataplane.org/dnsrdany.txt
# https://dataplane.org/dnsversion.txt
# https://dataplane.org/sipinvitation.txt
# https://dataplane.org/sipquery.txt
# https://dataplane.org/sipregistration.txt
# https://dataplane.org/smtpdata.txt
# https://dataplane.org/smtpgreet.txt
# https://dataplane.org/sshclient.txt
# https://dataplane.org/sshpwauth.txt
# https://dataplane.org/telnetlogin.txt
# https://dataplane.org/vncrfb.txt
# https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt
# http://sekuripy.hr/blacklist.txt
# https://kriskintel.com/feeds/ktip_malicious_domains.txt
# https://kriskintel.com/feeds/ktip_malicious_Ips.txt
# https://openphish.com/feed.txt
# http://data.phishtank.com/data/online-valid.csv
# https://sslbl.abuse.ch/blacklist/sslblacklist.csv
# https://raw.githubusercontent.com/stamparm/aux/master/maltrail-static-trails.txt
# https://view.sentinel.turris.cz/greylist-data/greylist-latest.csv
# http://tracker.viriback.com/dump.php
# http://www.urlvir.com/export-ip-addresses/

def get_data():
    with open('main_ip_feed.txt', 'w', encoding='utf8') as ip_feed:
        with open('main_domain_feed.txt','w', encoding='utf8') as domain_feed:
            with open('main_url_feed.txt','w', encoding='utf8') as url_feed:
                #feed_connectors.binary_defense.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.botvrij.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.cinsscore_ci_badguys.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.greensnow.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.the_haleys_ssh.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.netlab_dgas.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.dshield.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.tweet_ioc.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.de_blocklist.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.tor_project.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.rutgers.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.emerging_threats.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.secops_institute.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.myip_blacklist.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.firehol.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.scriptzteam.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.talos.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.urlhaus.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.dan_me_tor.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.hoshadiq_mining.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.darklist.start(ip_feed, domain_feed, url_feed)
                feed_connectors.vxvault_recent.start(ip_feed, domain_feed, url_feed)
                feed_connectors.viriback.start(ip_feed, domain_feed, url_feed)



def dedup_data():
    file_list = ['main_ip_feed.txt', 'main_domain_feed.txt', 'main_url_feed.txt']
    helpers.dedup_iocs.start(file_list)


def main():
    get_data()
    dedup_data()


main()