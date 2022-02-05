#!/usr/bin/python3
""" 2. LIFO Caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get' for implement
      LIFO caching system
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
        - must discard the last item put in cache (LIFO algorithm)
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
                penultimate_in__key_element = sorted_dict_keys[-2]
                del self.cache_by_time[penultimate_in__key_element]
                del self.cache_data[penultimate_in__key_element]
                print('DISCARD: {}'.format(penultimate_in__key_element))

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
