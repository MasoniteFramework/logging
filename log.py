from src.masonite.logging.channels import StackChannel

logger = StackChannel()
logger.notice('This is a message')