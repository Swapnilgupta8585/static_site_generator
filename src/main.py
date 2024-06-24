from copy_static import remove_public_dir_content,copy_static
from generate_page_function import generate_page_recursive

def main():
    
    file_path = "./static"
    public_dir = "./public"
    remove_public_dir_content(public_dir)
    copy_static(file_path, public_dir)
    from_path = "./content"
    template_path = "./template.html"
    dest_path = "./public"
    generate_page_recursive(from_path, template_path, dest_path)
main()
