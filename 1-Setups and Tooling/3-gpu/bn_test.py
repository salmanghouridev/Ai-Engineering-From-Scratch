import torch
import time

size = 5000

# Use Apple GPU (MPS) if available, otherwise CPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# Create two random matrices on the chosen device
a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)

# Wait for GPU to finish before timing
if device.type == "mps":
    torch.mps.synchronize()

# Start timer
start = time.time()

# Matrix multiplication
c = a @ b

# Wait again so timing is accurate
if device.type == "mps":
    torch.mps.synchronize()

# Print elapsed time
elapsed = time.time() - start
print(f"{device.type.upper()}: {elapsed:.3f}s")
