import sys
import os
from pprint import pprint
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import logging

from ldclient_mobile import MobileLDClient, MobileConfig
from ldclient.util import log

root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

config = MobileConfig(sdk_key=os.environ.get("LAUNCHDARKLY_MOBILE_KEY"), evaluation_reasons=1, use_report=1, send_events=False)
user = { "key": "foo@bar.com" }
client = MobileLDClient(user=user, config=config)
pprint(vars(client.all_flags_state()))

pprint(client.variation('experimentation-cohort', None))
