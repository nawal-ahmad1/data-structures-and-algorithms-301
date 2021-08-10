from stack_and_queue.stack_queue_brackets import validate_brackets

def test1():
    actual = validate_brackets('{Naw99})()]]]')
    assert actual == False

def test2():
    actual = validate_brackets('{([Hello])}')
    assert actual == True

def test3():
    actual = validate_brackets('{([Hello{]]85}])}')
    assert actual == False

def test4():
    actual = validate_brackets('{{([Nawa584[[][]])}}')
    assert actual == False
