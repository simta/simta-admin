dist_bin_SCRIPTS = simqc simqgrep simtrans
dist_sbin_SCRIPTS = simqclean simtamaint

EXTRA_DIST = 40simta.cron packaging/rpm/simta-admin.spec

rpm: dist-gzip
	rpmbuild -ta $(distdir).tar.gz
