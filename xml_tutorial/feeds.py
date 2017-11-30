from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import rfc2822_date
from django.utils.xmlutils import SimplerXMLGenerator
import datetime
from django.utils.timezone import utc
from django.utils.encoding import iri_to_uri
from jobs.models import Job


class IndeedFeed:
    "Base class for all syndication feeds. Subclasses should provide write()"
    def __init__(self, title, date, referencenumber, url, company, sourcename, country, email, description, **kwargs):
        def to_str(s):
            return str(s) if s is not None else s

        self.feed = {
            'title': to_str(title),
            'date': to_str(date),
            'referencenumber': to_str(referencenumber),
            'url': iri_to_uri(url),
            'company': to_str(company),
            'sourcename': to_str(sourcename),
            'country': to_str(country),
            'email': to_str(email),
            'description': to_str(description),
        }
        self.feed.update(kwargs)
        self.items = []

    def add_item(self, title, date, referencenumber, url, company, sourcename, country, email, description, **kwargs):
        """
        Add an item to the feed. All args are expected to be strings except
        pubdate and updateddate, which are datetime.datetime objects, and
        enclosures, which is an iterable of instances of the Enclosure class.
        """
        def to_str(s):
            return str(s) if s is not None else s
        item = {
            'title': to_str(title),
            'date': to_str(date),
            'referencenumber': to_str(referencenumber),
            'url': iri_to_uri(url),
            'company': to_str(company),
            'sourcename': to_str(sourcename),
            'country': to_str(country),
            'email': to_str(email),
            'description': to_str(description),
        }
        item.update(kwargs)
        self.items.append(item)

    def num_items(self):
        return len(self.items)

    def root_attributes(self):
        """
        Return extra attributes to place on the root (i.e. feed/channel) element.
        Called from write().
        """
        return {}

    def add_root_elements(self, handler):
        """
        Add elements in the root (i.e. feed/channel) element. Called
        from write().
        """
        pass

    def item_attributes(self, item):
        """
        Return extra attributes to place on each item (i.e. item/entry) element.
        """
        return {}

    def add_item_elements(self, handler, item):
        """
        Add elements on each item (i.e. item/entry) element.
        """
        pass

    def write(self, outfile, encoding):
        """
        Output the feed in the given encoding to outfile, which is a file-like
        object. Subclasses should override this.
        """
        raise NotImplementedError('subclasses of SyndicationFeed must provide a write() method')

    def writeString(self, encoding):
        """
        Return the feed in the given encoding as a string.
        """
        s = StringIO()
        self.write(s, encoding)
        return s.getvalue()

    def latest_post_date(self):
        return datetime.datetime.utcnow().replace(tzinfo=utc)






class JobsFeed(Feed):
    feed_type = IndeedFeed

    link = '/jobs/'

    def items(self):
        return Job.objects.all()

    


  