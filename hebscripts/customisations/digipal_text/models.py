# -*- coding: utf-8 -*-
from digipal_text.models import TextContentXML, TextUnits, TextUnit, ClassProperty
from digipal.utils import re_sub_fct
from digipal import utils as dputils
from django.db import models
import regex as re


def TextContentXML_convert(self):
    content = self.content

    # 1. Clean up

    # normalise spaces
    content = re.sub(ur'(?musi)&nbsp;', ur' ', content)
    content = re.sub(ur'(?musi)\n+', ur' ', content)
    content = re.sub(ur'(?musi) +', ur' ', content)

    # remove all style/lang/class attributes
    # mark spans for deletion
    # exception: span with line-through
    if 1:
        attribs_to_remove = set(['style', 'class', 'lang', 'data-mce-style'])

        xml = dputils.get_xml_from_unicode(content, ishtml=True, add_root=True)

        for element in xml.findall('.//*'):
            attribs = set(element.attrib.keys())

            intersection = attribs.intersection(attribs_to_remove)
            if intersection:
                # convert strikethrough and underline
                styles = element.attrib.get('style', '')
                if 'line-through' in styles or 'underline' in styles:
                    element.attrib['data-dpt'] = 'del'
                    element.attrib['data-dpt-rend'] = 'strikethrough'

                for att in intersection:
                    del element.attrib[att]

            if element.tag.lower() in ['div', 'span']\
                    and not element.attrib.keys():
                element.tag = 'deleteme'

            if element.tag.lower() in ['em']:
                # <seg lang="vernacular">{}</seg>
                element.tag = 'span'
                element.attrib['data-dpt'] = 'seg'
                element.attrib['data-dpt-lang'] = 'vernacular'

        content = dputils.get_unicode_from_xml(xml, remove_root=True)
        content = re.sub(ur'</?deleteme>', ur'', content)

    convert_pipes = 1
    if convert_pipes:
        # remove all line break markup so it can be reconstructed from
        # pipes
        while True:
            l = len(content)
            content = re.sub(
                ur'<span data-dpt="sb"[^>]*>([^<]*)</span>', ur'\1', content)
            if len(content) == l:
                break

        # convert WORD|WORD into WORD-|WORD
        content = re.sub(ur'(?musi)(\w)\|(\w)', ur'\1-|\2', content)
        # convert - | into -|
        content = re.sub(ur'(?musi)-s+\|', ur'-|', content)

        # convert | and -| into spans
        # content = re.sub(ur'(-?\|+)', ur'<span data-dpt="lb"
        # data-dpt-cat="sep">\1</span>', content)
        content = re.sub(
            ur'(-?\|+)', ur'<span data-dpt="sb">\1</span>', content)

    # remove nested line break spans (due to bugs with multiple
    # conversions)
    if 1:
        while True:
            l = len(content)
            content = re.sub(ur'(<span[^>]*>)\1([^<>]*)(</span>)\3',
                             ur'\1\2\3', content)
            if len(content) == l:
                break

    # c. ii: chapter number
    content = re.sub(
        ur'\bc\.? ([ivxl]+)\b', ur'<span data-dpt="cn">\1</span>', content
    )
    # (1): sentence number
    content = re.sub(
        ur'\((\d+)\)', ur'<span data-dpt="sn">\1</span>', content
    )
    # /f.XXXra/ : page break
    content = re.sub(
        ur'/f\.?\s*([\dX]+[rvab]+)/',
        ur'<span data-dpt="location" data-dpt-loctype="locus">\1</span>', content
    )

    if 1:
        def replace_unsetlled_unique(amatch):
            return replace_unsetlled(amatch)

        def replace_unsetlled(amatch, atype='unique'):
            # convert empty [] to [ - ]
            empty_unsettled = '...'

            ret = amatch.group(1)

            print(ret)

            return ret

        # [] : unsettled text - unique
        content = re.sub(
            ur'<strong>\[</strong>([^\[\]]*)<strong>\]</strong>',
            ur'<strong>[\1]</strong>',
            content
        )
        # [] : unsettled text - unique
        content = re.sub(
            ur'<strong>\s*\[([^]<]*)\]\s*</strong>',
            ur'<span data-dpt="seg" data-dpt-type="unsettled" data-dpt-subtype="unique">\1</span>',
            content
        )
        # [] : unsettled text - unique
        content = re.sub(
            ur'\[\s*<strong>([^]<]*)</strong>\s*\]',
            ur'<span data-dpt="seg" data-dpt-type="unsettled" data-dpt-subtype="unique">\1</span>',
            content
        )
        # [] : unsettled text - shared
        content = re.sub(
            ur'\[([^]<]*)\]',
            ur'<span data-dpt="seg" data-dpt-type="unsettled">\1</span>',
            content
        )

    content = re.sub(ur'<strong>(.*?)</strong>', ur'<span data-dpt="hi" data-dpt-rend="highlight">\1</span>', content)

    # (Title) ... | chapter title
    if 1:
        content = re.sub(
            ur'(?musi)\(\s*Title\s*\)(.+?)(</?p>|<span data-dpt="s[bn]"|<span data-dpt="head")',
            ur'<span data-dpt="head">\1</span>\2',
            content
        )

    self.content = content


TextContentXML.convert = TextContentXML_convert


def TextContentXML_save_with_element_ids(self, *args, **kwargs):

    # assign an id to all the unsettled elements
    xml = dputils.get_xml_from_unicode(
        self.content, ishtml=True, add_root=True)

    inc = 0
    from datetime import datetime
    now = datetime.utcnow()
    n = (now - datetime(1970, 1, 1)).total_seconds()

    for element in xml.findall('.//span[@data-dpt-type="unsettled"]'):

        if 'id' not in element.attrib:
            inc += 1
            aid = '%0.8x%x' % (n, inc)
            element.attrib['id'] = aid

    if inc > 0:
        content = dputils.get_unicode_from_xml(xml, remove_root=True)
        self.content = content

        self.save(*args, **kwargs)


TextContentXML.save_with_element_ids = TextContentXML_save_with_element_ids
