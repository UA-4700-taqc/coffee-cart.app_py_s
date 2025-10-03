"""Logger utility module for test automation project.

This module provides a comprehensive logging solution for test automation,
supporting all Python logging levels with auto-detection capabilities.
"""

import logging


class Logger:
    """Simple logger class for test automation project.

    Supports all Python logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    """

    @classmethod
    def get_logger(cls, name=None, console_level=logging.INFO):
        """Get configured logger instance with all logging levels available.

        Args:
            name (str, optional): Logger name. If None, uses calling module name.
            console_level (int): Minimum level for console output (default: INFO)

        Returns:
            logging.Logger: Configured logger supporting all levels
        """
        # Create logger with the provided name
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)  # Set to lowest level to capture all messages

        # Avoid duplicate handlers for performance and clean logs
        if logger.handlers:
            return logger

        # Create and configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)

        # Create detailed formatter for better readability
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
        )
        console_handler.setFormatter(console_formatter)

        # Add console handler to logger
        logger.addHandler(console_handler)

        return logger

    # Convenience methods for each log level - following best practices
    def debug(self, message):
        """Log debug message for detailed troubleshooting information."""
        self.get_logger().debug(message)

    def info(self, message):
        """Log info message for general operational information."""
        self.get_logger().info(message)

    def warning(self, message):
        """Log warning message for potential issues that don't stop execution."""
        self.get_logger().warning(message)

    def error(self, message):
        """Log error message for serious problems that affected execution."""
        self.get_logger().error(message)

    def critical(self, message):
        """Log critical message for very serious errors that may abort execution."""
        self.get_logger().critical(message)
