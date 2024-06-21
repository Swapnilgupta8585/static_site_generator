from block_markdown import markdown_to_blocks,block_to_block_type

def extract_title(markdown):
    list_of_blocks = markdown_to_blocks(markdown)
    for block in list_of_blocks:
        type_of_block = block_to_block_type(block)
        if type_of_block == "heading":
            if block.startswith('# '):
                return block[2:].strip()
    raise ValueError("All pages Need a single h1 header")
