from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        Initializes a TextNode instance.

        Parameters:
        - text (str): The text content of the node.
        - text_type (str): The type of text (e.g., 'text', 'bold', 'italic', 'code', 'link', 'image').
        - url (str, optional): The URL for links and images. Default is None.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compares two TextNode instances for equality.

        Parameters:
        - other (TextNode): The TextNode instance to compare against.

        Returns:
        - bool: True if all attributes are equal, otherwise False.
        """
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        """
        Provides a string representation of the TextNode instance.

        Returns:
        - str: A string representation of the TextNode instance.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    """
    Converts a TextNode instance to an HTML node (LeafNode).

    Parameters:
    - text_node (TextNode): The TextNode instance to convert.

    Returns:
    - LeafNode: The corresponding HTML node.

    Raises:
    - ValueError: If the text_type of the TextNode is invalid.
    """
    # Convert text_node to corresponding HTML node
    if text_node.text_type == "text":
        return LeafNode(None, text_node.t


