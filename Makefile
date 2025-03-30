# Docker image name
IMAGE_NAME := my-app
CONTAINER_NAME := my-app

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run --name $(CONTAINER_NAME) -d -p 5000:5000 $(IMAGE_NAME)

remove:
	docker image rm -f $(IMAGE_NAME)

# Clean up the container
clean:
	docker rm -f $(CONTAINER_NAME)

helm-tmp:
	helm dependency build
	helm template my-app deployment/.
