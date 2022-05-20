#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest
import time,os

@pytest.mark.check_tmpdir
def test_tmpdir(tmpdir):
    a_file = tmpdir.join('somthing.txt')

    a_sub_dir = tmpdir.mkdir('anything')

    another_file = a_sub_dir.join('123.txt')

    a_file.write('213456ytfdsaf')

    another_file.write('213456ytfdsaf')

    print("a_file       临时文件的路径是：{}".format(os.path.abspath(a_file)))
    print("another_file 临时文件的路径是：{}".format(os.path.abspath(another_file)))

    # time.sleep(10)

    assert a_file.read() == another_file.read()

@pytest.mark.check_tmpdir_factory
def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')

    base_temp = tmpdir_factory.getbasetemp()
    print('base_tmpdir:',base_temp)

    a_file = a_dir.join('somthing.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('another.txt')

    a_file.write('213456ytfdsaf')
    another_file.write('213456ytfdsaf')

    # print("a_file       临时文件的路径是：{}".format(os.path.abspath(a_file)))
    # print("another_file 临时文件的路径是：{}".format(os.path.abspath(another_file)))

    # time.sleep(10)

    assert a_file.read() == another_file.read()


