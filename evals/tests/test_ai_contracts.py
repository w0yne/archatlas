"""Targeted scenario-contract regressions, not live-agent quality measurements."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
sys.path.insert(0, str(ROOT / 'evals'))
import build_selection
import run_eval
from scenario_samples import load_manifest, SCENARIO


class AIContractRegression(unittest.TestCase):
    def test_s6_s11_s12_keep_explicit_security_and_deployment_choices(self):
        scenarios = run_eval.load_scenarios()
        catalog, tree = build_selection.load()
        rows = {r['code']: r for r in catalog['types']}
        for scenario in ('S6', 'S11', 'S12'):
            self.assertTrue(set(scenarios[scenario]['expected_types']) <= rows.keys())
        self.assertEqual(rows['F1']['target']['code'], 'E1')
        self.assertEqual(rows['F2']['target']['code'], 'D2')
        self.assertEqual(rows['G2']['target']['code'], 'G1')
        security = {c for leaf in build_selection.reader_tree(catalog, tree)['root']['security'] for c in leaf['types']}
        self.assertTrue({'F1', 'F2', 'F3', 'G3'} <= security)
        self.assertIn('不支持', scenarios['S12']['prompt'])

    def test_ingestion_and_permission_contracts_agree_across_views(self):
        facts = json.loads((SCENARIO / 'scenario.json').read_text())
        manifest = load_manifest()
        self.assertEqual(len(manifest['views']), 29)
        self.assertEqual(facts['assumptions']['AS-ingest']['details']['producer'], 'C-api')
        self.assertEqual(facts['assumptions']['AS-policy']['details']['roleMatrix']['R-operator'][:4], ['D'] * 4)
        for lang in ('en', 'zh'):
            for view, edge in [('C3', 'CON-17'), ('C6', 'I-10')]:
                model = json.loads((SCENARIO / f'views/{view}/{lang}/diagram.json').read_text())
                producer = next(e for e in model['edges'] if e['id'] == edge)
                self.assertEqual((producer['from'], producer['to']), ('C-api', 'Q-ingest'))
            model = json.loads((SCENARIO / f'views/E3/{lang}/diagram.json').read_text())
            self.assertFalse(any(e['from'] == 'E3-unapproved' and e['to'] == 'E3-executing' for e in model['edges']))
            self.assertFalse(any(e['from'] == 'E3-unknown' and e['to'] == 'E3-final' for e in model['edges']))
            auth = json.loads((SCENARIO / f'views/F1/{lang}/diagram.json').read_text())
            request = next(e for e in auth['edges'] if e['id'] == 'AUTH-1')
            branch = next(f for f in auth['frames'] if f['id'] == 'exchange')
            self.assertLess(request['step'], branch['from_step'])


if __name__ == '__main__':
    unittest.main()
