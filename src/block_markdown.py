from htmlnode import HtmlNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


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
            
        
            
def heading_block_to_htmlnode(block,block_type):
    if block_type == block_type_heading:
        
        if block.startswith("# "):
            return HtmlNode("h1", block[2:])

        if block.startswith("## "):
            return HtmlNode("h2", block[3:])
        
        if block.startswith("### "):
            return HtmlNode("h3", block[4:])
        
        if block.startswith("#### "):
            return HtmlNode("h4", block[5:])
        
        if block.startswith("##### "):
            return HtmlNode("h5", block[6:])
        
        if block.startswith("###### "):
            return HtmlNode("h6", block[7:])
        
def code_block_to_htmlnode(block,block_type):
    if block_type == block_type_code:
        lines = block.split("\n")
        join_list_lines = ("\n").join(lines[1:-1])
        return HtmlNode("pre",None,[HtmlNode("code",join_list_lines)])
    
def quote_block_to_htmlnode(block,block_type):
    if block_type == block_type_quote:
        lines = block.split("\n")
        updated_line = []
        for line in lines:
            updated_line.append((line[1:]))
        join_list_lines = ("\n").join(updated_line)
        return HtmlNode("blockquote", join_list_lines)
    
def paragraph_block_to_htmlnode(block,block_type):
    if block_type == block_type_paragraph:
        return HtmlNode("p", block)
    
def unordered_block_to_htmlnode(block,block_type):
    if block_type == block_type_unordered_list:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            li_nodes.append(HtmlNode("li",(line[2:])))
    return HtmlNode("ul",None,li_nodes)

def ordered_block_to_htmlnode(block,block_type):
    if block_type == block_type_ordered_list:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            li_nodes.append(HtmlNode("li",(line[3:])))
    return HtmlNode("ol",li_nodes)


    