# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from tkinter import *
from datetime import datetime
import pytz
import traceback
import re

###############################################################
###############################################################

"""
Code for retrieving and parsing Google and Yahoo News feeds
DO NOT CHANGE THIS CODE
"""

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        # assume the news we get is in GMT
        pubdate = pubdate.replace(tzinfo=pytz.timezone("GMT"))
        # convert to EST
        pubdate = pubdate.astimezone(pytz.timezone('EST'))
        # remove timezone information for simplicity
        pubdate = pubdate.replace(tzinfo=None)

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

# end of helper code

###############################################################
################  Data structure design  ######################
###############################################################

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        Create a class, NewsStory, with the following
        attributes and getter methods:

        Attributes:
            guid - a string
            title - a string
            description - a string
            link - a string
            pubdate - a datetime

        Getter methods:
            get_guid(self)
            get_title(self)
            get_description(self)
            get_link(self)
            get_pubdate(self)
        """

        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

###############################################################
########################  Triggers  ###########################
###############################################################

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

#=============================================================
#                       PHRASE TRIGGERS
#=============================================================

# Problem 2
class PhraseTrigger(Trigger):

    """
    Implement PhraseTrigger as subclass of Trigger.

    Attribute:
        phrase - a string

    Method:
        is_phrase_in - takes in one string argument text.
            It returns True if the whole phrase phrase is present,
            False otherwise, as described in the above examples.
            NOT case-sensitive. Implement this method.

    Valid Phrases:
    'PURPLE COW'
    'The purple cow is soft and cuddly.'
    'The farmer owns a really PURPLE cow.'
    'Purple!!! Cow!!!'
    'purple@#$%cow'
    'Did you see a purple     cow?'

    NOT Valid Phrases:
    'Purple cows are cool!'
    'The purple blob over there is a cow.'
    'How now brown cow.'
    'Cow!!! Purple!!!'
    'purplecowpurplecowpurplecow'
    """
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase.lower()
        self.phrase = self.phrase.split()


    def is_phrase_in(self, text):
        # Use regular expressions to clean the phrase of punctutation and extra characters
        self.text = text.lower()
        self.clean_text = re.findall(r"[\w']+", self.text)

        # Find the intersection of the two lists
        self.intersection = list(set(self.phrase) & set(self.clean_text))

        # If the phrase is equal to the intersection, return True
        if self.phrase in self.intersection:
            return True
        else:
            return False

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, title):
        """
        Implement TitleTrigger as subclass of PhraseTrigger.

        Fires when a news item's title contains a given phrase.

        Needs a working evaluate method.
        """
        PhraseTrigger.__init__(self, title)

    def evaluate(self, story):
        self.title = story.get_title()

        self.is_phrase_in(self.title)



# Problem 4
# TODO: DescriptionTrigger
"""
Implement DescriptionTrigger as subclass of PhraseTrigger.

Fires when a news item's description contains a given phrase.

Needs a working evaluate method.
"""

#============================================================
#                         TIME TRIGGERS
#============================================================
##Time Trigger - this is already implemented for you
##DO NOT CHANGE THIS CODE
class TimeTrigger(Trigger):
    def __init__(self, time):
        """
        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        """
        time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        self.time = time

# Problem 5
# TODO: BeforeTrigger and AfterTrigger
"""
Implement BeforeTrigger and AfterTrigger as subclass of TimeTrigger.

BeforeTrigger fires when a story is published strictly before the
trigger’s time.

AfterTrigger fires when a story is published strictly after the
trigger’s time.

Needs a working evaluate method.
"""

#============================================================
#                         COMPOSITE TRIGGERS
#============================================================


# Problem 6
# TODO: NotTrigger
"""
Implement a class NotTrigger.

Take in as input a trigger and returns its inverted value.

Needs a working evaluate method.
"""

# Problem 7
# TODO: AndTrigger
"""
Implement a class AndTrigger.

This trigger should take two triggers as arguments
to its constructor, and should fire on a news story
only if both of the inputted triggers would fire on that item.

Needs a working evaluate method.
"""

# Problem 8
# TODO: OrTrigger
"""
Implement a class OrTrigger.

This trigger should take two triggers as arguments
to its constructor, and should fire if either one (or both)
of its inputted triggers would fire on that item.

Needs a working evaluate method.
"""

###############################################################
########################  Filtering  ##########################
###############################################################

# Problem 9
# TODO: FilterStories
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in
    triggerlist fires.
    """
    # YOUR CODE HERE
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    print(len(stories))
    return stories


###############################################################
##################  User-Specified Triggers  ##################
###############################################################

# Problem 10
# TODO: ReadTriggerConfig
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)


    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # this should return a list of triggers specified by the configuration file

    # YOUR CODE HERE
    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("russia")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Conway")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 10
        # TODO: After implementing read_trigger_config, uncomment this line
        # triggerlist = read_trigger_config('triggers.txt')

        print("triggers:", triggerlist)

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        traceback.print_exc()
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
