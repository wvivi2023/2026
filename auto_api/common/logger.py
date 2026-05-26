import logging
import os
from datetime import datetime

# 日志目录
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_file = os.path.join(log_dir, f"run_{datetime.now().strftime('%Y%m%d%H%M%S')}.log")

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)