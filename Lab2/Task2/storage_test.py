import unittest
import os
import storage as st

class StorageTest(unittest.TestCase):

    def test_user_list(self):
        storage = st.Storage()
        storage.switch('user1')
        storage.switch('user2')
        storage.switch('user1')
        storage.switch('user1')
        user_list = [
            'user1',
            'user2'
        ]
        self.assertEqual(set(user_list), set(storage.user_list()))

    def test_add(self):
        storage = st.Storage()
        storage.switch('user1')
        storage.add('str', ('tuple',), 1)
        storage.add(1, 2)
        container_list = [
            'str',
            ('tuple',),
            1,
            2
        ]
        self.assertEqual(set(container_list), set(storage.list()))

    def test_remove(self):
        storage = st.Storage()
        storage.switch('user1')
        storage.add('str', ('tuple',), 1)
        storage.add(1, 2)
        storage.remove(('tuple',))
        container_list = [
            'str',
            1,
            2
        ]
        self.assertEqual(set(container_list), set(storage.list()))

    def test_find(self):
        storage = st.Storage()
        storage.switch('user1')
        storage.add('str', ('tuple',), 1)
        find_set = storage.find(('tuple',), 32)
        find_expected_set = {
            ('tuple',)
        }
        self.assertEqual(find_set, find_expected_set)

    def test_open_load(self):
        storage = st.Storage()
        storage.switch('user1')
        storage.add('str', ('tuple',), 1)
        storage.save('test.txt')
        storage.switch('user2')
        storage.add(2)
        storage.load('test.txt')
        os.remove('test.txt')
        container_list = [
            'str',
            ('tuple',),
            1,
            2
        ]
        self.assertEqual(set(container_list), set(storage.list()))
