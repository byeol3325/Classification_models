# -*- coding: utf-8 -*-
"""
This script analyzes the distribution of classes in a dataset.
It reads lists of file paths for training, validation, and test sets,
counts the number of samples for each class, prints the distribution to the console,
and saves a bar chart visualization for each set.

This script is designed for public sharing on platforms like GitHub,
using anonymous class names and relative paths.
"""

import os
import argparse
from collections import Counter
import warnings

# Suppress UserWarning, often from external libraries.
warnings.filterwarnings("ignore", category=UserWarning)

# Attempt to import matplotlib for plotting.
try:
    import matplotlib
    import matplotlib.pyplot as plt
    # Configure matplotlib for consistent plotting.
    # Ensures minus signs are rendered correctly.
    matplotlib.rcParams['axes.unicode_minus'] = False
    # Use a default font that supports English characters.
    matplotlib.rcParams['font.family'] = 'DejaVu Sans'
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Warning: matplotlib is not installed. Chart generation will be skipped.")
    print("You can install it by running: pip install matplotlib")

# --- Configuration ---
# Note: We're using dynamic class discovery, so no pre-defined class list is needed


def count_classes(file_path, split_name):
    """
    Counts class distribution from a given file list and saves a bar chart.

    Args:
        file_path (str): The path to the text file containing the list of data files.
        split_name (str): The name of the data split (e.g., 'Train', 'Validation', 'Test').
    """
    # Check if the data list file exists before proceeding.
    if not os.path.exists(file_path):
        print(f"--> Warning: Data list file not found at '{file_path}'. Skipping '{split_name}' set.\n")
        return

    # Read CSV file with file paths and class names using UTF-8 encoding.
    file_list = []
    class_list = []
    unique_classes = set()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        # Skip header line if it exists
        first_line = f.readline().strip()
        if first_line.startswith('file_path') or first_line.startswith('file_name'):
            # File has a header, continue with next lines
            pass
        else:
            # No header, process the first line too
            parts = first_line.split(',')
            if len(parts) >= 2:
                file_path_item = parts[0].strip()
                class_name = parts[1].strip()
                
                file_list.append(file_path_item)
                class_list.append(class_name)
                unique_classes.add(class_name)
        
        # Process remaining lines
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                file_path_item = parts[0].strip()
                class_name = parts[1].strip()
                
                file_list.append(file_path_item)
                class_list.append(class_name)
                unique_classes.add(class_name)
    
    # Convert set to sorted list for consistent ordering
    class_names_sorted = sorted(list(unique_classes))
    
    # Count occurrences of each class
    class_counts = Counter(class_list)

    print(f"--- [{split_name} set] Class Distribution ---")
    if not class_counts:
        print("  No data found.\n")
        return

    # Determine the count of the most frequent class for scaling the bar visual.
    max_count = max(class_counts.values())

    # Print the counts and a simple text-based bar for each class.
    for cname in class_names_sorted:
        count = class_counts.get(cname, 0)
        # Scale the bar length relative to the max count for better visualization.
        bar_length = int((count / max_count * 30)) if max_count > 0 else 0
        bar = '#' * bar_length
        print(f"  {cname:15}: {count:4d} | {bar}")
    print()

    # If matplotlib is available, generate and save a bar chart.
    if MATPLOTLIB_AVAILABLE:
        plt.figure(figsize=(10, 6))
        counts_list = [class_counts.get(cname, 0) for cname in class_names_sorted]
        plt.bar(class_names_sorted, counts_list, color='skyblue', label='Number of samples')
        
        # Add count numbers on top of each bar.
        for i, count in enumerate(counts_list):
            plt.text(i, count + (max_count * 0.01), str(count), ha='center')

        plt.title(f"'{split_name}' Set - Sample Distribution per Class")
        plt.xlabel("Class Name")
        plt.ylabel("Number of Samples")
        plt.ylim(top=max_count * 1.1) # Add some space at the top
        plt.tight_layout()
        
        # Save the chart to a PNG file.
        output_filename = f"{split_name.lower()}_distribution.png"
        plt.savefig(output_filename)
        plt.close()
        print(f"--> Saved bar chart to '{output_filename}'\n")


def main():
    """
    Main function to parse arguments and run the dataset distribution check.
    
    Example execution from the command line:
    
    1. To run with default settings (looking for list files in the data directory):
       python check_dataset_distributed.py
       
    2. To specify a different directory where the list files are located:
       python check_dataset_distributed.py --data_path custom_data_dir
       
    This will process 'train_data_list.txt', 'val_data_list.txt', and 'test_data_list.txt'
    found in the specified directory.

    command line example:
        python check_dataset_distributed.py --data_path data
    """
    # Setup argument parser to handle command-line arguments.
    parser = argparse.ArgumentParser(
        description='Analyzes and visualizes the class distribution of a dataset.',
        formatter_class=argparse.RawTextHelpFormatter # To preserve formatting in help text.
    )
    parser.add_argument(
        '--data_path',
        type=str,
        default='data',
        help='Path to the directory containing the data list files (e.g., train_data_list.txt).\nDefaults to the data directory.'
    )
    args = parser.parse_args()

    print(f"Starting dataset analysis in: {os.path.abspath(args.data_path)}\n")
    print("Using dynamic class discovery - classes will be found while reading data files\n")

    # Define the file names for each data split based on available files.
    data_lists = {
        'TrainVal': 'trainval_data_list.txt',  # Combined train and validation data
        'Test': 'test_data_list.txt'
    }

    # Iterate through each data split and analyze its class distribution.
    for split_name, file_name in data_lists.items():
        file_path = os.path.join(args.data_path, file_name)
        count_classes(file_path, split_name)

    print("--- Analysis complete. ---")


if __name__ == '__main__':
    # This block ensures the main function is called only when the script is executed directly.
    main()
