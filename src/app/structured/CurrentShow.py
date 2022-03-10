class CurShow:

    title = None
    desc = None

    image_s = None
    image_m = None
    image_l = None

    syno_s = None
    syno_m = None
    syno_l = None

    keywords = None

    category = None
    topic = None

    channel = None

    def __init__(self, df):
        self.title = df['title']
        self.desc = df['description']

        self.image_s = df['image_s']
        self.image_m = df['image_m']
        self.image_l = df['image_l']

        self.syno_s = df['syno_s']
        self.syno_m = df['syno_m']
        self.syno_l = df['syno_l']

        self.keywords = df['keywords']

        self.category = df['category']
        self.topic = df['topic']

        self.channel = df['channel']


