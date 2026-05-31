import unittest

from Main_tea import (
    Preferences,
    Sugar,
    Lemon,
    BlackTea,
    GreenTea,
    RedTea,
    TeaRecommender
)

#test of modifiers
class TestModifiers(unittest.TestCase):

    def test_sugar_bonus(self):
        sugar = Sugar(2)
        self.assertEqual(sugar.sweetness_bonus(), 3.0)

    def test_lemon_sourness_bonus(self):
        lemon = Lemon(2)
        self.assertEqual(lemon.sourness_bonus(), 4)

    def test_lemon_bitterness_reduction(self):
        lemon = Lemon(2)
        self.assertEqual(lemon.bitterness_reduction(), 1.0)

#test of brew method
class TestTeaMethods(unittest.TestCase):

    def test_brew_info_black(self):
        tea = BlackTea()
        self.assertEqual(tea.brew_info(), "95°C, 4 min")

    def test_brew_info_green(self):
        tea = GreenTea()
        self.assertEqual(tea.brew_info(), "80°C, 3 min")

#test of match method
class TestTeaMatch(unittest.TestCase):

    def test_match_returns_number(self):
        tea = BlackTea()

        prefs = Preferences(
            sweetness=5,
            sourness=5,
            bitterness=5,
            strength=5
        )

        score = tea.match(
            prefs,
            Sugar(1),
            Lemon(1)
        )

        self.assertIsInstance(score, float)

    def test_score_in_range(self):
        tea = RedTea()

        prefs = Preferences(
            sweetness=10,
            sourness=10,
            bitterness=10,
            strength=10
        )

        score = tea.match(
            prefs,
            Sugar(3),
            Lemon(2)
        )

        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 50)

#test of recommender
class TestRecommender(unittest.TestCase):

    def test_recommend_returns_valid_result(self):
        system = TeaRecommender()

        prefs = Preferences(
            sweetness=5,
            sourness=5,
            bitterness=5,
            strength=5
        )

        tea, score, sugar, lemon = system.recommend(prefs)

        self.assertIsNotNone(tea)
        self.assertIsInstance(score, float)
        self.assertIn(sugar, [0, 1, 2, 3])
        self.assertIn(lemon, [0, 1, 2])

    def test_recommended_tea_type(self):
        system = TeaRecommender()

        prefs = Preferences(
            sweetness=1,
            sourness=1,
            bitterness=10,
            strength=10
        )

        tea, score, sugar, lemon = system.recommend(prefs)

        self.assertIn(
            tea.__class__.__name__,
            ["BlackTea", "GreenTea", "RedTea"]
        )


if __name__ == "__main__":
    unittest.main()