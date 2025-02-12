from . import otus


def application(environ, start_response):
    print(environ)
    ...
    start_response('200', [('Content-Type', 'text/plain')])
    yield otus.my_super_code()
