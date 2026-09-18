import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app as app_module


def test_github_skills_activity_exists():
    assert "GitHub Skills" in app_module.activities


def test_github_skills_activity_has_capacity_and_schedule():
    activity = app_module.activities["GitHub Skills"]

    assert activity["description"]
    assert activity["schedule"]
    assert activity["max_participants"] > 0
    assert isinstance(activity["participants"], list)
