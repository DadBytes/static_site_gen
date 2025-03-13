import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "This is the link text.",
            children=None,
            props={"href": "https://www.google.com", "target": "_blank"},
        )

        attributes = node.props_to_html()
        self.assertEqual(attributes, " href='https://www.google.com' target='_blank'")


if __name__ == "__main__":
    unittest.main()
