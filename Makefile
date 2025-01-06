start-local:
	scripts/start-local.sh

check-links:
	scripts/check-links.sh

check-markers:
	scripts/check_merge_conflict_markers.sh .

check-all:
	scripts/check-links.sh
	echo "Echo checking for conflict markers"
	scripts/check_merge_conflict_markers.sh .
