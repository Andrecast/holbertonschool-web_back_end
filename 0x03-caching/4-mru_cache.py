#!/usr/bin/python3
""" 4. MRU Caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get' for implement
      MRU caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_by_time = {}

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key key
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        - must discard the most recently used item (MRU algorithm)
        - must print DISCARD: with the key discarded and following by
        a new line
        """
        if key and item:
            self.cache_by_time[key] = datetime.now()
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_dict_keys = sorted(
                                          self.cache_by_time,
                                          key=self.cache_by_time.get)
                most_recently_used_item_key = sorted_dict_keys[-2]
                del self.cache_by_time[most_recently_used_item_key]
                del self.cache_data[most_recently_used_item_key]
                print('DISCARD: {}'.format(most_recently_used_item_key))

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        element = self.cache_data.get(key)
        if element:
            self.cache_by_time[key] = datetime.now()
        return element
