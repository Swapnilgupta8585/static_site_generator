from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = get_html_node(block)
        children.append(html_node)
    return ParentNode("div",children)

def markdown_to_blocks(raw_markdown):
    if raw_markdown == "":
        return []
    list_blocks = []
    split_blocks = raw_markdown.split("\n\n")
    for block in split_blocks:
        if block == "":
            continue
        block = block.strip()
        list_blocks.append(block)

    return list_blocks

def get_html_node(block):
    block_type = block_to_block_type(block) 
    if block_type == block_type_heading:
        heading_html_node = heading_block_to_htmlnode(block)
        return heading_html_node
    if block_type == block_type_quote:
        quote_html_node = quote_block_to_htmlnode(block)
        return quote_html_node
    if block_type == block_type_code:
        code_html_node = code_block_to_htmlnode(block)
        return code_html_node
    if block_type == block_type_paragraph:
        paragraph_html_node = paragraph_block_to_htmlnode(block)
        return paragraph_html_node
    if block_type == block_type_ordered_list:
        ordered_list_html_node = ordered_block_to_htmlnode(block)
        return ordered_list_html_node
    if block_type == block_type_unordered_list:
        unordered_list_html_node = unordered_block_to_htmlnode(block)
        return unordered_list_html_node
    raise ValueError("Invalid block type")
        
def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading

    if len(lines) > 0 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    
    
    if block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return block_type_paragraph
            count += 1
        return block_type_ordered_list
    
    return block_type_paragraph

def heading_block_to_htmlnode(block):
    if block.startswith("# "):
        text = block[2:]
        children = inline_children_nodes(text)
        return ParentNode("h1",children)
    if block.startswith("## "):
        text = block[3:]
        children = inline_children_nodes(text)
        return ParentNode("h2",children)
    if block.startswith("### "):
        text = block[4:]
        children = inline_children_nodes(text)
        return ParentNode("h3",children)
    if block.startswith("#### "):
        text = block[5:]
        children = inline_children_nodes(text)
        return ParentNode("h4",children)
    if block.startswith("##### "):
        text = block[6:]
        children = inline_children_nodes(text)
        return ParentNode("h5",children)
    if block.startswith("###### "):
        text = block[7:]
        children = inline_children_nodes(text)
        return ParentNode("h6",children)
    else:
        raise ValueError("Invalid heading")

def code_block_to_htmlnode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = inline_children_nodes(text)
    code = ParentNode("code",children)
    return ParentNode("pre",[code])

def quote_block_to_htmlnode(block):
    lines = block.split("\n")
    updated_line = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        updated_line.append(line.lstrip(">").strip())
    text = (" ").join(updated_line)
    children = inline_children_nodes(text)
    return ParentNode("blockquote",children)

def paragraph_block_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = inline_children_nodes(paragraph)
    return ParentNode("p", children)
    
def unordered_block_to_htmlnode(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        text = line[2:]
        children = inline_children_nodes(text)
        li_nodes.append(ParentNode("li",children))
    return ParentNode("ul",li_nodes)

def ordered_block_to_htmlnode(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        text = line[3:]
        children = inline_children_nodes(text)
        li_nodes.append(ParentNode("li",children))
    return ParentNode("ol",li_nodes)

def inline_children_nodes(text):
    text_nodes = text_to_textnodes(text)
    inline_children_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        inline_children_nodes.append(html_node)
    return inline_children_nodes
    