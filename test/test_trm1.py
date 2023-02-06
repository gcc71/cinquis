# importing module
import sys
# appending a path
sys.path.append('../src')
import cinquis.trm1 as m1

def main():
    print('test_trm1')
    m1.model_from_json('intents.json', 'data.pth')


if __name__ == "__main__":
    main()
