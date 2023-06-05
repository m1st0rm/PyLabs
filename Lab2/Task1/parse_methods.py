import re


BEFORE_RE = r'(?<![^\s])'
BEFORE_WORD_RE = r'(?<![^\s\"\(])'

AFTER_END_RE = r'(?=\s*$)'
AFTER_ANY_RE = r'(?=\s+[^\s])'
AFTER_WORD_END_RE = r'(?=[\.\,\:\!\?\"\)\s]*$)'
AFTER_WORD_UPPER_RE = r'(?=[\.\,\:\!\?\"\)]*\s+[A-B])'
AFTER_WORD_LOWER_RE = r'(?=[\.\,\:\!\?\"\)]*\s+[^\sA-B])'

FORMAT_PARAMETERS_RE = dict(
    br=BEFORE_RE,
    bwr=BEFORE_WORD_RE,
    aer=AFTER_END_RE,
    aar=AFTER_ANY_RE,
    awer=AFTER_WORD_END_RE,
    awur=AFTER_WORD_UPPER_RE,
    awlr=AFTER_WORD_LOWER_RE,
)

WORD_ENDS_RE_LIST = [
    r'{bwr}(?i:etc\.)({awer}|{awur})',
    r'{bwr}(?i:i\.e\.)({awer}|{awur})',
    r'{bwr}(?i:e\.g\.)({awer}|{awur})',
    r'{bwr}(?i:c\.)({awer}|{awur})',
    r'{bwr}(?i:et\sal\.)({awer}|{awur})',
    r'{bwr}Dr\.{awer}',
    r'{bwr}Mr\.{awer}',
    r'{bwr}Mrs\.{awer}',
    r'{bwr}Lt\.{awer}',
    r'{bwr}Rep\.{awer}',
    r'{bwr}Jan\.({awer}|{awur})',
    r'{bwr}Feb\.({awer}|{awur})',
    r'{bwr}Mar\.({awer}|{awur})',
    r'{bwr}Apr\.({awer}|{awur})',
    r'{bwr}Aug\.({awer}|{awur})',
    r'{bwr}Sept\.({awer}|{awur})',
    r'{bwr}Oct\.({awer}|{awur})',
    r'{bwr}Nov\.({awer}|{awur})',
    r'{bwr}Dec\.({awer}|{awur})',
    r'{bwr}\.\s\.\s\.({awer}|{awur})'
]

WORD_OMISS_RE_LIST = [
    r'{bwr}(?i:etc\.){awlr}',
    r'{bwr}(?i:i\.e\.){awlr}',
    r'{bwr}(?i:e\.g\.){awlr}',
    r'{bwr}(?i:c\.){awlr}',
    r'{bwr}(?i:et al\.){awlr}',
    r'{bwr}Dr\.({awlr}|{awur})',
    r'{bwr}Mr\.({awlr}|{awur})',
    r'{bwr}Mrs\.({awlr}|{awur})',
    r'{bwr}Lt\.({awlr}|{awur})',
    r'{bwr}Rep\.({awlr}|{awur})',
    r'{bwr}([A-Z]\.\s+)*[A-Z]\.({awlr}|{awur})',
    r'{bwr}Jan\.{awlr}',
    r'{bwr}Feb\.{awlr}',
    r'{bwr}Mar\.{awlr}',
    r'{bwr}Apr\.{awlr}',
    r'{bwr}Aug\.{awlr}',
    r'{bwr}Sept\.{awlr}',
    r'{bwr}Oct\.{awlr}',
    r'{bwr}Nov\.{awlr}',
    r'{bwr}Dec\.{awlr}',
    r'{bwr}\.\s\.\s\.{awlr}'
]


def list_to_re(re_list):
    return '(' + '|'.join(re_list).format(**FORMAT_PARAMETERS_RE) + ')'


def find_matches(regex, text, capture_group):
    match_list = list()

    for m in re.finditer(regex, text):

        if m[capture_group] != None:
            match_list.append(m[capture_group])

    return match_list


def sentences(text):
    sentence_re = r'{br}({0}|[^\.\!\?])+[\.\!\?][\.\!\?\"\)]*'.format(list_to_re(WORD_OMISS_RE_LIST), **FORMAT_PARAMETERS_RE)
    return find_matches(sentence_re, text, 0)


def non_declarative_sentences(text):
    non_declarative_sentence_re = r'{br}({0}|[^\.\!\?])+[\!\?][\.\!\?\"\)]*'.format(list_to_re(WORD_OMISS_RE_LIST), **FORMAT_PARAMETERS_RE)
    return find_matches(non_declarative_sentence_re, text, 0)


def sentence_count(text):
    return len(sentences(text))


def non_declarative_sentence_count(text):
    return len(non_declarative_sentences(text))
