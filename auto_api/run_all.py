import os
import pytest
from datetime import datetime

if __name__ == "__main__":
    report_path = os.path.join("reports", f"api_report_{datetime.now().strftime('%Y%m%d%H%M%S')}.html")
    pytest.main([
        "./testcases/",
        "-v",
        "-s",
        f"--html={report_path}",
        "--self-contained-html"
    ])