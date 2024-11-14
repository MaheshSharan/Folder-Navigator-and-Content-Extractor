# Folder-Navigator-and-Content-Extractor

> Because life's too short to scroll through directories

## 📖 Overview

Welcome to Folder-Navigator-and-Content-Extractor, a Python toolkit that revolutionizes your development workflow. With two powerful scripts, we make it effortless to explore and share your project's code.

### Key Features

- 🌳 **Folder Structure Visualization:** Generate a hierarchical folder structure to understand your project layout at a glance
- 📄 **Content Extraction:** Consolidate code snippets from your project into a single file - ideal for sharing or creating comprehensive AI prompts for better project analysis

## 🚀 Usage

### Folder Structure Visualization

```python
root_dir = "your_project_root"
target_dirs = ["folder1", "folder2"]
exclude_dir = "node_modules"

# Generate folder structure
generate_folder_structure(root_dir, "folder_structure.txt", target_dirs, exclude_dir)
```

### Content Extraction

```python
source_folders = ["src", "lib"]
exclude_paths = ["src/tests", "lib/old_code.py"]
output_file = "code_snippets.txt"

# Extract content
extract_folder_content(source_folders, output_file, exclude_paths)
```

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, new features, or improved documentation, your input is valuable. Please open issues and submit pull requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚙️ Configuration

Both scripts can be customized through various parameters:

### Folder Structure Generator
- `root_dir`: Root directory to start scanning
- `target_dirs`: List of specific directories to include
- `exclude_dir`: Directories to exclude from scanning

### Content Extractor
- `source_folders`: List of folders to extract content from
- `exclude_paths`: Paths to exclude from extraction
- `output_file`: Destination file for extracted content



---

<div align="center">
Thanks for checking out our project! Feel free to use and contribute 🚀
</div>
