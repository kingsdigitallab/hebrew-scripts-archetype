# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# PROJECT settings
# PLEASE DO NOT PLACE ANY SENSITIVE DATA HERE (password, keys, personal
# data, etc.)
# Use local_settings.py for that purpose

# Lightbox
"""
The Lightbox is a separate project, even though it's still tightly linked to Digipal. It is possible to install it through pip:
>>> pip install git+https://github.com/Gbuomprisco/Digital-Lightbox.git
By default, it is disabled. You can enable it by setting the variable LIGHTBOX in your settings:
"""
LIGHTBOX = False

# Mezzanine
# SITE_TITLE = 'The community of the realm in Scotland'
SITE_TITLE = 'Hebrew Scripts - Archetype'

# Social
"""
The following variables contains the URLs/username to social networking sites.
- The TWITTER variable asks for the Twitter username.
- The GITHUB variable asks for the relative URL to your Github project or account
- The COMMENTS_DISQUS_SHORTNAME asks for the Disqus shortname
"""
TWITTER = ''
GITHUB = ''
# COMMENTS_DISQUS_SHORTNAME = "exondomesday"

# Annotator Settings

"""
If True, this setting will reject every change to the DB. To be used in production websites.
"""
REJECT_HTTP_API_REQUESTS = False  # if True, prevents any change to the DB

"""
This setting allows to set the number of zoom levels available in the OpenLayers layer.
"""
ANNOTATOR_ZOOM_LEVELS = 7  # This setting sets the number of zoom levels of O

FOOTER_LOGO_LINE = True

# Customise the faceted search settings
MODELS_PRIVATE = ['itempart', 'images', 'graphs', 'textcontentxml']
MODELS_PUBLIC = MODELS_PRIVATE

DEBUG_PERFORMANCE = False
COMPRESS_ENABLED = True
COMPRESS_ENABLED = False

from customisations.digipal.views.faceted_search.settings import FACETED_SEARCH

# CUSTOM_APPS = ['exon.customisations.mapping']

TEXT_IMAGE_MASTER_CONTENT_TYPE = 'transcription'
KDL_MAINTAINED = True

_TEXT_EDITOR_OPTIONS_CUSTOM = {
    'buttons': {
        'btnHeading': {'label': 'Heading', 'tei': '<head>{}</head>', 'color': '#efffb0'},
        'btnHeadingEmphasised': {'label': 'Heading (rubricated)', 'tei': '<head rend="emphasised">{}</head>'},
        'btnChapterNumber': {'label': 'Chapter Number', 'tei': '<cn>{}</cn>', 'color': '#ffe7bc'},
        'btnSentenceNumber': {'label': 'Sentence Number', 'tei': '<sn>{}</sn>', 'color': '#ffe7bc'},
        'btnPageNumber': {'label': 'Locus', 'tei': '<location loctype="locus">{}</location>', 'color': '#ffe7bc'},
        'btnStructure': {'label': 'Structure', 'buttons': [
            'btnHeading', 'btnHeadingEmphasised', 'btnChapterNumber', 'btnSentenceNumber', 'btnPageNumber'
        ]},

        'btnUnsettled': {'label': 'Unsettled (shared)', 'tei': '<seg type="unsettled">{}</seg>'},
        'btnUnsettledUnique': {'label': 'Unsettled (unique)', 'tei': '<seg type="unsettled" subtype="unique">{}</seg>'},
        'btnGenetic': {'label': 'Genetics', 'buttons': [
            'btnUnsettled', 'btnUnsettledUnique'
        ]},

        'btnAddedAbove': {'label': 'Added (above)', 'tei': '<add place="above">{}</add>'},
        'btnAddedInline': {'label': 'Added (inline)', 'tei': '<add place="inline">{}</add>'},
        'btnDeletedStruck': {'label': 'Deleted (struck)', 'tei': '<del rend="strikethrough">{}</del>', 'plain': 1},
        'btnDeletedErased': {'label': 'Deleted (erased)', 'tei': '<del rend="erased">{}</del>'},
        'btnRedInk': {'label': 'Red Ink', 'tei': '<hi rend="color(ret)">{}</hi>', 'color': '#ffc9c9'},
        'btnHighlighted': {'label': 'Highlighted', 'tei': '<hi rend="highlight">{}</hi>'},
        'btnSuperscripted': {'label': 'Superscripted', 'tei': '<hi rend="sup">{}</hi>', 'plain': 1},
        'btnScribal': {'label': 'Scribal Intervention', 'buttons': [
            'btnAddedAbove', 'btnAddedInline', 'btnDeletedStruck', 'btnDeletedErased',
            'btnRedInk', 'btnHighlighted', 'btnSuperscripted'
        ]},

        'btnVernacular': {'label': 'Vernacular', 'tei': '<seg lang="vernacular">{}</seg>', 'plain': 1},
        'btnHandShift': {'label': 'New Hand', 'tei': '<newhand>{}</newhand>'},
        'btnOther': {'label': 'Other', 'buttons': [
            'btnVernacular', 'btnHandShift',
        ]},
    },
    'show_highlights_in_preview': 1,
    'toolbars': {
        'default': 'psclear undo redo pssave | psconvert | btnStructure btnGenetic btnScribal btnOther | code ',
    },
    'panels': {
        'north': {
            'ratio': 0.0
        },
        'east': {
            'ratio': 0.0
        },
    }
}
