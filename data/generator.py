import kagglehub

# Download latest version
path = kagglehub.dataset_download("simeondee/brain-tumor-images-dataset")

print("Path to dataset files:", path)