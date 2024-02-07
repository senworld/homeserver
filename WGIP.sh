while true
do
	curl -s ipinfo.io/ip > ~/.wg/ip.txt
	sleep 3600
done
