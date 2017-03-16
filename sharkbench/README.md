** To test easily with shark about the response time locally and remotely

dd if=/dev/random of="sample.txt bs=1G count=1"

for i in `seq 1 1000`; 
do 
curl -m 10 -k -sL -w " %{http_code} %{time_connect} %{time_total} " -X PUT http://172.28.162.21/486a4c59-ce8f-ed73-abc8-82b44afaa4f2/6bb9f19e-c559-4205-8290-e5a754c0a4ec -d @sample.txt
echo ""
done
