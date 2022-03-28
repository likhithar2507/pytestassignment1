import area
import pytest

def test_area_square():
    side = 3
    result = area.area_square(side)
    assert result == side * side

def test_perimeter_rect():
    l=2
    w=3
    result=area.perimeter_rect(l,w)
    assert result == 2*(l+w)

def test_area_rect():
    l=3
    b=2
    result=area.area_rect(l,b)
    assert result == l*b

def test_area_circle():
    r=4
    PI = 3.14
    result=area.area_circle(r)
    assert result == PI * r * r

def test_area_triangle():
    a=3
    b=4
    c=5
    s=(a+b+c)/2
    result=area.area_triangle(a,b,c)
    assert result == (s * (s - a) * (s - b) * (s - c)) ** 0.5

