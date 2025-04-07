from enum import Enum

BlockType = Enum(
    "BlockType",
    ["paragraph", "heading", "code", "quote", "unordered_list", "ordered_list"],
)


def markdown_to_blocks(md):
    split_md = md.split("\n\n")

    stripped_list = []
    for block in split_md:
        if block == "":
            continue
        stripped_block = block.strip()
        stripped_list.append(stripped_block)
    return stripped_list


def check_list_startswith(block_list, char):
    for element in block_list:
        if not element.startswith(char):
            return False
    return True


def check_list_numbered(block_list):
    start = 1

    for element in block_list:
        if not element.startswith(f"{start}. "):
            return False
        start += 1
    return True


def block_to_block_type(block):
    if (block.rfind("# ") > -1) and (block.rfind("# ") < 6):
        return BlockType.heading
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.code

    split_block = block.splitlines()

    if check_list_startswith(split_block, "> "):
        return BlockType.quote
    if check_list_startswith(split_block, "- "):
        return BlockType.unordered_list
    if check_list_numbered(split_block):
        return BlockType.ordered_list
    else:
        return BlockType.paragraph


# blocks = [
#     "###### This is a heading",
#     "```This is a code block```",
#     "> this is a quote\n> with two lines",
#     "> this is an invalid\n >quote",
#     "1. first\n2. second\n3. third",
#     "1. first\n1. second\n3. third",
# ]
