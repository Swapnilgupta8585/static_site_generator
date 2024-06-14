import unittest

from htmlnode import HtmlNode,LeafNode,ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_of_props_to_html(self):
        node = HtmlNode(
            "p",
            "sappoBhai jindabaad",
            ['footer','navigation_bar'],
            {"href": "WWE.COM", "target": "WWE", "color": "BLUE"}
        )
        test_string= ' href="WWE.COM" target="WWE" color="BLUE"'
        self.assertEqual(node.props_to_html(),test_string)

   
    def test_of_LeafNode(self):
        node = LeafNode("p",
            "sappoBhai jindabaad",
            {"href": "WWE.COM", "target": "WWE", "color": "BLUE"}
        )
        self.assertEqual(node.to_html(),'<p href="WWE.COM" target="WWE" color="BLUE">sappoBhai jindabaad</p>')
    
    def test_to_html_no_tag(self):
        node = LeafNode(None,
            "sappoBhai jindabaad",
        )
        self.assertEqual(node.to_html(),"sappoBhai jindabaad")

    def test_of_error(self):
        node = LeafNode(None,None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_of_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],      
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_of_ParentNode2(self):
        node = ParentNode(
                    "p",
                    [
                    ParentNode(
                        "p",
                        [LeafNode("b", "Bold text"),
                         LeafNode(None, "Normal text")
                         ]
                        ),
                    LeafNode("i", "italic text"),
                    ParentNode(
                        "p",
                        [
                            ParentNode(
                                "h1",
                                [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text")
                                ]
                                ),
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text")
                        ]
                        ),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                    ]     
                )
        self.assertEqual(node.to_html(),f"<p><p><b>Bold text</b>Normal text</p><i>italic text</i><p><h1><b>Bold text</b>Normal text</h1><b>Bold text</b>Normal text<i>italic text</i></p><i>italic text</i>Normal text</p>")

#boot.dev tests
    # def test_to_html_with_children(self):
    #     child_node = LeafNode("span", "child")
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # def test_to_html_with_grandchildren(self):
    #     grandchild_node = LeafNode("b", "grandchild")
    #     child_node = ParentNode("span", [grandchild_node])
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(
    #         parent_node.to_html(),
    #         "<div><span><b>grandchild</b></span></div>",
    #     )

    # def test_to_html_many_children(self):
    #     node = ParentNode(
    #         "p",
    #         [
    #             LeafNode("b", "Bold text"),
    #             LeafNode(None, "Normal text"),
    #             LeafNode("i", "italic text"),
    #             LeafNode(None, "Normal text"),
    #         ],
    #     )
    #     self.assertEqual(
    #         node.to_html(),
    #         "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
    #     )

    # def test_headings(self):
    #     node = ParentNode(
    #         "h2",
    #         [
    #             LeafNode("b", "Bold text"),
    #             LeafNode(None, "Normal text"),
    #             LeafNode("i", "italic text"),
    #             LeafNode(None, "Normal text"),
    #         ],
    #     )
    #     self.assertEqual(
    #         node.to_html(),
    #         "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
    #     )




        
if __name__ == "__main__":
    unittest.main()