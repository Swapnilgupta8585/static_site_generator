from textnode import TextNode
import re

def text_to_textnodes(text):
    """
    Converts a text string into a list of TextNode instances, identifying bold, italic, code, images, and links.
    
    Parameters:
    - text (str): The input text to be converted into TextNode instances.
    
    Returns:
    - list: A list of TextNode instances representing the parsed content.
    """
    # Create an initial TextNode instance with the input text
    original_node = TextNode(text, 'text')
    
    # Process for bold text
    split_for_bold = split_nodes_delimiter([original_node], "**", "bold")
    
    # Process for italic text
    split_for_italic = split_nodes_delimiter(split_for_bold, "*", "italic")
    
    # Process for code text
    split_for_code = split_nodes_delimiter(split_for_italic, "`", "code")
    
    # Process for images
    split_for_images = split_nodes_images(split_for_code)
    
    # Process for links
    split_for_links = split_nodes_links(split_for_images)
    
    return split_for_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits nodes based on a delimiter and assigns a text type to the split parts.
    
    Parameters:
    - old_nodes (list): List of TextNode instances to process.
    - delimiter (str): The delimiter used for splitting (e.g., '**' for bold).
    - text_type (str): The type of text for the split parts (e.g., 'bold').
    
    Returns:
    - list: A list of TextNode instances with the appropriate text types.
    
    Raises:
    - ValueError: If the number of splits is even, indicating an unclosed section.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue      
        
        # Split the node's text based on the delimiter
        split_wrt_delimiter = node.text.split(delimiter)
        split_node = []
        
        # Ensure the number of splits is odd (delimiter must be paired)
        if len(split_wrt_delimiter) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(split_wrt_delimiter)):
            if split_wrt_delimiter[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(split_wrt_delimiter[i], "text"))
            else:
                split_node.append(TextNode(split_wrt_delimiter[i], text_type))
        
        new_nodes.extend(split_node)
    return new_nodes

def split_nodes_images(old_nodes):
    """
    Splits nodes to handle Markdown images and converts them into TextNode instances.
    
    Parameters:
    - old_nodes (list): List of TextNode instances to process.
    
    Returns:
    - list: A list of TextNode instances, including those for images.
    """
    new_nodes = []
    for node in old_nodes:
        split_node = []
        image_tuples = extract_markdown_images(node.text)

        if len(image_tuples) == 0:
            split_node.append(node)
            new_nodes.extend(split_node)
            continue
        
        node_text = node.text
        for image_tup in image_tuples:
            split_wrt_images = node_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
           
            if split_wrt_images[0] != "":
                split_node.append(TextNode(split_wrt_images[0], "text"))
            split_node.append(TextNode(image_tup[0], "image", image_tup[1]))
            node_text = split_wrt_images[1]
        
        new_nodes.extend(split_node)
        if node_text != "":
            new_nodes.append(TextNode(node_text, "text"))
    
    return new_nodes

def split_nodes_links(old_nodes):
    """
    Splits nodes to handle Markdown links and converts them into TextNode instances.
    
    Parameters:
    - old_nodes (list): List of TextNode instances to process.
    
    Returns:
    - list: A list of TextNode instances, including those for links.
    """
    new_nodes = []
    for node in old_nodes:
        split_node = []
        link_tuples = extract_markdown_links(node.text)

        if len(link_tuples) == 0:
            split_node.append(node)
            new_nodes.extend(split_node)
            continue
        
        node_text = node.text
        
        for link_tup in link_tuples:
            split_wrt_links = node_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            
            if split_wrt_links[0] != "":
                split_node.append(TextNode(split_wrt_links[0], "text"))
                
            split_node.append(TextNode(link_tup[0], "link", link_tup[1]))
            node_text = split_wrt_links[1]
        
        new_nodes.extend(split_node)
        if node_text != "":
            new_nodes.append(TextNode(node_text, "text"))
    
    return new_nodes

def extract_markdown_images(text):
    """
    Extracts image Markdown syntax from the text and returns a list of tuples (alt_text, url).
    
    Parameters:
    - text (str): The text containing Markdown image syntax.
    
    Returns:
    - list: A list of tuples where each tuple contains (alt_text, url) for an image.
    """
    alt_txt_and_url = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alt_txt_and_url

def extract_markdown_links(text):
    """
    Extracts link Markdown syntax from the text and returns a list of tuples (anchor_text, url).
    
    Parameters:
    - text (str): The text containing Markdown link syntax.
    
    Returns:
    - list: A list of tuples where each tuple contains (anchor_text, url) for a link.
    """
    anchor_txt_and_url = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return anchor_txt_and_url









