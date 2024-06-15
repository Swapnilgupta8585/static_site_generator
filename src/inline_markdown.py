from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                new_nodes.append(node)
                continue      
        
            split_wrt_delimiter = node.text.split(delimiter)
            split_node = []
            if len(split_wrt_delimiter) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            
            for i in range(0,len(split_wrt_delimiter)):
                if split_wrt_delimiter[i] == "":
                    continue
                if i % 2 == 0:
                    split_node.append(TextNode(split_wrt_delimiter[i],"text"))
                    continue
                split_node.append(TextNode(split_wrt_delimiter[i],text_type))
            new_nodes.extend(split_node)
        return new_nodes

        




