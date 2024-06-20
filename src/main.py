from textnode import TextNode
from copy_static import remove_public_dir_content,copy_static


def main():
    file_path = "/home/swapnilgupta1981/workspace/github.com/Swapnilgupta8585/static_site_generator/static"
    public_dir = "/home/swapnilgupta1981/workspace/github.com/Swapnilgupta8585/static_site_generator/public"
    remove_public_dir_content(public_dir)
    copy_static(file_path, public_dir)


main()
