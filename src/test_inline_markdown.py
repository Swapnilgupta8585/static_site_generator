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

if __name__ == "__main__":
      unittest.main()