import unittest
from textnode import TextNode
from inline_markdown import (split_nodes_delimiter,
                             extract_markdown_links,
                             extract_markdown_images,
                             split_nodes_images,
                             split_nodes_links,
                             text_to_textnodes
                            )

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

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        list_tuples = extract_markdown_images(text)
        self.assertListEqual([("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")],list_tuples)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        list_tuples = extract_markdown_links(text)
        self.assertListEqual([("link", "https://www.example.com"), ("another", "https://www.example.com/another")],list_tuples)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links2(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_nodes_images(self):
        node = TextNode(
                    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    "text",
                )
        split_nodes = split_nodes_images([node])
        self.assertListEqual([
                                TextNode("This is text with an ", "text"),
                                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                                TextNode(" and another ", "text"),
                                TextNode(
                                    "second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                                ),
                            ],split_nodes)  

    def test_split_nodes_links(self):
        node = TextNode(
                    "This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/another)",
                    "text",
                )
        split_nodes = split_nodes_links([node])
        self.assertListEqual([
                                TextNode("This is text with a ", "text"),
                                TextNode("link", "link", "https://www.example.com"),
                                TextNode(" and another ", "text"),
                                TextNode(
                                    "second link", "link", "https://www.example.com/another"
                                ),
                            ],split_nodes) 

    def test_split_nodes_images_empty_content(self):
            node = TextNode(
                        "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                        "text",
                    )
            split_nodes = split_nodes_images([node])
            self.assertListEqual([
                                    
                                    TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                                    TextNode(" and another ", "text"),
                                    TextNode(
                                        "second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                                    ),
                                ],split_nodes)  

    def test_split_nodes_links_empty_content(self):
        node = TextNode(
                    "[link](https://www.example.com) and another [second link](https://www.example.com/another)",
                    "text",
                )
        split_nodes = split_nodes_links([node])
        self.assertListEqual([
                                
                                TextNode("link", "link", "https://www.example.com"),
                                TextNode(" and another ", "text"),
                                TextNode(
                                    "second link", "link", "https://www.example.com/another"
                                ),
                            ],split_nodes) 
        
    def test_split_nodes_images_no_image(self):
            node = TextNode(
                        " no images this time sorry! ",
                        "text",
                    )
            split_nodes = split_nodes_images([node])
            self.assertListEqual([
                                    
                                    
                                    TextNode(" no images this time sorry! ", "text"),
                                    
                                ],split_nodes)  

    def test_split_nodes_links_no_link(self):
        node = TextNode(
                    " no links this time sorry! ",
                    "text",
                )
        split_nodes = split_nodes_links([node])
        self.assertListEqual([
                                
                                
                                TextNode(" no links this time sorry! ", "text"),
                                
                            ],split_nodes) 

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertListEqual(
             [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ],text_to_textnodes(text)
        )

    def test_text_to_textnode(self):
        text = "This `code code` is [link](https://boot.dev) **text****another_text** with an *italic* word *italy* and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        self.assertListEqual(
             [
                TextNode("This ", "text"),
                TextNode("code code", "code"),
                TextNode(" is ", "text"),
                TextNode("link", "link", "https://boot.dev"),
                TextNode(" ", "text"),
                TextNode("text", "bold"),
                TextNode("another_text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word ", "text"),
                TextNode("italy", "italic"),
                TextNode(" and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
                TextNode(" ", "text"),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ],text_to_textnodes(text)
        )

if __name__ == "__main__":
      unittest.main()