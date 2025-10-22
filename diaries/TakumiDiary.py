from diaries.AbstractDiary import AbstractDiary

class TakumiDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "大海賊時代の幕が開けた"

    def get_author(self):
        return "Sample"