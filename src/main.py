from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if TextType(text_node.text_type) == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if TextType(text_node.text_type) == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if TextType(text_node.text_type) == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if TextType(text_node.text_type) == TextType.CODE:
        return LeafNode("code", text_node.text)
    if TextType(text_node.text_type) == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if TextType(text_node.text_type) == TextType.IMAGE:
        return LeafNode("code", text_node.text)

    # text_node.TEXT: This should return a LeafNode with no tag, just a raw text value.
    # text_node.BOLD: This should return a LeafNode with a "b" tag and the text
    # text_node.ITALIC: "i" tag, text
    # text_node.CODE: "code" tag, text
    # text_node.LINK: "a" tag, anchor text, and "href" prop
    # text_node.IMAGE


def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
