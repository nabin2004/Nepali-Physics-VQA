from llmops.logging.logger import logging
from llmops.exception.exception import LLMOpsException
import sys 

try:
    logging.info("Fine-tuning started")
    logging.warning("Dataset size is small, results may vary")

    # Error simulation
    1 / 0

except Exception as e:
    logging.error("Training failed due to GPU OOM or other error")
    raise LLMOpsException(e, sys)