"""Regenerate controlled OpsPilot synthetic workbooks reproducibly."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.synthetic.data_fit import generate_data_fit_packs
from src.synthetic.generate import generate_demo_workbooks, generate_quality_issue_workbooks


if __name__ == "__main__":
    output_directory = PROJECT_ROOT / "data" / "synthetic"
    created = generate_demo_workbooks(output_directory)
    created.update(generate_quality_issue_workbooks(output_directory))
    for name, path in created.items():
        print(f"{name}: {path}")
    data_fit_directory = output_directory / "data-fit"
    generate_data_fit_packs(data_fit_directory)
    print(f"data_fit_packs: {data_fit_directory}")
