import os, requests

import feed_connectors.binary_defense
import feed_connectors.botvrij
import feed_connectors.cinsscore_ci_badguys


def main():
    with open('main_ip_feed.txt', 'w') as ip_feed:
        with open('main_domain_feed.txt','w') as domain_feed:
            with open('main_url_feed.txt','w') as url_feed:
                feed_connectors.binary_defense.start(ip_feed, domain_feed, url_feed)
                feed_connectors.botvrij.start(ip_feed, domain_feed, url_feed)


main()