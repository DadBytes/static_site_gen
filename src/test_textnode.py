import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bolded node", TextType.BOLD)
        node2 = TextNode("This is a bolded node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_miss_url(self):
        node = TextNode("This is a bolded node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev/")
        self.assertNotEqual(node.url, None)

    def test_ineq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a bolded node", TextType.BOLD)
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
