import bulrush

# Bulrush specific settings
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS
# THEME = "bulrush/bulrush"

PLUGIN_PATHS = ["assets"]
PLUGINS = ["assets"]

AUTHOR = ""
SITENAME = "CullyBlockParty"
SITEURL = ""
DEFAULT_DATE = "fs"
DEFAULT_CATEGORY = "Info"

PATH = "content"

STATIC_PATHS = [
    "images",
    "extra",  # this
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/style.css": {"path": "style.css"},
}

TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Email", "mailto:cullyneighborhoodblockparty@gmail.com"),
    ("Facebook Event Page", "#"),
    (
        "Amazon Wishlist",
        "https://www.amazon.com/hz/wishlist/ls/2G4PP9UICVTOK?ref_=wl_share",
    ),
    ("Volunteer Sign Up", "https://volunteersignup.org/9FX8C"),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = True
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

CATEGORY_SAVE_AS = ""
AUTHOR_SAVE_AS = ""

MENUITEMS = (
    ("Donate", "/donate-information/"),
    (
        "Espanol",
        "https://cullyblockparty-com.translate.goog/?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=en&_x_tr_pto=wapp",
    ),
)
