#!/usr/bin/env bash
set -e

# allow override of target URL
if [ -n "$TARGET_URL" ]; then
  echo "Using TARGET_URL=$TARGET_URL"
fi

# run pytest, produce junit xml for Jenkins
pytest -q --maxfail=1 --junitxml=results/junit.xml --html=results/report.html -n auto tests || true
# keep exit code 0 but capture failures by junit xml (Jenkins will interpret)
