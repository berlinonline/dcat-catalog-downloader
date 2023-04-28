# DCAT Catalog Downloader

Downloads DCAT RDF data from a DCAT catalog endpoint and merges it to query it locally.

## Requirements

- Python 3

## Installation

The easiest way to install the downloader is directly from this repository via `pip`.
You might want to do this in a dedicated virtual Python environment (_venv_), depending on your circumstances.
If you want to use the downloader locally on a machine that runs many different applications, using a venv is recommended.
If you want to use the downloader in a throwaway container (such as in a GitHub Actions workflow), the venv might not be necessary.
The following example uses a venv.

```shell
# Create a directory to work in
% mkdir dcat-catalog-downloader
% cd dcat-catalog-downloader

# Create a Python venv (virtual environment):
% python -m venv venv

# Activate the venv:
% . venv/bin/activate

# Install the downloader and its dependencies into the venv:
(venv) % pip install git+https://github.com/berlinonline/dcat-catalog-downloader.git
```

## Running the Downloader


## License

This material is copyright ©[BerlinOnline Stadtportal GmbH & Co. KG]( https://www.berlinonline.net/).

All software in this repository is published under the [MIT License](LICENSE).
