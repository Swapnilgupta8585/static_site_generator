class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes an HTML node.
        
        Parameters:
        - tag (str): The HTML tag (e.g., 'div', 'span'). Default is None.
        - value (str): The text content of the node. Default is None.
        - children (list): A list of child HtmlNode instances. Default is None.
        - props (dict): A dictionary of HTML attributes (e.g., {'class': 'my-class'}). Default is None.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Converts the HTML node to an HTML string. This method should be overridden in subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def props_to_html(self):
        """
        Converts the properties dictionary to an HTML attribute string.
        
        Returns:
        - str: A string of HTML attributes (e.g., 'class="my-class" id="my-id"').
        """
        if self.props is None:
            return ""
        formatted_string = ""
        for key, value in self.props.items():
            formatted_string += f' {key}="{value}"'
        return formatted_string

    def __repr__(self):
        """
        Provides a string representation of the HTML node.
        
        Returns:
        - str: A string representation of the HtmlNode instance.
        """
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes a leaf HTML node (a node without children).
        
        Parameters:
        - tag (str): The HTML tag (e.g., 'p', 'span').
        - value (str): The text content of the node.
        - props (dict): A dictionary of HTML attributes. Default is None.
        """
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Converts the leaf HTML node to an HTML string.
        
        Returns:
        - str: The HTML string representation of the leaf node.
        
        Raises:
        - ValueError: If the value is None (i.e., no content) or the tag is None.
        """
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        """
        Provides a string representation of the leaf HTML node.
        
        Returns:
        - str: A string representation of the LeafNode instance.
        """
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        """
        Initializes a parent HTML node (a node with children).
        
        Parameters:
        - tag (str): The HTML tag (e.g., 'div', 'section').
        - children (list): A list of child HtmlNode instances.
        - props (dict): A dictionary of HTML attributes. Default is None.
        """
        super().__init__(tag, None, children, props)

    def to_html(self):
        """
        Converts the parent HTML node to an HTML string.
        
        Returns:
        - str: The HTML string representation of the parent node.
        
        Raises:
        - ValueError: If the tag is None or there are no children.
        """
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        final_html = ''
        for child in self.children:
            if isinstance(child, LeafNode):
                final_html += child.to_html()
            elif isinstance(child, ParentNode):
                final_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{final_html}</{self.tag}>"

    def __repr__(self):
        """
        Provides a string representation of the parent HTML node.
        
        Returns:
        - str: A string representation of the ParentNode instance.
        """
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"






    
            


