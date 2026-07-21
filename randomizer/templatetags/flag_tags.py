from django import template

from ..types.settings import Settings

register = template.Library()


@register.filter
def flag_tooltip(flag, letter):
    """Prefix a setting's tooltip with its flag-string coordinates.

    e.g.  S(shopqual)
          Default: original

    followed by the flag's existing HTML description. ``letter`` is the
    category letter (the subcategory id).

    Returns a plain (unsafe) string so Django autoescapes it in the title
    attribute exactly as ``{{ flag.description }}`` did before: the browser
    decodes the entities back to HTML when reading the attribute, and
    Bootstrap (data-bs-html="true") renders it. Escaping keeps quotes in the
    description from terminating the attribute early.
    """
    default = Settings.default_value_string(flag)
    return f"{letter}({flag.id})<br>Default: {default}<br><br>{flag.description}"
