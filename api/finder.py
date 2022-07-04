from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        capital = dic.get("capital")
        country = dic.get("country")

        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            response = requests.get(url)
            data = response.json()
            capital = data[0]["capital"][0]
            country = country.title()
            message = f"The capital of {country} is {capital}."

        elif capital:
            url = f"https://restcountries.com/v3.1/capital/{capital}"
            response = requests.get(url)
            data = response.json()
            country = data[0]["name"]["common"]
            capital = capital.title()
            message = f"{capital} is the capital of {country}."

        else:
            message = "There has been an error."

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

        return