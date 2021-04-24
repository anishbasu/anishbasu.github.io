from itertools import chain
class h:
    def __init__(self, tag, *args, **kwargs):
        self.__type = tag
        self.attributes_list = [arg for arg in args if isinstance(arg, dict)]
        if kwargs:
            self.attributes_list.append(kwargs)
        self.attributes = {}
        for attr_obj in self.attributes_list:
            self.attributes = {**self.attributes, **attr_obj}
        self.children = [arg for arg in args if isinstance(arg, (h, str))]
    def insert(self, child):
        if isinstance(child, dict):
            self.attributes = {**self.attributes, **child}
        if isinstance(child, str) or isinstance(child, h):
            self.children.append(child)
    def render(self, depth = 0):
        content = "\n".join([child.render(depth = depth + 1) if isinstance(child, h) else h.indent(depth + 1) + child for child in self.children])
        attrs = " " + " ".join([f"{k}=\"{v}\"" for k, v in self.attributes.items()]) if self.attributes else ""
        return f"{h.indent(depth)}<{self.__type}{attrs}>\n{content}\n{h.indent(depth)}</{self.__type}>"
    @staticmethod
    def indent(val):
        return " " * 4 * val
    def __str__(self):
        return self.render()