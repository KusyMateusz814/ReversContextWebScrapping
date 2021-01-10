from selenium import webdriver
import os
import sys
import argparse

#dodaje do scieszki obecny folder, co pozwala skorzystac z geckodrivera000
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
    lang_from = sys.argv[1]    # jezyk z ktorego jest cytat
    lang_to = sys.argv[2]      # jezyk w ktorym szukam omawianego cytatu
    sentence = sys.argv[3]     # cytat
    number_to_reverso = 8      # liczba przykladow w source i destination języku
    if len(sys.argv) < 5:      #
        number_to_reverso = 8
    else: 
        number_to_reverso = int(sys.argv[4])*2
    def_environment()
    def_reverso_context(lang_from, lang_to, sentence, number_to_reverso)

if __name__ == "__main__":
    if sys.argv[1] == "-l":
        print('do zrobienia pobieranie jezykow')
    elif len(sys.argv)> 2:
        main()

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="show language to converse - source and destination")
#args = parser.parse_args()


