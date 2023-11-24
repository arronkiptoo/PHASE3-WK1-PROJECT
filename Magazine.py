from Articles import Article


class Magazine:
    _magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def all(self):
        return Magazine._magazines

    def find_by_name(cls, name):
        return next((magazine for magazine in cls._magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls._magazines:
            titles.extend(article.title() for article in magazine._articles)
        return titles

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author()
            authors_count[author] = authors_count.get(author, 0) + 1

        return [author for author, count in authors_count.items() if count > 2]
