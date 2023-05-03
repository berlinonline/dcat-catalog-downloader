# DCAT Catalog Downloader

## TL;DR

 Download and merge DCAT RDF data from a DCAT catalog endpoint to query it locally.

## Description

The [ckanext-dcat](https://github.com/ckan/ckanext-dcat) extension implements a [DCAT](https://www.w3.org/TR/vocab-dcat-3/) metadata export for [CKAN](https://ckan.org).
Among other things, it implements a [catalog endpoint](https://github.com/ckan/ckanext-dcat#catalog-endpoint) to download CKAN's dataset metadata as RDF.
The output of the catalog endpoint is paged, and there is no way to download the complete metadata dump at once.
Also, CKAN and `ckanext-dcat` have no SPARQL endpoint to query the metadata online.

The DCAT Catalog Downloader makes it easier to query the DCAT data from a CKAN instance by paging through the catalog endpoint, downloading each page and merging it.

The repository contains:

- a Python-based command line tool `download_catalog` that pages through the DCAT catalog endpoint to download the complete catalog
- a [Makefile](Makfile) to orchestrate downloading and merging the data
- a handful of [SPARQL queries](queries) that you can run on the downloaded data

## Requirements

- **Python 3** for the downloader
- To query RDF data locally, you need an **RDF framework with SPARQL capabilities**.
The excellent [rdflib](https://rdflib.readthedocs.io) library that is installed as a dependency of the downloader lets you use SPARQL on local data files, so you could [just use that](https://rdflib.readthedocs.io/en/stable/intro_to_sparql.html "Documentation for using SPARQL with the Python library rdflib").
I prefer to use the Java-based [Apache Jena](https://jena.apache.org), because it is very performant and comes with a range of useful command line tools.
Some package managers offer packaged versions of Jena. E.g., on Mac OS you can use homebrew to install Jena: `brew install jena`.


## Installing the Downloader

- Clone the repository:

```
$ git clone https://github.com/berlinonline/dcat-catalog-downloader
```

- Create and activate a Python virtual environment:

```
$ cd dcat-catalog-downloader
$ python -m venv venv
$ . venv/bin/activate
```

- Install the required python libraries:

```
(venv) $ pip install -r requirements.txt
```

- Install the command line tool:

```
(venv) $ python setup.py develop
```

## Running the Downloader

You now have the downloader available as a command line tool.

```
(venv) $ download_catalog --help                                                             
usage: download_catalog [-h] --endpoint ENDPOINT [--output OUTPUT]

Page through the DCAT-catalog endpoint of CKAN instance and save all pages into an output folder.

options:
  -h, --help           show this help message and exit
  --endpoint ENDPOINT  endpoint URL of the CKAN's DCAT catalog, e.g. https://datenregister.berlin.de/catalog.ttl
  --output OUTPUT      path to the output folder containing the catalog pages. Default is data/temp.
```

You can either use the downloader directly or use the Makefile to create a folder structure, download the data and merge it to a specific location.

```
(venv) $ make data/output/catalog.ttl                                                                
creating data/temp directory ...
creating data/temp/parts ...
downloading all catalog pages to data/temp/parts ...
INFO:root:Reading first catalog page from https://datenregister.berlin.de/catalog.ttl ...
INFO:root:Last page is 33 ...
INFO:root:Saving catalog page: https://datenregister.berlin.de/catalog.ttl?page=2 to data/temp/parts/catalog.ttl?page=2
INFO:root:Saving catalog page: https://datenregister.berlin.de/catalog.ttl?page=3 to data/temp/parts/catalog.ttl?page=3
...
INFO:root:Saving catalog page: https://datenregister.berlin.de/catalog.ttl?page=32 to data/temp/parts/catalog.ttl?page=32
INFO:root:Saving catalog page: https://datenregister.berlin.de/catalog.ttl?page=33 to data/temp/parts/catalog.ttl?page=33
creating data/output directory ...
merging all catalog pages in data/temp/parts to data/output/catalog.ttl ...
```

The Makefile downloads from https://datenregister.berlin.de.
If you want to download from a different CKAN instance, you need to change `ckan_base` variable at the top of the file. 

## Querying the Data

How you run a query depends on which SPARQL engine you have installed.
If you have Jena, you can use the [`sparql` command line tool](https://jena.apache.org/documentation/tools/index.html#sparql-queries-on-local-files-and-endpoints).
There are some queries that come as part of the repository, which you can just use.
Or you write your own queries, of course.

```
$ sparql --data data/output/catalog.ttl --query queries/distinct_authors.rq --results=csv
publisher
 Bezirksamt Friedrichshain-Kreuzberg von Berlin - Vermessung
Abt. III C - Freiraumplanung und Stadtgrün
Abteilung II - Integrativer Umweltschutz
Amt für Statistik Berlin-Brandenburg
Berlin.de
BerlinOnline Stadtportal GmbH & Co KG
BerlinOnline Stadtportal GmbH & Co. KG
Berliner Feuerwehr
Berliner Forsten
Berliner Stadtreinigung (BSR)
Berliner Umweltportal
...
Statistisches Landesamt Bremen
Stromnetz Berlin GmbH
Tegel Projekt GmbH
Tegel Projekt GmbH - Urban Data & Plattform
VBB - Verkehrsverbund Berlin-Brandenburg GmbH
Verkehrslenkung Berlin
WISTA Management GmbH
openstreetmap.org
```


## License

This material is copyright ©[BerlinOnline Stadtportal GmbH & Co. KG]( https://www.berlinonline.net/).

All software in this repository is published under the [MIT License](LICENSE).
