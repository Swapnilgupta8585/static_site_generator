from textnode import TextNode
import re

def text_to_textnodes(text):
    original_node = TextNode(text,'text')
    
    split_for_bold = split_nodes_delimiter([original_node],"**","bold")
    
    split_for_italic = split_nodes_delimiter(split_for_bold,"*","italic")
    
    split_for_code = split_nodes_delimiter(split_for_italic,"`","code")
    
    split_for_images = split_nodes_images(split_for_code)
    
    split_for_links = split_nodes_links(split_for_images)
    
    return split_for_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                new_nodes.append(node)
                continue      
        
            split_wrt_delimiter = node.text.split(delimiter)
            split_node = []
            if len(split_wrt_delimiter) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            
            for i in range(0,len(split_wrt_delimiter)):
                if split_wrt_delimiter[i] == "":
                    continue
                if i % 2 == 0:
                    split_node.append(TextNode(split_wrt_delimiter[i],"text"))
                    continue
                split_node.append(TextNode(split_wrt_delimiter[i],text_type))
            new_nodes.extend(split_node)
        return new_nodes

def split_nodes_images(old_nodes):
    new_node  = []
    for node in old_nodes:
        split_node = []
        image_tuples = extract_markdown_images(node.text)

        if len(image_tuples) == 0:
            split_node.append(node)
            new_node.extend(split_node)
            continue
        node_text = node.text
        for image_tup in image_tuples:
            split_wrt_images = node_text.split(f"![{image_tup[0]}]({image_tup[1]})",1)
           
            if split_wrt_images[0] != "":
                split_node.append(TextNode(split_wrt_images[0],"text"))
            split_node.append(TextNode(image_tup[0],"image",image_tup[1]))
            node_text = split_wrt_images[1]
        new_node.extend(split_node)
        if node_text != "":
            new_node.append(TextNode(node_text,"text"))
        
    
    return new_node

def split_nodes_links(old_nodes):
    new_node  = []
    
    for node in old_nodes:
        
        split_node = []
        link_tuples = extract_markdown_links(node.text)
       
        
        if len(link_tuples) == 0:
            split_node.append(node)
            new_node.extend(split_node)
            continue
        node_text = node.text
        
        for link_tup in link_tuples:
            split_wrt_links = node_text.split(f"[{link_tup[0]}]({link_tup[1]})",1)
            
            if split_wrt_links[0] != "":
                split_node.append(TextNode(split_wrt_links[0],"text"))
                
            split_node.append(TextNode(link_tup[0],"link",link_tup[1]))
            node_text = split_wrt_links[1]
        new_node.extend(split_node)
        if node_text != "":
            new_node.append(TextNode(node_text,"text"))
        
   
    return new_node

def extract_markdown_images(text):
    alt_txt_and_url = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return alt_txt_and_url

def extract_markdown_links(text):
    anchor_txt_and_url = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return anchor_txt_and_url








