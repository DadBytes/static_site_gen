from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # check if a matching closing delimiter is found
        sub_nodes = []
        split_node = node.text.split(delimiter)

        if len(split_node) % 2 == 0:
            raise ValueError("this is not valid markdown systax")

        for i in range(len(split_node)):
            if split_node[i] == "":
                continue

            if i % 2 == 0:
                sub_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                sub_nodes.append(TextNode(split_node[i], text_type))

        new_nodes.extend(sub_nodes)

    return new_nodes


def extract_markdown_images(text):
    image_list = []
    images = re.findall(r"(?<=!)(\[.*?\))", text)

    for image in images:
        alt_text = re.findall(r"(?<=\[).+?(?=\])", image)[0]
        url = re.findall(r"(?<=\().+?(?=\))", image)[0]

        image_list.append((alt_text, url))

    return image_list


def extract_markdown_links(text):
    link_list = []
    links = re.findall(r"(?<!!)(\[.*?\))", text)

    for link in links:
        anchor_text = re.findall(r"(?<=\[).+?(?=\])", link)[0]
        url = re.findall(r"(?<=\().+?(?=\))", link)[0]

        link_list.append((anchor_text, url))

    return link_list
