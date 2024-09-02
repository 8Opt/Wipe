echo "Stop fluvio" 
cd ./fluvio_config
docker compose down

echo "Remove fluvio-data & fluvio-metadata"
rm -rf fluvio-data fluvio-metadata
