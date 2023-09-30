#if this does not work, go into terminal and install the libraries
#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
#pip install requests

import webbrowser
import urllib3
from bs4 import BeautifulSoup
import time
try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' found")



#filters the url results from the google search based on if it contains the word we are looking for
def Title_Filter(title, url, text):
    newurl = []
    newtitle = []

    for words in text:
        i = 0
        for names in title:
            word2 = words[:-1]
            #most disgusting if statement ever
            #looks at title of article (the name you get from googlesearch) and sees if the word itself we are looking for is there,
            #also looks at the full uppercase and full lowercase version of the title
            if words in names or word2 in names or words.upper() in names or word2.upper() in names or words.lower() in names or word2.lower() in names:
                newurl.append(url[i])
                newtitle.append(names)
            i+=1

    return newurl, newtitle

#gets the title of the webpage given a url, used for title filtering in the function above
def Get_Title(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    htmlSource = r.data
    soup = BeautifulSoup(htmlSource, "html.parser")
    return soup.title.text

#searches Google for the Handspoeak webpages for the words in the sentence
def Get_GoogleSearch(word, refined):
    #list and query needed to search
    query = "Handspeak " + word
    url_list = []

    #Get search results into a list
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    	#print(j)
        url_list.append(j)

    #only looks for Handspeak websites
    substring = "https://www.handspeak.com/word/index.php"
    for l in url_list:
        if substring in l:
            #a good link to use
            refined.append(l)
            #webbrowser.open(l)



#basically runs all of the other functions, doing the whole translation process
def Translate(inputtext):
    #initialized some things
    refined = []
    test = inputtext
    #split the input text word by word and search for the Handspeak articles for each word
    splitted = test.split()
    for a in splitted:
        Get_GoogleSearch(a, refined)

    #print the list of links
    print("Refined list of links: ")

    #gets a list of titles
    titles = []
    for b in refined:
        titles.append(Get_Title(b))


    #filter the titles
    refined, titles = Title_Filter(titles, refined, splitted)
    count = 0
    max = len(titles)
    while (count < max):
        print(titles[count])
        print(refined[count])
        count += 1

    for link in refined:
        webbrowser.open(link)
        time.sleep(1)



