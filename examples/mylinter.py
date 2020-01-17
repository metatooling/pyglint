import astroid

import pyglint


group = pyglint.CheckerGroup("mylinter")


BAD_NAME = group.problem(
    name="bad-name",
    text="The name '{name}' is against the guidelines.",
    explanation="It's a good idea to have a useful and descriptive name. For example, Counter instead of ctr.",
)

IMPORT_FROM = group.problem(
    "import-from",
    text="`from ... import` is not allowed.",
    explanation="Namespaces are one honkin' great idea.",
)


@group.check(astroid.node_classes.Name)
def find_short_names(checker, node):
    if len(node.name) < 4:
        yield pyglint.message(problem=BAD_NAME, node=node, name=node.name)


@group.check(astroid.node_classes.ImportFrom)
def find_import_from(checker, node):
    yield pyglint.message(problem=IMPORT_FROM, node=node)


def register(linter):
    """Register checkers."""
    checker = pyglint.make_pylint_checker(group)
    linter.register_checker(checker(linter))
