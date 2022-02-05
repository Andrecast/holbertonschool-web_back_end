#!/usr/bin/python3
""" 1. FIFO caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get' for implement
      FIFO caching system
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
        - must discard the first item put in cache (FIFO algorithm)
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
                first_in_key_element = sorted_dict_keys[0]
                del self.cache_by_time[first_in_key_element]
                del self.cache_data[first_in_key_element]
                print('DISCARD: {}'.format(first_in_key_element))

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
