dist_bin_SCRIPTS = simqc simqgrep
dist_sbin_SCRIPTS = simqclean simtamaint
dist_pkglibexec_SCRIPTS = check-simta-expansion check-simta-queue check-simta-queue-age check-simta-queue-jailed check-simta-queue-ownership metrics-simta

EXTRA_DIST = 40simta.cron packaging/rpm/simta-admin.spec

rpm: dist-xz
	rpmbuild -ta $(distdir).tar.xz
