# Build Fluvio's docker image
echo "Building Docker image"
cd ./fluvio_config
docker compose up -d
cd ../

echo "Create topic" 
fluvio topic create

echo "Running the app"
# Run Pub/Sub
python producer.py &
python customer.py
