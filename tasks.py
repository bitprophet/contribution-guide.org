from invoke import Collection
from invocations import docs

ns = Collection(docs)
ns.configure({
    'sphinx.source': '.',
    'sphinx.target': '_build',
})
