from block_markdown import markdown_to_html_node
from extract_title_function import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print("======================================================================")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    print("======================================================================")
    # read the content of markdown file
    with open(from_path,'r') as f:
        markdown = f.read()
    # read the content of template file
    with open(template_path,'r') as f2:
        template = f2.read()
    #get the whole html by converting the markdown to html
    html= markdown_to_html_node(markdown).to_html()
    #get the title of markdown file
    title = extract_title(markdown)
    # reaplce content and title by html and title variables
    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    # get the directory of dest_path
    directory = os.path.dirname(dest_path)
    # if the dest_path exists do nothing( no error because exist_ok = True) else make the dest_path directory
    os.makedirs(directory,exist_ok=True)
    # write the page content in dest_path directory
    with open(dest_path,'w') as f3:
        f3.write(page_content)
   

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    # getting the path of content
    file_path = dir_path_content
    # making a list of filenames in the content path directory like [index.html, majesty(dir)]
    file_names = os.listdir(dir_path_content)
    # iterating through every filenames 
    for filename in file_names:
        #joining the path of the filenames in the file_path
        file_path = os.path.join(file_path,filename)
        #if it's a file and ends with a 'md 'just call the generate page function and generate a static page
        if os.path.isfile(file_path) and filename.endswith('md'):
            generate_page(file_path, template_path, os.path.join(dest_dir_path,f"{filename[:-3]}.html")) # update the destination path and get all the html code in a {filename}.html file
            file_path = dir_path_content #also get back to the initial content path because there is a chance we can have some sub-dir so we want to cover those as well
        
        #if it is a dir then call the generate_page_recursive func recursively 
        elif os.path.isdir(file_path):
            generate_page_recursive(file_path, template_path, os.path.join(dest_dir_path,f"{filename}")) # get all the html in a file names {filename} in the destination path
        
        





