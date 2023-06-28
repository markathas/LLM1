import tiktoken

f = open('/mnt/data/MyDocuments/shakespeare/complete-works.original.txt', mode='r')
sp = f.read()
print('string length:',len(sp))
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

tokens = num_tokens_from_string(sp, "cl100k_base")
print('tokens found:', tokens)

