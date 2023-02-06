# importing module
import sys
# appending a path
sys.path.append('../src')
import cinquis.intents as ci


def main():
    print('test_intents')
    varNumcorpus = 'Corpus/r1.txt'
    varStringcorpus = 'Corpus/r2.txt'
    varVarcorpus = 'Corpus/r3.txt'
    ci.addIntent("trump", varNumcorpus, "trump news")
    ci.addIntent("covid", varStringcorpus, "covid news")
    ci.addIntent("biden", varVarcorpus, "biden news")
    ci.createIntents('intents.json')
    print('test complete')

    #if len(sys.argv) > 3:
        #if(sys.argv[1]) == 'make_intent_from_file':
            #make_intent_from_file(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])


#def make_intent_from_file(tag,filepath,response,intentsFilePath):
    #it.addIntent(tag,filepath,response)
    #it.createIntents(intentsFilePath)



if __name__ == "__main__":
    main()
