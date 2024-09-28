import requests
import re
from bs4 import BeautifulSoup
import click

    
def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html,'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+',raw_text)
 
def get_html_of(url):
    res = requests.get(url)
    if res.status_code != 200:
        print(f'The status code of {res.status_code} is not acceptable')
        return ''
    return res.content.decode()  
 
def get_top_words_from(all_words,length):
     word_count = word_counter(all_words,length)
     return sorted(word_count.items(), key = lambda item: item[1], reverse = True) 
 
def word_counter (all_words, length):
    word_count = {}
    for word in all_words:
        if len(word) < length:
            continue
        if word not in word_count:
            word_count[word] = 1
        else :
            counter = word_count.get(word)
            word_count[word] = counter + 1
    return word_count;       
    
    
    
@click.command()
@click.option('--url','-u',prompt='Please enter the url',help='Url of the webpage')
@click.option('--length','-l',default=0,help='Minimum length of the word(default value is zero)')
@click.option('--deep','-d',default=None,type = int,help='How many words to extract')
@click.option('--save','-s',default=None,help='Specify the file name to save the output')

def main(url,length,deep,save):
    all_words = get_all_words_from(url)
    top_words = get_top_words_from(all_words,length)
     
    if deep is None:
        deep = len(top_words) 
     
    if deep > len(top_words):
        print(f"Warning: Requested {deep} words, but only {len(top_words)} are available.")
        deep = len(top_words)

    output = []
    for i in range(deep):
        output.append(top_words[i][0]) 

    # Print to console
    for word in output:
        print(word)

    # Save to file if specified
    if save:
        with open(save, 'w') as f:
            for word in output:
                f.write(word + '\n')  
        print(f"___________________________________________________________________________OUTPUT SAVED TO {save}___________________________________________________________________________")

if __name__ == '__main__':
    main()
        
