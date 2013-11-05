# The models for your scraped items - the course descriptions & prereqs
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CourseItem(Item):
    number = Field() # course number
    prereqs = Field()  # any prerequisites
    coreqs = Field() # any corequisites
    antireqs = Field() # any anti-requisites
