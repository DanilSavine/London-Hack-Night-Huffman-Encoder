import heapq


def generate_distribution(phrase):
    letter_freq_dist = dict().fromkeys(phrase)
    for letter in letter_freq_dist.keys():
        letter_freq_dist[letter] = phrase.count(letter)
    print(letter_freq_dist)
    return letter_freq_dist


class Node:
    def __init__(self, letter, frequency, parent=None, child_left=None, child_right=None, code=None):
        self.letter = letter
        self.frequency = frequency
        self.parent = parent
        self.child_left = child_left
        self.child_right = child_right
        self.code = code

    def __lt__(self, nxt):
        return self.frequency < nxt.frequency


def create_huffman_tree(distribution_dict):
    huffman_tree = []
    for letter in distribution_dict:
        heapq.heappush(huffman_tree, Node(letter, distribution_dict[letter]))
    while len(huffman_tree) > 1:
        left_node = heapq.heappop(huffman_tree)
        right_node = heapq.heappop(huffman_tree)
        left_node.code, right_node.code = "1", "0"
        heapq.heappush(huffman_tree, Node(letter=left_node.letter + right_node.letter,
                                          frequency=left_node.frequency + right_node.frequency,
                                          child_left=left_node,
                                          child_right=right_node,
                                          code=""))
    return huffman_tree


def print_huffman_code(huffman_node, code=""):
    code = code + str(huffman_node.code)
    if huffman_node.child_right:
        print_huffman_code(huffman_node.child_right, code)
    if huffman_node.child_left:
        print_huffman_code(huffman_node.child_left, code)
    if not huffman_node.child_left and not huffman_node.child_right:
        print(f"{huffman_node.letter} : {code}")


if __name__ == '__main__':
    message = "aaaaaaaaaaaabbbcccccddeeeeeeeeee"
    distribution = generate_distribution(message)
    tree = create_huffman_tree(distribution)
    print_huffman_code(tree[0])