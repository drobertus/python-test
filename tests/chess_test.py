import requests
import unittest
import json
import yaml

class TestChess(unittest.TestCase):
    """Test case file for the chess API"""

    chess_url = 'http://chesstest.solidfire.net:8080/json-rpc'

    defaultStartPosition = [{"loc": "a8", "type": "r"}, {"loc": "b8", "type": "n"},
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
            "type": "P"}, {"loc": "e1", "type": "K"}, {"loc": "h2", "type": "P"}]

    def setUp(self):
        pass
    
    # Test case- two knights able to move to the same location
    # the syntax has no capacity to distinguish the moves
    def test_start_valid(self): 
        """Make a valid move from the start configuration"""
        theresp = requests.post(self.__class__.chess_url, json={
            "method": "MakeMove",
            "params": {
            "boardState": self.__class__.defaultStartPosition,
            "move": "Nc3",
            "playerState": "w"
            },
            "id": 1,
            "jsonrpc": "2.0"
            })
        print(theresp.status_code)
        self.assertEqual(theresp.status_code, 200)
        response = json.loads(theresp.text)
        
        expectedResp = {"id":1,"result": {"playerState": "b", "gameState": "",
            "boardState":[{"loc":"a1","type":"R"},{"loc":"c1","type":"B"},
            {"loc":"d1","type":"Q"},{"loc":"e1","type":"K"},{"loc":"f1","type":"B"},
            {"loc":"g1","type":"N"},{"loc":"h1","type":"R"},{"loc":"a2","type":"P"},
            {"loc":"b2","type":"P"},{"loc":"c2","type":"P"},{"loc":"d2","type":"P"},
            {"loc":"e2","type":"P"},{"loc":"f2","type":"P"},{"loc":"g2","type":"P"},
            {"loc":"h2","type":"P"},{"loc":"c3","type":"N"},{"loc":"a7","type":"p"},
            {"loc":"b7","type":"p"},{"loc":"c7","type":"p"},{"loc":"d7","type":"p"},
            {"loc":"e7","type":"p"},{"loc":"f7","type":"p"},{"loc":"g7","type":"p"},
            {"loc":"h7","type":"p"},{"loc":"a8","type":"r"},{"loc":"b8","type":"n"},
            {"loc":"c8","type":"b"},{"loc":"d8","type":"q"},{"loc":"e8","type":"k"},
            {"loc":"f8","type":"b"},{"loc":"g8","type":"n"},{"loc":"h8","type":"r"}]}}

        self.assertDictEqual(response, expectedResp)

    def test_start_invalid(self): 
        """Make an invalid move from the start configuration"""    
        theresp = requests.post(self.__class__.chess_url, json={
            "method": "MakeMove",
            "params": {
            "boardState": self.__class__.defaultStartPosition,
            "move": "Nc5",
            "playerState": "w"
            },
            "id": 1,
            "jsonrpc": "2.0"
            })

        self.assertEqual(theresp.status_code, 200)
        response = yaml.safe_load(theresp.text) # json.loads(theresp.text)
        self.assertDictContainsSubset({"id":1, "error":{"message":"Move cannot be made.", "code":-32020, 
            "data":"Nc5"}}, response)

    def test_ambigious_move(self):
        """Make a move from a position in which the moved piece is ambigiuous"""
        ambiguousStartPosition = []
        theresp = requests.post(self.__class__.chess_url, json={
            "method": "MakeMove",
            "params": {
            "boardState": self.__class__.ambiguousStartPosition,
            "move": "Nc5",
            "playerState": "w"
            },
            "id": 1,
            "jsonrpc": "2.0"
            })


if __name__ == '__main__':
    unittest.main()