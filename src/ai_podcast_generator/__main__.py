from ai_podcast_generator.config import load_settings_from_json
from ai_podcast_generator.connectors.rss_connector import RSSConnector

settings = load_settings_from_json("config.json")

if settings.data_sources.rss:
    for rss_source in settings.data_sources.rss:
        rss_connector = RSSConnector(url=rss_source.feed_url)
        res = rss_connector.fetch()
        res
