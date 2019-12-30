import unittest
import pytest
from ex_01 import process_seq

def test_cool_processing(capsys):
    seq = [{'name': 'Austin', 'rate': 31, 'category': 'GHT' }]

    # make it stop, it hurts
    process_seq(seq)
    out, err = capsys.readouterr()
    assert 'Do some cool processing\n' == out

def test_less_cool_processing(capsys):
    seq = [{'name': 'Austin', 'rate': 31, 'category': 'SBT' }]

    # make it stop, it hurts
    process_seq(seq)
    out, err = capsys.readouterr()
    assert 'This processing is less cool\n' == out