import requests
import json
import unittest

class TestChess(unittest.TestCase):
    """Test case file for the chess API"""

    chess_url = 'http://chesstest.solidfire.net:8080/json-rpc'

    def setUp(self):
        pass
    
    # Test case- two knights able to move to the same location
    # the syntax has no capacity to distinguish the moves
    def test_start_valid(self): 
        """Make a vlid move from the start configuration"""
        theresp = requests.post(self.__class__.chess_url, data={
            "method": "MakeMove",
            "params": {
            "boardState": [{"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"},
            {"loc": "c8", "type": "b"}, {"loc": "d8", "type": "q"}, {"loc": "e8", "type":
            "k"}, {"loc": "f8", "type": "b"}, {"loc": "g8", "type": "n"}, {"loc": "h8",
            "type": "r"}, {"loc": "a7", "type": "p"}, {"loc": "b7", "type": "p"}, {"loc":
            "c7", "type": "p"}, {"loc": "d7", "type": "p"}, {"loc": "e7", "type": "p"},
            {"loc": "f7", "type": "p"}, {"loc": "g7", "type": "p"}, {"loc": "h7", "type":
            "p"}, {"loc": "a1", "type": "R"}, {"loc": "b1", "type": "N"}, {"loc": "c1",
            "type": "B"}, {"loc": "d1", "type": "Q"}, {"loc": "f1", "type": "B"}, {"loc":
            "g1", "type": "N"}, {"loc": "h1", "type": "R"}, {"loc": "a2", "type": "P"},
            {"loc": "b2", "type": "P"}, {"loc": "c2", "type": "P"}, {"loc": "d2", "type":
            "P"}, {"loc": "e2", "type": "P"}, {"loc": "f2", "type": "P"}, {"loc": "g2",
            "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}],
            "move": "Nc3",
            "playerState": "w"
            },
            "id": 1,
            "jsonrpc": "2.0"
            })
        print(theresp.status_code)
        self.assertEqual(theresp.status_code, 200)


if __name__ == '__main__':
    unittest.main()