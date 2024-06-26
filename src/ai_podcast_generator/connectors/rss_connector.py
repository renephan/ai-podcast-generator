from ai_podcast_generator.connectors.base_connector import BaseConnector
import feedparser


class RSSConnector(BaseConnector):
    url: str

    def fetch(self):
        return feedparser.parse(self.url)
