ckan_base = https://datenregister.berlin.de
endpoint_name = catalog.ttl
dcat_endpoint = $(ckan_base)/$(endpoint_name)

data/temp/parts: data/temp
	@echo "creating $@ ..."
	@mkdir -p $@
	@echo "downloading all catalog pages to $@ ..."
	@download_catalog --endpoint $(dcat_endpoint) --output $@

data/output/catalog.ttl: data/temp/parts data/output
	@echo "merging all catalog pages in $< to $@ ..."
	@rdfpipe -i turtle -o turtle $</$(endpoint_name)* > $@

clean: clean-temp clean-output

clean-temp:
	@echo "deleting temp folder ..."
	@rm -rf data/temp

clean-output:
	@echo "deleting output folder ..."
	@rm -rf data/output

data/temp:
	@echo "creating $@ directory ..."
	@mkdir -p $@

data/output:
	@echo "creating $@ directory ..."
	@mkdir -p $@
