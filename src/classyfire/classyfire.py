import pandas as pd
import requests
import time
import logging

MAX_RETRIES = 5  # Limit the total number of attempts
INITIAL_WAIT_TIME = 2  # Start with a 2-second wait

##
logging.basicConfig(
    level=logging.INFO,            # or DEBUG for more detail
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
##

class ClassyFire:
	def __init__(self):
		self.session = requests.Session()
		self.URL = "http://classyfire.wishartlab.com"
		self.session.headers.update({
			'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
			})
		self.headers = ({
					'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
					})

	def process_response(self, url):
		response = None
		for attempt in range(MAX_RETRIES):
			try:
				response = requests.get(url=url, headers=self.headers)
				response.raise_for_status()
			except requests.exceptions.HTTPError as e:
				failed_response = e.response
				if failed_response.status_code == 404:
					logger.debug("Entity not found (404)")
					return None
				if failed_response.status_code == 429:
					wait_time = INITIAL_WAIT_TIME * (2 ** attempt)
					retry_after = response.headers.get("Retry-After")
					if retry_after:
						wait_time = int(retry_after)
						logger.debug(wait_time)
					if attempt + 1 == MAX_RETRIES:
						break
					time.sleep(wait_time)
					continue
			except requests.exceptions.Timeout as e:
				print("Timeout error")
				raise
			except requests.exceptions.RequestException as e:
				logger.debug("An general error occurred during the request: %s", e)
				return None

			results = response.json()
			return results

		
	def get_entity_classification(self, inchikey, format_type="json"):
		url = f"{self.URL}/entities/{inchikey}.{format_type}"
		res = self.process_response(url)
		return res


if __name__ == "__main__":
	from collections import defaultdict

	cf = ClassyFire()

	inchikey = "JVTAAEKCZFNVCJ-UHFFFAOYSA-N"
	cf_res = cf.get_entity_classification(inchikey)
	print(cf_res["class"])

	# An invalid key to test error handling
	inchikey_invalid = "INVALIDKEY-UHFFFAOYSA-N"
	cf_res = cf.get_entity_classification(inchikey_invalid)
	print(cf_res)

	##
	inchi_list = ["LCTONWCANYUPML-UHFFFAOYSA-M",
				  "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
				  "RYYVLZVUVIJVGH-UHFFFAOYSA-N",
				  "BSYNRYMUTXBXSQ-UHFFFAOYSA-N",
				  "INVALIDKEY-UHFFFAOYSA-N"]

	##
	saved_inchi = defaultdict(list)
	bad_inchi = defaultdict(list)

	for inchi in inchi_list:
		res = cf.get_entity_classification(inchi)
		if res is not None:
			print(res["class"])

			for k, v in res["class"].items():
				saved_inchi[k].append(v)
		if res is None:
			bad_inchi["inchikey"].append(inchi)
			bad_inchi["name"].append("unknown")
			logger.info("%s is bad", inchi)
	print(pd.DataFrame(saved_inchi))
	print(pd.DataFrame(bad_inchi))
