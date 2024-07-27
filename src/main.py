from copy_static import remove_public_dir_content, copy_static
from generate_page_function import generate_page_recursive

def main():
    """
    Main function to execute the following steps:
    1. Clear existing content in the public directory.
    2. Copy static files from the source directory to the public directory.
    3. Generate pages recursively from the content directory using a template.
    """
    # Define paths
    file_path = "./static"          # Directory containing static files to be copied
    public_dir = "./public"        # Directory where static files will be copied
    from_path = "./content"        # Directory containing content files for page generation
    template_path = "./template.html"  # Path to the HTML template for page generation
    dest_path = "./public"         # Destination directory for the generated pages

    # Remove existing content in the public directory
    remove_public_dir_content(public_dir)
    
    # Copy static files from the source directory to the public directory
    copy_static(file_path, public_dir)
    
    # Generate pages recursively from the content directory using the provided template
    generate_page_recursive(from_path, template_path, dest_path)

# Execute the main function
main()

