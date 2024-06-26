from pydantic import BaseModel


class BaseDocument(BaseModel):
    title: str
    summary: str
    content: str
    source: str
    published_at: str

    def to_json(self):
        return {
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "source": self.source,
            "published_at": self.published_at,
        }
