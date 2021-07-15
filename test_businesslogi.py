import businesslogic as bl

def test_kg2g():
    assert bl.kg2g(1) == 1000
    assert bl.kg2g(0) != 1
    assert bl.kg2g(-1) != 1000

def test_kg2p():
    assert bl.kg2p(1) == 2.205
    assert bl.kg2g(0) != 1
    assert bl.kg2g(-1) != 2.21

def test_kg2o():
    assert bl.kg2o(1) == 35.274
    assert bl.kg2g(0) != 1
    assert bl.kg2g(-1) != 35.27

def test_m2cm():
    assert bl.m2cm(1) == 100
    assert bl.m2cm(0) != 1
    assert bl.m2cm(-1) != 100

def test_m2f():
    assert bl.m2f(1) == 3.281
    assert bl.m2f(0) != 1
    assert bl.m2f(-1) != 3.281

def test_m2i():
    assert bl.m2i(1) == 39.37
    assert bl.m2i(0) != 1
    assert bl.m2i(-1) != 39.37

def test_c2f():
    assert bl.c2f(0) == 32
    assert bl.c2f(-1) != 32

def test_c2k():
    assert bl.c2k(0) == 273.15
    assert bl.c2k(-1) != 273.15
 