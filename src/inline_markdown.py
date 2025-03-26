from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # check if a matching closing delimiter is found
        sub_nodes = []
        split_node = old_node.text.split(delimiter)

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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        temp_node = old_node.text
        for image in images:
            image_alt, image_link = image
            split_node = temp_node.split(f"![{image_alt}]({image_link})", 1)

            if len(split_node) != 2:
                raise ValueError("invalid markdown")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            temp_node = split_node[1]

        if temp_node != "":
            new_nodes.append(TextNode(temp_node, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        temp_node = old_node.text
        for link in links:
            image_alt, image_link = link
            split_node = temp_node.split(f"[{image_alt}]({image_link})", 1)

            if len(split_node) != 2:
                raise ValueError("invalid markdown")

            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.LINK, image_link))
            temp_node = split_node[1]

        if temp_node != "":
            new_nodes.append(TextNode(temp_node, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes
