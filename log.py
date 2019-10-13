from src.masonite.logging.channels import StackChannel

logger = StackChannel()
print(logger.notice('This is a message'))