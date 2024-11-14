import os

def generate_folder_structure(root_dir, output_file, target_dirs=[], exclude_dir=""): # define your target dir here ,For eg:target_dirs=["backend", "frontend"],exclude_dir="node_modules"
    """
    Generates a hierarchical folder structure for specified target directories and saves it to a file.

    Args:
        root_dir: The root directory to start from.
        output_file: The path to the output file.
        target_dirs: A list of target directories to scan.
        exclude_dir: The directory to exclude.
    """

    with open(output_file, "w") as f:
        def print_tree(dir_path, indent=""):
            """Recursively prints the folder structure."""
            for item in os.listdir(dir_path):
                full_path = os.path.join(dir_path, item)
                if os.path.isdir(full_path) and item != exclude_dir:
                    f.write(f"{indent}+---{item}\n")
                    print_tree(full_path, indent + "|   ")
                elif os.path.isfile(full_path):
                    f.write(f"{indent}|   {item}\n")

        for target_dir in target_dirs:
            target_path = os.path.join(root_dir, target_dir)
            if os.path.isdir(target_path):
                f.write(f"+---{target_dir}\n")
                print_tree(target_path, "|   ")

if __name__ == "__main__":
    root_dir = r"" ##pass your folder name here like (Desktop\ExampleFolder)
    output_file = os.path.join(root_dir, "folder_structure.txt")
    generate_folder_structure(root_dir, output_file)
    print(f"Folder structure saved to {output_file}")