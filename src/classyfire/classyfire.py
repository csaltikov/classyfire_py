import requests
import pandas as pd


class ClassyFire:
	def __init__(self):
		self.session = requests.Session()
		self.URL = "http://classyfire.wishartlab.com"
		self.session.headers.update({
			'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
			})
		self.headers =({
					'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
					})

	def process_response(self, url):
		try:
			response = requests.get(url=url, headers=self.headers)
			if response.status_code == 404:
				print("Entity not found (404)")
				return None
			response.raise_for_status()
			results = response.json()
			return results
		except requests.exceptions.RequestException as e:
			print(f"An general error occurred during the request: {e}")
			return None
		
	def get_entity_classification(self, inchikey, format_type="json"):
		url = f"{self.URL}/entities/{inchikey}.{format_type}"
		res = self.process_response(url)
		return res


if __name__ == "__main__":
	cf = ClassyFire()
	inchikey = "JVTAAEKCZFNVCJ-UHFFFAOYSA-N"

	# An invalid key to test error handling
	inchikey_invalid = "INVALIDKEY-UHFFFAOYSA-N" 

	cf_res = cf.get_entity_classification(inchikey)
	print(cf_res["class"])
	cf_res = cf.get_entity_classification(inchikey_invalid)
	print(cf_res)