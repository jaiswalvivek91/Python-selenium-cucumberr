#!/bin/bash
# Ensure the public directory exists
mkdir -p reports/public
# Clean up any stale index
rm -f reports/public/index.html
# Find last 50 directories named run-* under reports/public
runs=$(ls -1dt reports/public/run-* 2>/dev/null | head -n 50)
# Generate index.html
echo "<html><head><title>Allure Report Index</title></head><body>" \
&& echo "<h2>Latest Allure Reports</h2><ul>"
for dir in $runs; do
    name=$(basename "$dir")
    echo "<li><a href=\"$name/index.html\" target=\"_blank\">$name</a></li>"
done
echo "</ul></body></html>" > reports/public/index.html
