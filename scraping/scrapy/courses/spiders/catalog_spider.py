from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from courses.items import CourseItem
import re

class CatalogSpider(BaseSpider):
    name = "catalog"
    #allowed_domains = ["cmu.edu"] #?
    #start_urls = ["http://coursecatalog.web.cmu.edu/schoolofcomputerscience/"]
    course_number = "15-122" # get this from somewhere else later
    start_urls = [("http://coursecatalog.web.cmu.edu/ribbit/?page=getcourse.rjs&code=" + course_number)]

    def parse(self, response):
        # Create xml selector & get its contents as a string for regex parsing
        xxs = XmlXPathSelector(response)
        data = str(xxs.select('/courseinfo').extract())
        
        # Create course item
        item = CourseItem()

        # Get course number from url
        number_regex = re.compile('(..-...)')
        number_match = number_regex.search(response.url)
        if (number_match != None):
            number_match.group()
            item['number'] = number_match.group(1)
        
        # Construct regular expression for prerequisite decoding
        prereq_regex = re.compile('Prerequisite(?:s)?:(.*)(\.')
        
        match = prereq_regex.search(data)
        if (match == None):
            print item
            return
        else:
            match.group()
            print match.group(1)
            item['prereqs'] = match.group(1)
    
        print item


            
