# importing module
import sys
# appending a path
sys.path.append('../src')
import cinquis.bow as bw


def main():
    print('test_bw_bow_from_json')
    #bw.bow_from_json('intents.json')
    bow = bw.bow_from_json('intents.json')
    #print (len(bow.all_words))

    #test text output
    #for pattern_sentence, tag in bow.xy:
        #print(pattern_sentence)
        #print(tag)
        #print('======================================================')
    #print(str(bow.getAllWordsLen()))

    #test bag of words output
    for pattern_sentence, tag in bow.xy:
        print(pattern_sentence)
        print(bw.bag_of_words_from_cleaned(pattern_sentence, bow.all_words))
        print(tag)
        print('======================================================')

    for t in range(len(bow.y_train)):
        print(bow.y_train[t])
        print(bow.X_train[t])


    #print(len(bow.y_train))
    #print(len(bow.X_train))


    print('test complete')


if __name__ == "__main__":
    main()
