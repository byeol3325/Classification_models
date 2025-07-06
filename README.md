# Installation
Follow these steps to set up the project locally.

## Prerequisites
Ensure you have **Anaconda** or **Miniconda** installed. This project uses a Conda environment for dependency management.

1. **Clone the repository:**
```
git clone https://github.com/byeol3325/Classification_models.git
cd Classification_models
```

2. **Create and activate the Conda environment:**

We recommend creating a dedicated Conda environment using the provided environment.yaml file to ensure all dependencies are correctly installed.
```
conda env create -f environment.yaml
conda activate 2dto3d
```

This command will create a new Conda environment named 2dto3d and install all the necessary libraries, including PyTorch with CUDA support (torch==2.5.1+cu121, torchvision==0.20.1+cu121, torchaudio==2.5.1+cu121), Hugging Face Transformers, PEFT.

