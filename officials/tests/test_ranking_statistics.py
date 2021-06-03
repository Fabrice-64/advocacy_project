from django.test import TestCase
import officials.ranking_statistics as rs
from .database_sample import ranking_sample


class RankingStatisticsTest(TestCase):

    def setUp(self):
        self.officials_statistics = rs.GetStatsFromOfficials(ranking_sample)

    def test_officials_statistics(self):
        officials_statistics = self.officials_statistics.get_stats_from_officials()
        self.assertEqual(len(officials_statistics), 3)
        self.assertEqual(
            officials_statistics['propinquity']['count'], 20)

    def test_get_quantiles_from_officials(self):
        officials_quantiles = self.officials_statistics.get_quantiles_from_officials()
        self.assertEqual(officials_quantiles['propinquity'][0.5], 6.15)

    def test_get_officials_below_P50_I50(self):
        officials_below_50_50 = self.officials_statistics.get_officials_below_P50_I50()
        self.assertEqual(len(officials_below_50_50), 3)

    def test_get_officials_below_P50_above_I50(self):
        officials_sample = self.officials_statistics.get_officials_below_P50_above_I50()
        self.assertEqual(len(officials_sample), 7)

    def test_get_officials_above_P50_below_I50(self):
        officials_sample = self.officials_statistics.get_officials_above_P50_below_I50()
        self.assertEqual(len(officials_sample), 6)

    def test_get_officials_above_P50_above_I50(self):
        officials_sample = self.officials_statistics.get_officials_above_P50_above_I50()
        self.assertEqual(len(officials_sample), 4)

    def test_get_influence_targets(self):
        officials_sample = self.officials_statistics.get_influence_targets()
        self.assertIsNotNone(officials_sample)
