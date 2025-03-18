class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        attributes = ""
        for value in self.props.items():
            attribute = value[0]
            data = value[1]
            attributes = attributes + f' {attribute}="{data}"'
        return attributes

    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError("All parent nodes must have children.")

        child_output = ""
        for child in self.children:
            child_output += child.to_html()

        return f"<{self.tag}>{child_output}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
