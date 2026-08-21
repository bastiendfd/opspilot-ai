import subprocess
import sys
from pathlib import Path


def test_synthetic_generation_script_runs_from_repository_root() -> None:
    repository_root = Path(__file__).resolve().parents[1]

    completed = subprocess.run(
        [sys.executable, "scripts/generate_synthetic_data.py"],
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert "actual:" in completed.stdout
    assert "data_fit_packs:" in completed.stdout
    assert (repository_root / "data" / "synthetic" / "Actual.xlsx").exists()
    assert (repository_root / "data" / "synthetic" / "data-fit" / "echo" / "mapping.json").exists()
