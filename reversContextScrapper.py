from selenium import webdriver
import os
import sys
import argparse
import logging

def def_params():
    parser = argparse.ArgumentParser(
            description="program do pobierania danych z reverscontect"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug mode")
    parser.add_argument("-f", "--fromLang", required=True, help="język do tłumaczenia")
    parser.add_argument("-t", "--toLang", required=True, help="język docelowy tłumaczenia")
    parser.add_argument("-s", "--sentence", required=True, help="zdanie do przetłumaczenie")
    parser.add_argument("-n", "--numberToReverso", default=8, help="liczba kontekstów do wyświetlenia")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    return args

#dodaje do scieszki obecny folder, co pozwala skorzystac z geckodrivera
def def_environment():
    path_to_dir = os.path.dirname(os.path.realpath(__file__))
    print("Scieszka do folderu:"+path_to_dir)
    os.environ["PATH"] += os.pathsep + path_to_dir

def create_url(lang_from, lang_to, sentence):
    replace_space_sentences = sentence.replace(' ','+')
    url_basic='https://context.reverso.net/translation/'
    return url_basic+''+lang_from+'-'+lang_to+'/'+replace_space_sentences

def def_reverso_context(lang_from, lang_to, sentence, number_to_reverso):
    sentence_url=create_url(lang_from, lang_to, sentence)
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(sentence_url)
    #to skopiowalem prosto z przegladarki
    element = driver.find_element_by_xpath('//*[@id="examples-content"]')

    all_lines = element.text.split('\n') #zapisuje calosc do jednego
    len_element= len(all_lines)
    print("Całkowita liczba elementów:" + str(len_element))
    for val in range(number_to_reverso):
        print("  " + all_lines[val])
    driver.quit()

def main():
    args=def_params()
    logging.debug("Only shown in debug mode")
    logging.debug("args.sentence: "+args.sentence)
    logging.debug("args.fromLang: "+args.fromLang)
    logging.debug("args.toLang:   "+args.toLang)
    sentence  = args.sentence
    lang_from = args.fromLang
    lang_to  = args.toLang
    number_to_reverso = args.numberToReverso
    def_environment()
    def_reverso_context(lang_from, lang_to, sentence, number_to_reverso)

if __name__ == "__main__":
    main()

