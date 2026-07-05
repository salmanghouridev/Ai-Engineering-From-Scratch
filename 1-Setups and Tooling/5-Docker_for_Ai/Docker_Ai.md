Containers make "works on my machine" a thing of the past.


## Learning Objectives
- Build a GPU-enabled Docker image with CUDA, PyTorch, and AI libraries from a Dockerfile
- Mount host directories as volumes to persist models, datasets, and code across container rebuilds
- Configure the NVIDIA Container Toolkit to expose GPUs inside containers
- Orchestrate multi-service AI applications (inference server + vector database) using Docker Compose

## The Problem
You trained a model on your laptop with PyTorch 2.3, CUDA 12.4, and Python 3.12. Your colleague has PyTorch 2.1, CUDA 11.8, and Python 3.10. Your model crashes on their machine. Your Dockerfile works on both.

AI projects are dependency nightmares. A typical stack includes Python, PyTorch, CUDA drivers, cuDNN, system-level C libraries, and specialized packages like flash-attn that need exact compiler versions. Docker packages all of this into a single image that runs identically everywhere.

## Why AI projects need Docker more than most

- GPU drivers are fragile. CUDA 12.4 code does not run on CUDA 11.8. Docker isolates the CUDA toolkit inside the container while sharing the host GPU driver through the NVIDIA Container Toolkit.

- Model weights are large. A 7B parameter model is 14 GB in fp16. You do not want to re-download it every time you rebuild. Docker volumes let you mount a models directory from the host.

- Multi-service architectures are common. A real AI application is not just a Python script. It is an inference server, a vector database for RAG, maybe a web frontend. Docker Compose orchestrates all of these with one command.


## Exercises
- Build the Dockerfile and run python -c "import torch; print(torch.__version__)" inside the container
- Start the docker-compose stack and verify Qdrant is accessible from the AI container at http://qdrant:6333/collections
- Add flask to the Dockerfile, rebuild, and run a simple API server on port 5000. Map the port with -p 5000:5000
- Measure the image size with docker images. Try switching the base image from devel to runtime and compare sizes