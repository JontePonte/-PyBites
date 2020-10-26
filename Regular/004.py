
# Oly works in browser at PyBites because of tempfile


import os
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    # not a beautiful solution...
    content_list = content.split(">")
    content_striped = [item[:-10] for item in content_list if '</category' in item]
    
    counted = Counter(content_striped)
    
    return counted.most_common(n)

print(get_pybites_top_tags(10))
