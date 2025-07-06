# Installation
Follow these steps to set up the project locally.

## Prerequisites
Ensure you have **Anaconda** or **Miniconda** installed. This project uses a Conda environment for dependency management.

## Steps

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



# How to run

This section will guide you through getting the project up and running, from understanding the data structure to training and evaluating your models.

## Data structure

Your project expects a specific data organization. The core of your dataset should reside within a data directory, containing both your image files (.png, .jpg, etc.) and their corresponding lists.

```bash
data/
├── dataset/             # Contains your image files (.png, .jpg, etc.)
│   ├── image1.png
│   ├── image2.jpg
│   └── ...
├── trainval_data_list.txt  # List of image paths and labels for training/validation
└── test_data_list.txt      # List of image paths and labels for testing
```

These .txt files (trainval_data_list.txt and test_data_list.txt) are crucial. They define which image files belong to your training/validation and test sets, respectively, along with their associated class labels. You can open them to see their exact format and content. Your current code is built to read and process data based on this precise structure.

## Check your data distribution

Understanding your dataset's class distribution is vital, especially given the potential for class imbalance in real-world drawing datasets. We've provided a utility script to visualize this.

```
# To check the distribution of the default dataset (located in 'data/')
python check_dataset_distributed.py

# To check the distribution of a dataset in a different directory
python check_dataset_distributed.py --data_path your_data_dir
```

This script will:
- Analyze the class distribution within your trainval_data_list.txt and test_data_list.txt.
- Print a breakdown of sample counts for each class.
- Generate bar charts (train_distribution.png and test_distribution.png) in the project root, providing a clear visual representation of your dataset's balance.
