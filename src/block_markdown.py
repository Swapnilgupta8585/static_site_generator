def markdown_to_blocks(raw_markdown):
    if raw_markdown == "":
        return []
    list_blocks = []
    split_blocks = raw_markdown.split('\n\n')
    for block in split_blocks:
        if block == "":
            continue
        block = block.strip()
        list_blocks.append(block)
    
    return list_blocks
        
