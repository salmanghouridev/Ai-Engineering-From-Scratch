Every AI model is just matrix math wearing a fancy hat.


## Learning Objectives

- Implement vector and matrix operations (addition, dot product, matrix multiply) from scratch in Python
- Explain geometrically what the dot product, projection, and Gram-Schmidt process do
- Determine linear independence, rank, and basis of a set of vectors using row reduction
- Connect linear algebra concepts to their AI applications: embeddings, attention scores, and LoRA


## The Problem

Open any ML paper. Within the first page, you'll see vectors, matrices, dot products, and transformations. Without linear algebra intuition, these are just symbols. With it, you can see what a neural network is actually doing -- moving points around in space.

You don't need to be a mathematician. You need to see what these operations mean geometrically, then code them yourself.


## The syllabus
If your goal is AI engineering, learn these in this order:

1. Vectors and norms: what data looks like in numeric form.
2. Dot product and cosine similarity: how models measure similarity.
3. Matrix multiplication: how layers and transformations work.
4. Systems : the shape of many optimization and fitting problems.
5. Linear independence, span, basis, rank: how to reason about information content.
6. Projection and orthogonality: the foundation of regression and PCA.
7. Eigenvalues and eigenvectors: directions a transformation preserves, crucial for PCA and stability.
8. SVD: the most useful decomposition in practice for compression, approximation, and LoRA intuition.
9. Tensors: how modern deep learning frameworks store batches, images, and sequences.
10. Attention as linear algebra: the heart of transformers.


## Concepts in plain language

###  Norm and distance
A norm is the size of a vector, and distance tells you how far apart two vectors are. In AI, norms help regularization, nearest-neighbor search, and optimization stability.

### Orthogonality
Orthogonal vectors are perpendicular, which means they do not overlap in the geometric sense. This matters because orthogonal directions carry distinct information, and orthonormal bases make computation more stable.

### Eigenvalues and eigenvectors
These are the special directions a transformation stretches without changing direction. They matter because PCA uses them to find the most informative directions in data, and stability analysis often depends on them.

### SVD
SVD breaks a matrix into simple pieces and reveals which directions carry most of the information. It is widely useful for compression, denoising, low-rank approximation, latent structure discovery, and LoRA-style parameter reduction.


## A mental model

Imagine a sentence enters an embedding model as tokens, each token becomes a vector, attention compares vectors using dot products, and each layer applies learned matrix transformations until the representation is useful for prediction. That full pipeline is mostly linear algebra plus nonlinear activations.

If you remember only one sentence, remember this: AI models learn useful transformations of vectors in high-dimensional spaces.

### What to practice
- Add, scale, and normalize vectors.
- Compute dot products and cosine similarity.
- Multiply matrices and track shapes carefully.
- Solve small systems .
- Check rank and linear dependence.
- Visualize projections in 2D.
- Learn PCA and SVD with NumPy.
- Implement one dense layer and one attention head from scratch.