import os

# Create the original file to rename
with open('old_name.txt', 'w') as f:
    f.write("This is a test file.")

# write a new function to rename files
def rename_file(directory, old_name, new_name):
    try:
        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            if old_name in filename:  # Check if the file matches the old_name
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, filename.replace(old_name, new_name))
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
    except FileNotFoundError:
        print("The specified directory or file does not exist.")
    except PermissionError:
        print("Permission denied. Ensure you have the right permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")
