from src.masonite.logging.channels import SlackChannel

logger = SlackChannel()
print(logger.debug('This is a message'))