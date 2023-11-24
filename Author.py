from Articles import Article


class Author:
    _authors = []

    def __init__(self, name):
        self._name = name
        self._articles = []
        self._magazines = []
        Author._authors.append(self)

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(self._magazines))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        self._magazines.append(magazine)

    def topic_areas(self):
        return list(set(magazine.category() for magazine in self._magazines))
