import requests
import requests_cache
from time import sleep
from datetime import timedelta

requests_cache.install_cache("classyfire_cache", expire_after=timedelta(days=7))


def get_inchikey(compound):
	session = requests.Session()
	session.headers.update({
			'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
			})

	URL = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/property/InChIKey/TXT"

	try:
		response = session.get(URL)
		if response.raise_for_status():
			return None
		return response.text.rstrip().split()
	except requests.exceptions.RequestException as e:
		return None


def batch_get(compounds):
	batch_size = 20
	sleep_interval = 2
	results = []
	i = 0
	for start in range(0, len(compounds), batch_size):
		end = start + batch_size
		for compound in compounds[start:end]:
			result = get_inchikey(compound)
			if result:
				result = result[0]
			results.append(result)
			if i % 10 == 0:
				print(i)
			i += 1
		if end < len(compounds):
			sleep(sleep_interval)

	return results


if __name__ == "__main__":
	compound = "pyruvate"
	inchikey = get_inchikey(compound)
	print(inchikey)

	compounds_ = ["pyruvate", "fumarate", "succinate", "foobar"]

	res = batch_get(compounds_)
	print(res)
