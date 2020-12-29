import pytest
from flask import request


# Unit test for request page
with app.test_request_context('/display_number/5', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/display_number/5'
    assert request.number == 5