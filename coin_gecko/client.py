import json
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class CoinGecko:

  def __init__(self) -> None:
    self.base_url = 'https://api.coingecko.com/api/v3'
    self.session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
    self.session.mount('http://', HTTPAdapter(max_retries=retries))

