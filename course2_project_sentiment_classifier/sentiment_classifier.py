punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word: str):
    strip_word = ""

    for i in word:
        if i not in punctuation_chars:
            strip_word += i

    return strip_word


def get_pos(sentences):
    """takes one parameter, a string which represents one or more sentences and calculates how many words in the
    string are considered positive words."""
    li = []
    for word in sentences.split():
        wordstrip = strip_punctuation(word).lower().strip()
        if wordstrip in positive_words:
            li.append(wordstrip)
    return len(li)


def get_neg(sentences):
    """takes one parameter, a string which represents one or more sentences and calculates how many words in the
    string are considered positive words."""
    li = []
    for word in sentences.split():
        wordstrip = strip_punctuation(word).lower().strip()
        if wordstrip in negative_words:
            li.append(wordstrip)
    return len(li)


with open("project_twitter_data.csv", 'r') as twitter_data:
    lines = twitter_data.readlines()
    header = str(lines[0])
    field_names = header.strip().split(',')

    resulting_data = open("resulting_data.csv", 'w')
    resulting_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score,Net Score')
    resulting_data.write('\n')

    for line in lines[1:]:
        columns = line.replace("\n", "").split(",")
        rt_num = columns[1]
        reply_num = columns[2]
        pos_score = int(get_pos(columns[0]))
        neg_score = int(get_neg(columns[0]))
        net_score = -neg_score + pos_score
        row_string = "{},{},{},{},{}".format(rt_num, reply_num, pos_score, neg_score, net_score)
        resulting_data.write(row_string)
        resulting_data.write("\n")
    resulting_data.close()
