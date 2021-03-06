import os, os.path
import nose.tools           as nose
import biobox_cli.container as ctn

def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def is_ci_server():
    return "CI" in os.environ.keys()

def remove_container(container):
    if not is_ci_server():
        ctn.remove(container)

def assert_file_not_empty(file_):
    file_size = os.stat(file_).st_size
    nose.assert_not_equal(file_size, 0,
            "File should not be empty but is: {}".format(file_))

def assert_file_contents_equal(file_, contents):
    with open(file_, 'r') as f:
        nose.assert_equal(f.read(), contents)
