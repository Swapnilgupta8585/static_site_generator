import unittest
from textnode import TextNode
from inline_markdown import split_nodes_delimiter

class Test_inline_markdown(unittest.TestCase):
    def test_delim_bold(self):
            node = TextNode("This is text with a **bolded** word", "text")
            new_nodes = split_nodes_delimiter([node], "**", "bold")
            self.assertListEqual(
                [
                    TextNode("This is text with a ","text"),
                    TextNode("bolded", "bold"),
                    TextNode(" word", "text"),
                ],
                new_nodes,
            )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_no_texx_type_textnode(self):
        node = TextNode("`This is text with a code block word`", "code")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                node
                
            ],
            new_nodes,
        )
    
    
    def test_split_nodes_delimiter_adjacent_delim_text(self):
        """
        Test splitting a TextNode into multiple TextNodes by a delimiter,
        where there are two adjacent delimited text segements.
        """
        # Arrange
        node = TextNode("**bold1****bold2**`code`", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("bold1", "bold"),
            TextNode("bold2", "bold"),
            TextNode("`code`", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_non_text_type(self):
       
        # Arrange
        nodes: list[TextNode] = [
            TextNode("italic text", "italic"),
            TextNode("bold text", "bold"),
            TextNode("Text with a `code block`", "text"),
        ]
        # Act
        actual_nodes = split_nodes_delimiter(nodes, "`", "code")
        expected_nodes = [
            TextNode("italic text", "italic"),
            TextNode("bold text", "bold"),
            TextNode("Text with a ", "text"),
            TextNode("code block", "code"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

   
    


if __name__ == "__main__":
      unittest.main()