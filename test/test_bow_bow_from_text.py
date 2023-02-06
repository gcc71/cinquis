# importing module
import sys
# appending a path
sys.path.append('../src')
import cinquis.bow as bw

some_text = """
Franco Zeffirelli was a well-respected Italian stage and film director, producer, production designer, and politician. So when Zeffirelli,
in his role as the director of the 1968 film “Romeo and Juliet,” allegedly told teenage actors Olivia Hussey and Leonard Whiting there
would be no nudity shown, they said they believed him. Citizens: “Hey that Covid “Pandemic” thing sucked, millions died, and we would like
for that not to happen again. Can we address the ethicality of our biological research and put measures in place to ensure this doesn’t happen again?”
"""

sentence = """Can we address the ethicality of our biological research and
put measures in place to ensure this doesn’t happen again?"""


def main():
    print('test_bow')


    #print('tokenize test')
    #tokenized_sentence = ti.tokenize(sentence)
    #tokenized_text = ti.tokenize(some_text)
    #print(tokenized_sentence)
    #print(tokenized_text)


    #print('stem test')
    #sentence_words = [ti.stem(word) for word in tokenized_sentence]
    #text_words = [ti.stem(word) for word in tokenized_text]
    #print(sentence_words)
    #print(text_words)


    print('bag of words test')


    print(bw.bag_of_words(sentence, some_text))
    print('test complete')


if __name__ == "__main__":
    main()
