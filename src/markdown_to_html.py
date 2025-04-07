# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
# Determine the type of block (you already have a function for this)
# Based on the type of block, create a new HTMLNode with the proper data
# Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
# The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes


def block_type_tags(block_type):
    tags = {BlockType.paragraph: "p", BlockType.code: "code"}
    return tags[block_type]


def text_type_tags(text_type):
    tags = {TextType.BOLD: "b"}
    return tags[text_type]


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def markdown_to_html_node(markdown):
    parent_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_tag = block_type_tags(block_type)
        children = text_to_children(block)
        parent_nodes.append(
            ParentNode(
                block_tag,
                children,
            )
        )
    return ParentNode("div", parent_nodes)


# Create unit tests. Here are two to get you started:
# def test_paragraphs(self):
# md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """

# node = markdown_to_html_node(md)
# html = node.to_html()
# print(html)
#     self.assertEqual(
#         html,
#         "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#     )

# def test_codeblock(self):
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """

#     node = markdown_to_html_node(md)
#     html = node.to_html()
#     self.assertEqual(
#         html,
#         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#     )
