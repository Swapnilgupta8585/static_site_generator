from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

# Constants representing different block types in markdown
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_html_node(markdown):
    """
    Converts markdown text into an HTML node tree.

    Parameters:
    - markdown (str): The markdown text to convert.

    Returns:
    - ParentNode: The root HTML node (a div element) containing all converted child nodes.
    """
    children = []
    blocks = markdown_to_blocks(markdown)  # Split markdown into blocks
    for block in blocks:
        html_node = get_html_node(block)  # Convert each block to an HTML node
        children.append(html_node)
    return ParentNode("div", children)  # Return a ParentNode with all HTML nodes as children

def markdown_to_blocks(raw_markdown):
    """
    Splits raw markdown text into individual blocks.

    Parameters:
    - raw_markdown (str): The raw markdown text.

    Returns:
    - list: A list of strings, each representing a block of markdown.
    """
    if raw_markdown == "":
        return []  # Return an empty list if markdown is empty

    list_blocks = []
    split_blocks = raw_markdown.split("\n\n")  # Split blocks by double newlines
    for block in split_blocks:
        if block == "":
            continue
        block = block.strip()  # Remove leading and trailing whitespace
        list_blocks.append(block)

    return list_blocks

def get_html_node(block):
    """
    Converts a markdown block into an HTML node based on its type.

    Parameters:
    - block (str): A single markdown block.

    Returns:
    - HTML node: The corresponding HTML representation of the markdown block.

    Raises:
    - ValueError: If the block type is invalid.
    """
    block_type = block_to_block_type(block)  # Determine the type of the block
    
    # Convert the block to an HTML node based on its type
    if block_type == block_type_heading:
        return heading_block_to_htmlnode(block)
    if block_type == block_type_quote:
        return quote_block_to_htmlnode(block)
    if block_type == block_type_code:
        return code_block_to_htmlnode(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_htmlnode(block)
    if block_type == block_type_ordered_list:
        return ordered_block_to_htmlnode(block)
    if block_type == block_type_unordered_list:
        return unordered_block_to_htmlnode(block)
    
    raise ValueError("Invalid block type")  # Raise an error if the block type is not recognized

        
def block_to_block_type(block):
    """
    Determines the type of a markdown block based on its content.

    Parameters:
    - block (str): A single markdown block of text.

    Returns:
    - str: The type of the markdown block, such as 'heading', 'code', 'quote', 'unordered_list', 'ordered_list', or 'paragraph'.
    """
    lines = block.split("\n")  # Split the block into individual lines

    # Check for heading blocks (starting with '#')
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading

    # Check for code blocks (surrounded by triple backticks)
    if len(lines) > 0 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code

    # Check for quote blocks (starting with '>')
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    # Check for unordered list blocks (starting with '* ')
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    
    # Check for unordered list blocks (starting with '- ')
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    
    # Check for ordered list blocks (starting with '1. ')
    if block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return block_type_paragraph
            count += 1
        return block_type_ordered_list
    
    # Default to paragraph if no other type matches
    return block_type_paragraph


from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

def heading_block_to_htmlnode(block):
    """
    Converts a heading markdown block to an HTML node.

    Parameters:
    - block (str): The markdown heading block.

    Returns:
    - ParentNode: The corresponding HTML node (h1-h6).
    
    Raises:
    - ValueError: If the block does not match any valid heading format.
    """
    if block.startswith("# "):
        text = block[2:]
        children = inline_children_nodes(text)
        return ParentNode("h1", children)
    if block.startswith("## "):
        text = block[3:]
        children = inline_children_nodes(text)
        return ParentNode("h2", children)
    if block.startswith("### "):
        text = block[4:]
        children = inline_children_nodes(text)
        return ParentNode("h3", children)
    if block.startswith("#### "):
        text = block[5:]
        children = inline_children_nodes(text)
        return ParentNode("h4", children)
    if block.startswith("##### "):
        text = block[6:]
        children = inline_children_nodes(text)
        return ParentNode("h5", children)
    if block.startswith("###### "):
        text = block[7:]
        children = inline_children_nodes(text)
        return ParentNode("h6", children)
    else:
        raise ValueError("Invalid heading")

def code_block_to_htmlnode(block):
    """
    Converts a code markdown block to an HTML node.

    Parameters:
    - block (str): The markdown code block.

    Returns:
    - ParentNode: The corresponding HTML node (pre/code).
    
    Raises:
    - ValueError: If the block does not start and end with triple backticks.
    """
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = inline_children_nodes(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_block_to_htmlnode(block):
    """
    Converts a quote markdown block to an HTML node.

    Parameters:
    - block (str): The markdown quote block.

    Returns:
    - ParentNode: The corresponding HTML node (blockquote).
    
    Raises:
    - ValueError: If the block does not start with '>'.
    """
    lines = block.split("\n")
    updated_line = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        updated_line.append(line.lstrip(">").strip())
    text = (" ").join(updated_line)
    children = inline_children_nodes(text)
    return ParentNode("blockquote", children)

def paragraph_block_to_htmlnode(block):
    """
    Converts a paragraph markdown block to an HTML node.

    Parameters:
    - block (str): The markdown paragraph block.

    Returns:
    - ParentNode: The corresponding HTML node (p).
    """
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = inline_children_nodes(paragraph)
    return ParentNode("p", children)
    
def unordered_block_to_htmlnode(block):
    """
    Converts an unordered list markdown block to an HTML node.

    Parameters:
    - block (str): The markdown unordered list block.

    Returns:
    - ParentNode: The corresponding HTML node (ul/li).
    """
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        text = line[2:]
        children = inline_children_nodes(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)

def ordered_block_to_htmlnode(block):
    """
    Converts an ordered list markdown block to an HTML node.

    Parameters:
    - block (str): The markdown ordered list block.

    Returns:
    - ParentNode: The corresponding HTML node (ol/li).
    """
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        text = line[3:]
        children = inline_children_nodes(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ol", li_nodes)

def inline_children_nodes(text):
    """
    Converts a markdown text to a list of HTML nodes representing inline elements.

    Parameters:
    - text (str): The markdown text.

    Returns:
    - list: A list of ParentNode instances representing inline HTML elements.
    """
    text_nodes = text_to_textnodes(text)  # Convert text to text nodes
    inline_children_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)  # Convert text node to HTML node
        inline_children_nodes.append(html_node)
    return inline_children_nodes
