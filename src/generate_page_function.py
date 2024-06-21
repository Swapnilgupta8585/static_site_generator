from block_markdown import markdown_to_html_node
from extract_title_function import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path,'r') as f:
        markdown = f.read()
        print(markdown)

    with open(template_path,'r') as f2:
        template = f2.read()
        print(template)

    html= markdown_to_html_node(markdown).to_html()
    print(html)
   
    title = extract_title(markdown)
    print(title)

    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    print(page_content)
    directory = os.path.dirname(dest_path)
    print(directory)
    os.makedirs(directory,exist_ok=True)

    with open(dest_path,'w') as f3:
        print(dest_path)
        f3.write(page_content)
   

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    file_path = dir_path_content
    file_names = os.listdir(dir_path_content)
    
    
   
    for filename in file_names:
        file_path = os.path.join(file_path,filename)
        if os.path.isfile(file_path) and filename.endswith('md'):
            generate_page(file_path, template_path, os.path.join(dest_dir_path,f"{filename[:-3]}.html"))
            file_path = dir_path_content
        elif os.path.isdir(file_path):
            generate_page_recursive(file_path, template_path, os.path.join(dest_dir_path,f"{filename}"))
        
        





