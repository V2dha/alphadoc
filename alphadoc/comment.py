import tokenize
from io import StringIO


def get_comments(source):
    if not hasattr(source, 'readline'):
        source = StringIO(source)

    tokenizer = tokenize.generate_tokens(source.readline)
    for token in tokenizer:
        if token[0] == tokenize.COMMENT:
            yield token[1:4]


def get_comment_blocks(source):
    comments = []

    for comment, start, end in get_comments(source):
        if (not comments or comments[-1][1][0] == start[0] - 1
                and comments[-1][1][1] == start[1]):
            comments.append((comment, start, end))
        else:
            yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]
            comments = [(comment, start, end)]

    if comments:
        yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]

def get_doc_blocks(source):
    comments = []

    for comment, start, end in get_comments(source):
        if (not comments or comments[-1][1][0] == start[0] - 1
                and comments[-1][1][1] == start[1]):
            comments.append((comment, start, end))
        else:
            yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]
            comments = [(comment, start, end)]

    if comments:
        yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]


if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as fp:
        for comment, start, end in get_comment_blocks(fp):
            heading = "Line %s" % (start[0])
            print(heading)
            print('-' * len(heading))
            print('')
            print(comment)
            print('\n')
    


    
