import unittest
from typing import Tuple, List

def lcs(s1: str, s2: str) -> Tuple[int, List[str]]:
    return 0, []

class TestLCS(unittest.TestCase):
    
    _a: str = "ABCBDAB"
    _b: str = "BDCABA" 
    _subsequences: List[str] = [
        "BDAB",
        "BCAB",
        "BCBA"
    ]
    
    def test_length(self):
        length, subs = lcs(self._a, self._b)
        self.assertEqual( length, 4 )
        self.assertCountEqual( len(subs), len(self._subsequences) )
        for sub in subs:
            self.assertIn( sub, self._subsequences )

if __name__ == "__main__":
    unittest.main()