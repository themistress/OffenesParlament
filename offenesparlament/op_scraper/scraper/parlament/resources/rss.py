import feedparser
import roman
from parlament.settings import BASE_URL
from parlament.settings import URLOPTIONS
from parlament.settings import LLP
from urllib import urlencode
# sample link for single law
# http://www.parlament.gv.at/PAKT/VHG/XXV/I/I_00458/index.shtml


def get_laws_url(GP="XXV"):
    """
    Returns the RSS url for the requested Gesetzgebungsperiode
    """
    options = URLOPTIONS.copy()
    options['GP'] = GP

    url_options = urlencode(options)
    laws_url = "{}?{}".format(BASE_URL, url_options)
    return laws_url


def get_urls():
    urls = []
    for i in LLP:
        roman_numeral = roman.toRoman(i)
        rss = feedparser.parse(get_laws_url(roman_numeral))
        print "GP {}: {} laws".format(roman_numeral, len(rss['entries']))
        urls = urls + [entry['link'] for entry in rss['entries']]
    return urls
