import unittest

from htmlnode import HtmlNode,LeafNode


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

        
if __name__ == "__main__":
    unittest.main()