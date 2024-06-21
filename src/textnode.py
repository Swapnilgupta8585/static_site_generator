from htmlnode import LeafNode

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):

        if self.text == other.text and self.text_type == other.text_type and  self.url == other.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None,text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b",text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i",text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code",text_node.text)
    
    elif text_node.text_type == "link":
        return LeafNode("a",text_node.text,{"href": text_node.url })
    elif text_node.text_type == "image":
        return LeafNode("img",text_node.text,{"src": text_node.url},)
    else:
        raise ValueError(f"Invalid Text Type: {text_node.text_type}")    


