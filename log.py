from src.masonite.logging.channels import TerminalChannel

logger = TerminalChannel()
print(logger.debug('This is a message'))