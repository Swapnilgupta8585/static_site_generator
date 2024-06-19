from block_markdown import(markdown_to_blocks,
                        heading_block_to_htmlnode,
                        block_to_block_type,
                        code_block_to_htmlnode,
                        quote_block_to_htmlnode,
                        paragraph_block_to_htmlnode,
                        unordered_block_to_htmlnode,
                        ordered_block_to_htmlnode,
                        block_type_paragraph,
                        block_type_heading,
                        block_type_code, 
                        block_type_quote,
                        block_type_unordered_list,
                        block_type_ordered_list)

from inline_markdown import text_to_textnodes

from textnode import text_node_to_html_node


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError("hehe")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        formatted_string = ""
        for key,value in self.props.items():
            formatted_string += f' {key}="{value}"'
        return formatted_string
    
    def __repr__(self):
        return f"HtmlNode({self.tag},{self.value},{self.children},{self.props})"
    
class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"

class ParentNode(HtmlNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tags")
        if self.children == None:
            raise ValueError("Invalid HTML: no children")
        final_html = ''
        for children in self.children:
            if isinstance(children,LeafNode):
                final_html += children.to_html()
            elif isinstance(children,ParentNode):
                final_html += children.to_html()

        return  f"<{self.tag}{self.props_to_html()}>{final_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    







    def markdown_to_html_node(markdown):
        children_node = []
        # it is the children node which will consist the order and all the children node of the the ultimate parentNode => ParentNode("div",childrenNode)

        list_of_blocks = markdown_to_blocks(markdown) # breaking the whole markdown text into blocks of different kind

        for block in list_of_blocks: # iterating over every block in list_of_blocks

            block_type = block_to_block_type(block) # getting the type of the block

            if block_type == block_type_heading: 
                # getting htmlnode for this particular block
                heading_html_node = heading_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_heading_html_node = text_to_textnodes(heading_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_heading_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                heading_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(heading_html_node)

            if block_type == block_type_quote:
                # getting htmlnode for this particular block
                quote_html_node = quote_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_quote_html_node = text_to_textnodes(quote_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_quote_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                quote_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(quote_html_node)
                

            if block_type == block_type_code:
                # getting htmlnode for this particular block
                code_html_node = code_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_code_html_node = text_to_textnodes(code_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_code_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                code_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(code_html_node)



            if block_type == block_type_paragraph:
                # getting htmlnode for this particular block
                paragraph_html_node = paragraph_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_paragraph_html_node = text_to_textnodes(paragraph_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_paragraph_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                paragraph_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(paragraph_html_node)





            if block_type == block_type_unordered_list:
                # getting htmlnode for this particular block
                unordered_list_html_node = unordered_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_unordered_list_html_node = text_to_textnodes(unordered_list_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_unordered_list_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                unordered_list_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(unordered_list_html_node)





            if block_type == block_type_ordered_list:
                # getting htmlnode for this particular block
                ordered_list_html_node = ordered_block_to_htmlnode(block,block_type) 

                #getting all the textNodes that this block's htmlnode.value contains
                all_textnodes_in_ordered_list_html_node = text_to_textnodes(ordered_list_html_node.value) 

                # children inline nodes of block's html_node
                all_inline_markdown_nodes = [] 

                for text_node in all_textnodes_in_ordered_list_html_node:

                    #appending the result of getting the html_node from the text_node in children inline nodes list
                    all_inline_markdown_nodes.append(text_node_to_html_node(text_node))

                #setting the children instance variable for the block's html_node
                ordered_list_html_node.children = all_inline_markdown_nodes

                #appending the block's html_node with it's inline children_nodes
                children_node.append(ordered_list_html_node)

            
        Final_html_node = HtmlNode("div",None,children_node)
        all_html = Final_html_node.to_html()
        return all_html
            
            


