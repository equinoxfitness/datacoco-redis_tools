import unittest

from datacoco_redis_tools.redis_tools import RedisInteraction


class TestRedisInteraction(unittest.TestCase):
    def test_set_key(self):
        self.testClass = RedisInteraction(
            "dev-dataredis.equinoxfitness.com", 6379, 1
        )
        self.testClass.connect()
        print("--------------test_set_key")
        test_field = {"test1": "test1", "test2": "test2"}
        self.testClass.set_key("test_key", test_field)
