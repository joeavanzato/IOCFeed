import os
import sqlite3

import requests

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


url_list = {}

url_list['maxmind_highrisk'] = 'https://www.maxmind.com/en/high-risk-ip-sample-list'
url_list['loki_signatures'] = 'https://raw.githubusercontent.com/Neo23x0/signature-base/master/iocs/c2-iocs.txt'

def main():
    with open('main_ip_feed.txt', 'w', encoding='utf8') as ip_feed:
        with open('main_domain_feed.txt','w', encoding='utf8') as domain_feed:
            with open('main_url_feed.txt','w', encoding='utf8') as url_feed:
                feed_connectors.binary_defense.start(ip_feed, domain_feed, url_feed)
                feed_connectors.botvrij.start(ip_feed, domain_feed, url_feed)
                feed_connectors.cinsscore_ci_badguys.start(ip_feed, domain_feed, url_feed)
                feed_connectors.greensnow.start(ip_feed, domain_feed, url_feed)
                feed_connectors.the_haleys_ssh.start(ip_feed, domain_feed, url_feed)
                feed_connectors.netlab_dgas.start(ip_feed, domain_feed, url_feed)
                feed_connectors.dshield.start(ip_feed, domain_feed, url_feed)
                feed_connectors.tweet_ioc.start(ip_feed, domain_feed, url_feed)
                feed_connectors.de_blocklist.start(ip_feed, domain_feed, url_feed)
                feed_connectors.tor_project.start(ip_feed, domain_feed, url_feed)
                feed_connectors.rutgers.start(ip_feed, domain_feed, url_feed)
                feed_connectors.emerging_threats.start(ip_feed, domain_feed, url_feed)
                feed_connectors.secops_institute.start(ip_feed, domain_feed, url_feed)
                feed_connectors.myip_blacklist.start(ip_feed, domain_feed, url_feed)
                feed_connectors.firehol.start(ip_feed, domain_feed, url_feed)
                feed_connectors.scriptzteam.start(ip_feed, domain_feed, url_feed)
                feed_connectors.talos.start(ip_feed, domain_feed, url_feed)
                feed_connectors.urlhaus.start(ip_feed, domain_feed, url_feed)

main()