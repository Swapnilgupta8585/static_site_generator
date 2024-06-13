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


