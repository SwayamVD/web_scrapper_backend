from selectorlib import Extractor
import requests 
from ScrapePRJ import settings


# Create an Extractor by reading from the YAML file
selectors_string = """
    name:
        css: '#productTitle'
        type: Text
    price:
        css: '.a-price-whole'
        type: Text
    
    images:
        css: '.imgTagWrapper img'
        type: Attribute
        attribute: src

    cashback:
        css: '#itembox-GCCashback'
        type: Text

    bank_offer:
        css: '#itembox-InstantBankDiscount .a-truncate-full'
        type: Text



    partner_offer:
        css: '#itembox-Partner .a-truncate-full'  
        type: Text

    rating:
        css: '#averageCustomerReviews .a-icon-alt'
        type: Text


    link_to_all_reviews:
        css: 'div.card-padding a.a-link-emphasis'
        type: Link

    availabiliy:
        css: '#availability'
        type: Text

    about_item:
        css: '#feature-bullets .a-unordered-list .a-list-item'
        multiple: true
        type: Text
"""


def scrape_amazon(url):  
    domain = get_domain(url)
    selector_path = settings.SELECTORS_CONFIG.get(domain,'myAPP/flip.yml')
    # e = Extractor.from_yaml_string(selectors_string)
    # e = Extractor.from_yaml_file('myAPP/selectors.yml')
    e = Extractor.from_yaml_file(selector_path)

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

def get_domain(url):
    return url.split('/')[2]