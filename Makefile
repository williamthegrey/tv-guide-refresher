version_file = VERSION
version = $(shell cat $(version_file))
lib_dir = Contents/Libraries
shared_lib_dir = Shared
dist_dir = dist
bundle_dir = tv-guide-refresher.bundle
archive_name = tv-guide-refresher-$(version).bundle.zip

all:
	mkdir -p $(lib_dir)/$(shared_lib_dir)
	pip2 install -t $(lib_dir)/$(shared_lib_dir) -r requirements.txt
	mkdir -p $(dist_dir)/$(bundle_dir)
	cp -r Contents $(dist_dir)/$(bundle_dir)
	cp $(version_file) $(dist_dir)/$(bundle_dir)
	cp README.md $(dist_dir)/$(bundle_dir)
	( cd $(dist_dir) && zip -r $(archive_name) $(bundle_dir) )
	rm -rf $(dist_dir)/$(bundle_dir)

clean:
	rm -rf $(dist_dir)
	rm -rf $(lib_dir)
