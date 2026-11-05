import importlib.util
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('brady',ROOT/'src/tom_brady_analise.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class HistoricalContract(unittest.TestCase):
 def setUp(self):self.record=json.loads((ROOT/'data/career_summary.json').read_text())
 def test_source_snapshot(self):
  r=m.analyze(self.record);self.assertEqual(r['career_seasons'],23);self.assertEqual(r['super_bowl_appearances'],10);self.assertAlmostEqual(r['win_share_of_super_bowl_appearances'],.7)
 def test_inconsistent_wins_rejected(self):
  self.record['super_bowl_wins']=11
  with self.assertRaises(ValueError):m.analyze(self.record)
 def test_no_appearances_is_not_zero_conversion(self):
  self.record.update(super_bowl_wins=0,super_bowl_appearances=0);self.assertIsNone(m.analyze(self.record)['win_share_of_super_bowl_appearances'])
if __name__=='__main__':unittest.main()
