lib_dir = Contents/Libraries
shared_lib_dir = Shared
dist_dir = dist
bundle_dir = tv-guide-refresher.bundle
archive_name = tv-guide-refresher.bundle.tar.gz

all:
	mkdir -p $(lib_dir)/$(shared_lib_dir)
	pip install -t $(lib_dir)/$(shared_lib_dir) -r requirements.txt
	mkdir -p $(dist_dir)/$(bundle_dir)
	cp -r Contents $(dist_dir)/$(bundle_dir)
	( cd $(dist_dir) && tar -czf $(archive_name) $(bundle_dir) )
	rm -rf $(dist_dir)/$(bundle_dir)

clean:
	rm -rf $(dist_dir)
	rm -rf $(lib_dir)
