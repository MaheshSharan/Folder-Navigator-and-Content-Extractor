import os

def copy_folder_content(source_folders, output_file, exclude_paths=[]):
    """
    Copies the content of files from the specified source folders and their subdirectories to a single output file.

    Args:
        source_folders: A list of source folders to copy content from.
        output_file: The path to the output file.
        exclude_paths: A list of relative paths to exclude from copying.
    """
    with open(output_file, "w") as output:
        def copy_files(folder_path, relative_path=""):
            """Recursively copies file content with proper formatting."""
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                relative_item_path = os.path.join(relative_path, item) if relative_path else item

                if os.path.isdir(item_path):
                    if relative_item_path not in exclude_paths:
                        output.write(f"\n// {relative_item_path}/\n")
                        output.write("-" * 50 + "\n")  # Add a separator line
                        copy_files(item_path, relative_item_path)
                elif os.path.isfile(item_path):
                    if relative_item_path not in exclude_paths:
                        with open(item_path, "r") as file:
                            content = file.read()
                            output.write(f"\n// {relative_item_path}\n")
                            output.write(content + "\n")
                            output.write("-" * 50 + "\n")  # Add a separator line

        for source_folder in source_folders:
            copy_files(source_folder)

    print(f"Content copied to {output_file}")

if __name__ == "__main__":
    # User-defined source folders and exclude paths
    source_folders = [""] #eg:Frontend/src/components
    exclude_paths = []

    output_file = "code_snippets.txt"
    copy_folder_content(source_folders, output_file, exclude_paths)