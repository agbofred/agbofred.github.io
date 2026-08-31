import urllib.parse

def make_orca_link(target_url):
    base_orca_api = "https://orcascan.com"
    # This safely converts characters like '?' and '=' into '%3F' and '%3D'
    encoded_target = urllib.parse.quote_plus(target_url)
    
    return base_orca_api + encoded_target

# Example Usage:
my_link = "https://jedrembold.prof/daily"
print(make_orca_link(my_link))
