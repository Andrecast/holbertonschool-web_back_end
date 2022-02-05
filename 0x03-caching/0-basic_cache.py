#!/usr/bin/python3
""" 0. Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get'
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
