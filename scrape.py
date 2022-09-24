import requests
from bs4 import BeautifulSoup
import pprint #built in module- to print beutifully in the terminal

response = requests.get("https://news.ycombinator.com/news") # requesting repose to grab the link and download the html files
# print(response) - RESPONSE 200
# print(response. text) - will print the entire html file nd then we grab the data from the html and using BeautifulSoup clean up the data
response2 = requests.get("https://news.ycombinator.com/news?p=2") # if we want page 2
soup = BeautifulSoup(response.text, "html.parser")  #BeautifulSoup is converting response.text which is in string format to a html and then we are assigning it to an object called soup
# there are many types of parsers in BeautifulSoup like html parser, xml parser
soup2 = BeautifulSoup(response2.text, "html.parser")
# print(soup) - prints the html of the webpage print(soup.body) - body of the html file print(soup.body.content) - grabs the content but in a list format
# print(soup.find_all("div")) - grabs the div objects that are there int he html file
# print(soup.find_all("a")) - grabs all the anchor tags(link) print(soup.title) - title of the html print(soup.a) - grabs the first anchor tag on the html
# print(soup.find("a")) - finds the first anchor tag in the html file
# print(soup.find(id = "score_20514755")) - finds the first class id tag with the score given in the html file
# print(soup.select(".scores")) - selectin all classes of scores using css selectors
# print(soup.select(#score_20514755))
# If we wanna grab the first link in the and also the no. of upvotes then:
# print(soup.select(".titlelink")[0]) #cus it will print all the classes with titlelink...as we want the first one [0]
links = soup.select(".titlelink")  # to grab all the links in the page
subtext = soup.select(".subtext") # to grab all the votes using the score class .-class #-id
links2 = soup2.select(".titlelink")
subtext2 = soup2.select(".subtext")
# print(votes[0].get("id")) - grabs the 1st links votes and prints out its id. votes is a list here
mega_link = links + links2  # addin both the links
mega_subtext = subtext + subtext2
def sort_stories_by_votes(hnlist): #hn - hackernews # willl sort ascendin to descendin
    # sorted(hnlist) - will give an error cus its in dictionary and python doesnt know in which manner to sort it as in usin titles or wat
    # sorted(hnlist, key = lambda k: k["votes"]) - to sort dictionories using keys we use lambda
    return sorted(hnlist, key=lambda k: k["votes"], reverse = True)  # to reverse the order



def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links): # enumerate gives index also
        title = links[index].getText()  # gets only the text nd no link. Thus the title is useless without the link so:
        href = links[index].get("href", None) #if the link is broken in href attribute then the default becomes None
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))  # we can get an error by this if a story haas no votes
            # replaces points with just a space string
            if points>=100:
                hn.append({"title": title,"link": href, "votes": points})  # to add both the links and titles
    return sort_stories_by_votes(hn) # we want the list to be sorted frm highest votes to the least
pprint.pprint(create_custom_hn(mega_link, mega_subtext))



