#!/usr/bin/env python

# All imports
import sys
import json
import urllib2
import io
import traceback
import os
from PIL import Image

# Define constants
API_ROOT = "http://xkcd.com/"


# The XKCD Command Line class
class XKCDCL:
    # Constructor for the XKCDCL
    def __init__(self):
        self.arg = ""
        self.api_url = ""
        self.comic_url = ""

        if len(sys.argv) >= 2:
            self.arg = sys.argv[1]

        self.display_comic()

    # Fetch the API url corresponding to current comic
    def get_api_url(self):
        if self.arg == "":
            # Fetch the currrent comic api url
            self.api_url = API_ROOT + "info.0.json"
        elif self.arg == "about":
            # Show about info
            self.show_about_info()
            sys.exit()
        else:
            # Fetch the api url of comic at given point
            self.api_url = API_ROOT + self.arg + "/info.0.json"

    # Get the comic url corresponding to current API call
    def get_comic_url(self):
        self.get_api_url()

        try:
            # Fetch the data from API endpoint
            data = json.load(urllib2.urlopen(self.api_url))
        except:
            print traceback.format_exc()
            print "No json response received. xkcd servers appear to be coma. Somebody wake up Munroe!"
            sys.exit()

        # Get the image URL from json data
        self.comic_url = data["img"]
        # Get the comic id from json data
        self.comic_id = data["num"]

    # Display the comic in the GUI system
    def display_comic(self):
        self.get_comic_url()

        try:
            # Fetch the image data
            fd = urllib2.urlopen(self.comic_url)
            comic_file = io.BytesIO(fd.read())

            # Show the image using PIL
            comic = Image.open(comic_file)
            comic.show()

            # Save the image
            user = str(os.getlogin())
            filename = "/home/" + user + "/Pictures/XKCD-CL/" + str(self.comic_id) + ".png"
            directory = os.path.dirname(filename)

            if not os.path.exists(directory):
                os.makedirs(directory)

	    comic.save(filename)
	    fd.close()

        except:
            print traceback.format_exc()
            print "Error: No such comic found! Try fetching comic no. 42."
            return

    # Show the about data of program
    def show_about_info(self):
        print "XKCD Command Line Utility (v" + __version__ + ")\n"
        print "Written by:"

        for email in __authors__:
            print __authors__[email] + " <" + email + ">"

        print "\nLicensed under " + __license__

# The main method
def main():
    XKCDCL()

# Invocation of the main method
if __name__ == "__main__":
	main()
	print "done"	
