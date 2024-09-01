# Build Fluvio's docker image
cd ./fluvio_config
docker-compose up -d
cd ../

# Run Pub/Sub
python producer.py &
python consumer.py
