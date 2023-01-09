import random
import time

def get_word():
    words = ['cat', 'dog', 'bird', 'fish','Give me One dollar!']
    return random.choice(words)

def main():
    while True:
        word = get_word()
        print(word)
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        if user_input == word:
            print('딩동댕! 맞췄습니다.')
            print('Elapsed time: %.2f seconds' % elapsed_time)
        else:
            print('Incorrect!')

if __name__ == '__main__':
    main()
