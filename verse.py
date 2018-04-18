class Verse(object):
    def __init__(self, book, chapter, verse, text):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.text = text

    def __str__(self):
        return self.book + " " + self.chapter + ":" + self.verse + " " + self.text

    def convertToVec(self):
    	pass

    #Dictionary: Key(Book name), Value(List chapters, each being a list of verses)