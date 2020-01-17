import astroid

import pyglint


chk = pyglint.CheckerGroup("mylinter")


BAD_NAME = chk.problem(
    name="bad-name",
    text="The name '{name}' is against the guidelines.",
    explanation="It's a good idea to have a useful and descriptive name. For example, Counter instead of ctr.",
)


@chk.check_for_problems(astroid.node_classes.Name, problems=[BAD_NAME])
def find_short_names(checker, node):
    if len(node.name) < 4:
        yield pyglint.message(problem=BAD_NAME, node=node, name=node.name)


@chk.check_for_problems(astroid.node_classes.Name, problems=[BAD_NAME])
def find_long_names(checker, node):
    if len(node.name) > 30:
        yield pyglint.message(problem=BAD_NAME, node=node, name=node.name)


@chk.standalone_check(
    astroid.node_classes.ImportFrom, text="`from ... import` is not allowed."
)
def import_from(checker, node):
    """Namespaces are one honkin' great idea."""
    yield pyglint.message(node=node)


def register(linter):
    """Register checkers."""
    checker = pyglint.make_pylint_checker(chk)
    linter.register_checker(checker(linter))
