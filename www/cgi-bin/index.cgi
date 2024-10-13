#!/bin/sh

echo "Content-Type: text/html"
echo ""

#echo "${REMOTE_ADDR} - [$(date)] \"${REQUEST_METHOD} ${REQUEST_URI}\" \"${HTTP_REFERER}${REQUEST_URI}\" \"${HTTP_USER_AGENT}\"" >> ~/cgi/www/cgi-bin/log

echo "<h1>Download</h1>"
ls -a "..${REQUEST_URI#${SCRIPT_NAME}}" | while read line
do
	echo "<div><a href='$line'>$line</a></div>"
done

echo "<br/>"
echo "<hr/>"
echo "<br/>"

date 



