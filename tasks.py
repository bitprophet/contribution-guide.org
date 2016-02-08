from invoke import Collection
from invocations import docs

ns = Collection(docs)
ns.configure({
    'sphinx': {
        'source': '.',
        'target': '_build',
        'target_file': 'index.html',
    },
})
