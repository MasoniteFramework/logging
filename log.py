from src.masonite.logging.channels import DailyChannel

logger = DailyChannel()
print(logger.debug('This is a message'))