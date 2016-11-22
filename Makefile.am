dist_bin_SCRIPTS = simqc simqgrep simtrans
dist_sbin_SCRIPTS = simqclean simtamaint

EXTRA_DIST = 40simta.cron packaging/rpm/simta-admin.spec

rpm: dist-xz
	rpmbuild -ta $(distdir).tar.xz
