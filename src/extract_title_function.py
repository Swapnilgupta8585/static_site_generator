from block_markdown import markdown_to_blocks, block_to_block_type

def extract_title(markdown):
    """
    Extracts the title from a Markdown string. 
    Assumes that the title is the first level 1 heading (i.e., starts with '# ').
    
    Parameters:
    - markdown (str): The Markdown text to extract the title from.
    
    Returns:
    - str: The extracted title.
    
    Raises:
    - ValueError: If no level 1 heading is found in the Markdown text.
    """
    # Convert the Markdown text into a list of blocks
    list_of_blocks = markdown_to_blocks(markdown)
    
    # Iterate through each block to find the heading
    for block in list_of_blocks:
        # Determine the type of the block (e.g., heading, paragraph, etc.)
        type_of_block = block_to_block_type(block)
        
        # Check if the block is a heading
        if type_of_block == "heading":
            # If it's a level 1 heading, extract and return the title
            if block.startswith('# '):
                return block[2:].strip()
    
    # Raise an error if no level 1 heading is found
    raise ValueError("All pages need a single h1 header")
