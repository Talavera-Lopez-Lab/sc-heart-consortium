import os
import shutil

# Define the source directory where your folders are located
source_dir = '/Volumes/LaCie/heart_consortium/hubmap'

# Define the destination directory where you want to copy the files
destination_dir = '/Volumes/LaCie/heart_consortium/sc_cell/sc_rna/hubmap'

# Mapping of prefixes to file types based on the provided table
file_types = {
    'HBM236': 'snRNAseq [Salmon]',
    'HBM296': 'sciRNAseq [Salmon]',
    'HBM342': 'sciRNAseq [Salmon]',
    'HBM364': 'sciRNAseq [Salmon]',
    'HBM385': 'sciRNAseq [Salmon]',
    'HBM537': 'snRNAseq [Salmon]',
    'HBM563': 'sciRNAseq [Salmon]',
    'HBM573': 'sciRNAseq [Salmon]',
    'HBM592': 'sciRNAseq [Salmon]',
    'HBM599': 'sciRNAseq [Salmon]',
    'HBM852': 'sciRNAseq [Salmon]',
    'HBM927': 'sciRNAseq [Salmon]',
    'HBM943': 'sciRNAseq [Salmon]',
    'HBM957': 'snRNAseq [Salmon]',
    'HBM982': 'sciRNAseq [Salmon]'
}

# Loop through each folder in the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    
    # Check if the folder path is a directory
    if os.path.isdir(folder_path):
        # Extract the prefix (e.g., HBM236) from the folder name
        prefix = folder_name.split('.')[0]
        
        # Check if the prefix exists in the file_types dictionary
        if prefix in file_types:
            # Determine the file type based on the prefix
            data_type = file_types[prefix]
            
            # Construct the new file name based on the prefix and data type
            if data_type == 'snRNAseq [Salmon]':
                new_filename = f"{prefix}_snn_snr_hubmap.h5ad"
            elif data_type == 'sciRNAseq [Salmon]':
                new_filename = f"{prefix}_sc_rna_hubmap.h5ad"
            else:
                continue  # Skip folders that don't match the expected pattern
            
            # Find the raw_expr.h5ad file in the folder
            files = os.listdir(folder_path)
            for file in files:
                if file.endswith('raw_expr.h5ad'):
                    raw_expr_file = os.path.join(folder_path, file)
                    
                    # Copy the file to the destination directory with the new name
                    destination_path = os.path.join(destination_dir, new_filename)
                    shutil.copyfile(raw_expr_file, destination_path)
                    
                    # Print confirmation message
                    print(f"Copied {raw_expr_file} to {destination_path}")
                    break  # Stop searching for files once raw_expr.h5ad is found