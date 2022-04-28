from src.Processing import input_processing, input_processing_for_tests, output_processing

if __name__ == '__main__':
    grammar = input_processing_for_tests()
    word = input()
    output_processing(word, grammar)
