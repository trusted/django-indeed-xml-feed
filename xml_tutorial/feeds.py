from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import SyndicationFeed, rfc2822_date
from django.utils.xmlutils import SimplerXMLGenerator
import datetime
from django.utils.timezone import utc
from django.utils.encoding import iri_to_uri
from jobs.models import Job


class IndeedFeed(SyndicationFeed):

    content_type = 'application/rss+xml; charset=utf-8'

    def write(self, outfile, encoding):
        handler = SimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("source", {})
        self.add_root_elements(handler)
        self.write_items(handler)
        handler.endElement("source")

    def add_root_elements(self, handler):
        super(IndeedFeed, self).add_root_elements(handler)
        handler.addQuickElement('publisher', 'ATS Name')
        handler.addQuickElement('publisherUrl', 'http://www.atssite.com')
        handler.addQuickElement("lastBuildDate", rfc2822_date(self.latest_post_date()))

    def write_items(self, handler):
        for item in self.items:
            handler.startElement('job', self.item_attributes(item))
            self.add_item_elements(handler, item)
            handler.endElement("job")

    def add_item_elements(self, handler, item):
        super(IndeedFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u"title", item['title'])
        handler.addQuickElement("date", item['date'])
        handler.addQuickElement("referencenumber", item['referencenumber'])
        handler.addQuickElement("url", item['link'])
        handler.addQuickElement("company", item['company'])
        handler.addQuickElement("sourcename", item['sourcename'])
        handler.addQuickElement("country", item['country'])
        handler.addQuickElement("email", item['email'])
        handler.addQuickElement("description", item['description'])


class JobsFeed(Feed):
    feed_type = IndeedFeed

    link = '/jobs/'

    def items(self):
        return Job.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_extra_kwargs(self, obj):
        """
        Returns an extra keyword arguments dictionary that is used with
        the `add_item` call of the feed generator.
        Add the 'content' field of the 'Entry' item, to be used by the custom feed generator.
        """
        return {
            'date': str(obj.date),
            'referencenumber': obj.referencenumber,
            'company': obj.company,
            'sourcename': obj.sourcename,
            'country': obj.country,
            'email': obj.email    
        }

  