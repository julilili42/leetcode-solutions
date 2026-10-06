import unittest
from unittest.mock import patch

import update_readme_stats as stats


class LookupTest(unittest.TestCase):
    def test_lookup_names_and_search_fallback(self):
        for folder, slug in {
            "coin_change_2": "coin-change-ii",
            "move_zeroes": "move-zeroes",
            "jump_game_II": "jump-game-ii",
            "some_problem_2": "some-problem-ii",
            "search_a_2d_matrix": "search-a-2d-matrix",
            **stats.SLUG_ALIASES,
        }.items():
            with self.subTest(folder=folder):
                self.assertEqual(stats.folder_to_slug(folder), slug)
                question = {"titleSlug": slug, "difficulty": "Medium"}
                with patch.object(stats, "leetcode_graphql", return_value={
                    "data": {"question": question},
                }) as graphql:
                    self.assertEqual(stats.fetch_problem(folder), question)
                    self.assertEqual(graphql.call_args.args[1], {"titleSlug": slug})

                with patch.object(stats, "leetcode_graphql", side_effect=[
                    {"data": {"question": None}},
                    {"data": {"problemsetQuestionList": {"questions": [question]}}},
                ]) as graphql:
                    self.assertEqual(stats.fetch_problem(folder), question)
                    self.assertEqual(
                        graphql.call_args.args[1]["filters"]["searchKeywords"],
                        slug.replace("-", " "),
                    )


if __name__ == "__main__":
    unittest.main()
