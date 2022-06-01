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
import feed_connectors.dataplane
import feed_connectors.alienvault
import feed_connectors.phish_tank
import feed_connectors.open_phish
import feed_connectors.krisk_intel
import feed_connectors.sekuripy
import feed_connectors.abuse_ch
import feed_connectors.turris_cz
import feed_connectors.cruzit_blocklist
import feed_connectors.danger_rulez

# TODO
# https://www.maxmind.com/en/high-risk-ip-sample-list
# https://raw.githubusercontent.com/Neo23x0/signature-base/master/iocs/c2-iocs.txt
# https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.csv
# https://danger.rulez.sk/projects/bruteforceblocker/blist.php
# https://raw.githubusercontent.com/stamparm/aux/master/maltrail-static-trails.txt - very large
# http://www.urlvir.com/export-ip-addresses/ - Not seeing data

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
                #feed_connectors.vxvault_recent.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.viriback.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.dataplane.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.alienvault.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.phish_tank.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.open_phish.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.krisk_intel.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.sekuripy.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.abuse_ch.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.turris_cz.start(ip_feed, domain_feed, url_feed)
                #feed_connectors.cruzit_blocklist.start(ip_feed, domain_feed, url_feed)
                feed_connectors.danger_rulez.start(ip_feed, domain_feed, url_feed)




def dedup_data():
    file_list = ['main_ip_feed.txt', 'main_domain_feed.txt', 'main_url_feed.txt']
    helpers.dedup_iocs.start(file_list)


def main():
    get_data()
    dedup_data()


main()