import argparse
import logging
from pathlib import Path
from rdflib import Graph, Namespace, URIRef
import urllib.request 

logging.basicConfig(level=logging.INFO)
HYDRA = Namespace("http://www.w3.org/ns/hydra/core#")

class DCATCatalogDownloader:

    def last_page_index(self)->int:
        first_page = URIRef(f"{self.endpoint}?page=1")
        last_page = self.graph.value(first_page, HYDRA.lastPage)
        last_page_index = last_page.split("=").pop()
        return int(last_page_index)

    def page_through_catalog(self):
        logging.info(f"Reading first catalog page from {self.endpoint} ...")
        self.graph.parse(self.endpoint)

        _last_page_index = self.last_page_index()
        logging.info(f"Last page is {_last_page_index} ...")

        endpoint_name = self.endpoint.split("/").pop()

        page_path = self.output_folder / f"{endpoint_name}?page=1"
        self.graph.serialize(destination=page_path)

        for index in range(2, _last_page_index+1):
            page_url = f"{self.endpoint}?page={index}"
            page_path = self.output_folder / f"{endpoint_name}?page={index}"
            logging.info(f"Saving catalog page: {page_url} to {page_path}")
            urllib.request.urlretrieve(page_url, page_path)


            # self.graph = Graph()
            # self.graph.parse(page_url)
            # self.graph.serialize(destination=page_path)

    def init_parser(self):
        parser = argparse.ArgumentParser(
            description="Page through the DCAT-catalog endpoint of CKAN instance and save all pages into an output folder.")
        parser.add_argument('--endpoint',
                            required=True,
                            help="Endpoint URL of the CKAN's DCAT catalog, e.g. https://datenregister.berlin.de/catalog.ttl.")
        parser.add_argument('--output',
                            help="Path to the output folder containing the catalog pages",
                            type=Path,
                            default=Path('data/temp')
                            )

        return parser

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        parser = self.init_parser()
        args = parser.parse_args()
        self.endpoint = args.endpoint
        self.output_folder = args.output
        self.graph = Graph()

    def run(self):
        self.page_through_catalog()

