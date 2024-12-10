from pathlib import Path

from django import template
from django.template.defaultfilters import stringfilter
from markdown import Markdown

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    r = {}
    path = Path(value)
    with path.open("r") as f:
        content = f.read()
    m = Markdown(
        extensions=[
            "extra",
            "nl2br",
            "sane_lists",
            "meta",
            "toc",
        ],
    )
    r["html"] = m.convert(content)
    r["meta"] = m.Meta
    return r
