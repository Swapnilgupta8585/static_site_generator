from textnode import TextNode
from htmlnode import HtmlNode

def main():
    my_text_node = TextNode("sappo bhai","bold")
    print(my_text_node)
    my_html_node = HtmlNode("p","sappoBhai jindabaad",['footer','navigation_bar'],{"href": "WWE.COM", "target": "WWE", "color": "BLUE"})
    print(my_html_node)
main()
