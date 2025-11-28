import requests


def get_inchikey(compound):
	session = requests.Session()
	session.headers.update({
			'User-Agent': 'ClassyFire Python Client/1.0 (contact@example.com)'
			})

	URL = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/property/InChIKey/TXT"

	try:
		response = session.get(URL)
		return response.text.rstrip()
	except requests.exceptions.RequestException as e:
		print(f"An general error occurred during the request: {e}")
		return None


if __name__ == "__main__":
	compound = "pyruvate"
	inchikey = get_inchikey(compound)
	print(inchikey)