from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        BASE_URL = "https://restcountries.com/v3.1"
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        country = dic.get("country")
        capital = dic.get("capital")

        if country and capital:
            message = "Stretch goal coming soon"
        elif country:
            url = f"{BASE_URL}/name/{country}"
            r = requests.get(url)
            data = r.json()
            capitals = data[0]["capital"]
            joined_capitals = " and ".join(capitals)
            message = f"The capital of {country} is {joined_capitals}"
        elif capital:
            url = f"{BASE_URL}/capital/{capital}"
            r = requests.get(url)
            data = r.json()
            message = str(data)

        else:
            message = "Supply a country or capital please"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

        return