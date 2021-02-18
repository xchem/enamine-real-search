from requests.utils import quote
import http.client
import json

class EnamineSession:
    def __init__(self, base_url='www.enaminestore.com'):
        """
        Sets up a session to search Enamine REAL space with. There are two options available: substructure search, or
        similarity search. After setting up a session (e.g. session = EnamineSession()), run a similarity search with
        session.similarity_search(smiles, threshold) or a substructure search with session.substructure_search(smiles)

        :param base_url: str
            the base url for the online enamine store. Default = www.enaminestore.com
        """

        self.base_url = base_url
        self.conn = http.client.HTTPSConnection(base_url)
        self.headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'Accept': 'application/json',
            'X-Prototype-Version': '1.7',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.enaminestore.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.enaminestore.com/search',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Content-Type': 'text/plain'
        }

    def run_request(self, search_ext, full_str):
        """
        Runs the actual requests from similarity search or substructure search.

        :param search_ext: str
            search extension on top of base url in class __init__
        :param full_str: str
            the encoded string to send as raw-data to the url
        :return: result
        """
        self.conn.request("POST", search_ext, full_str, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        result = data.decode("utf-8")
        try:
            r2 = json.loads(result)
            r3 = json.loads(r2['result'][0])
            list_of_mols = r3['data']
            return list_of_mols
        except:
            return result

    def similarity_search(self, smiles, threshold, search_ext="/search.realsearch:searchrealsendrequest"):
        """
        Performs a similarity search against Enamine Real based on a smiles string and similarity threshold
        :param smiles: str
            SMILES string to search for similar molecules of
        :param threshold: float
            value between 0 and 1, where 0 is no similarity, and 1 is an exact match
        :param search_ext:
        :return:
        """
        json_data = quote(f'{{"search":{{"query":"{smiles}","similarityThreshold":"{str(threshold)}"}}}}')
        full_str = f'controlPath=sim&jsonData={json_data}&PageSize=10000&reqMethod=POST'

        return self.run_request(search_ext=search_ext, full_str=full_str)

    def substructure_search(self, smiles, search_ext="/search.realsearch:searchrealsendrequest"):
        """
        Performs a substructure search based on an input molecule by smiles
        :param smiles: str
            SMILES string of substructure to search for
        :param search_ext:
        :return:
        """

        json_data = quote(f'{{"search":"{smiles}"}}')
        full_str = f'controlPath=sub&jsonData={json_data}&PageSize=10000&reqMethod=POST'

        return self.run_request(search_ext=search_ext, full_str=full_str)
