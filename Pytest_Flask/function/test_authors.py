#!/usr/bin/env python3
# -*- coding: utf-8 -*

import json
import pytest

@pytest.mark.fixture_scope
def test_fixture_scope(author_file_json):
    with author_file_json.open() as file:
        data = json.load(file)
        print("data:",data)
        assert data['birr']['city'] == 'shenzhen'

@pytest.mark.fixture_scope
def test_fixture_scope2(author_file_json):
    with author_file_json.open() as file:
        data = json.load(file)
        print("len(data):",len(data))
        assert len(data) == 3