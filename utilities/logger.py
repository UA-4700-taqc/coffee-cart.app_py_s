"""Logger utility module for test automation project.

This module provides a comprehensive logging solution for test automation,
supporting all Python logging levels with auto-detection capabilities.
"""

import inspect
import logging


class Logger:
    """Simple logger class for test automation project.

    Supports all Python logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    """

    def __init__(self, name=None, console_level=logging.INFO, file_level=logging.DEBUG):
        """Initialize logger with optional name and configurable log levels.

        Args:
            name (str, optional): Logger name. If None, uses calling module name.
            console_level (int): Minimum level for console output (default: INFO)
            file_level (int): Minimum level for file output (default: DEBUG)
        """
        if name is None:
            # Auto-detect calling module name for better traceability
            frame = inspect.currentframe().f_back
            caller_module = frame.f_globals.get("__name__", "test_automation")
            self.logger_name = caller_module
        else:
            self.logger_name = name

        self.console_level = console_level
        self.file_level = file_level
        self._logger = None

    def get_logger(self):
        """Get configured logger instance with all logging levels available.

        Returns:
            logging.Logger: Configured logger supporting all levels
        """
        if self._logger is None:
            self._logger = self._setup_logger()
        return self._logger

    def _setup_logger(self):
        """Set up and configure the logger with console handler.

        Optimized to prevent duplicate handlers for performance.
        """
        # Create logger with the detected or provided name
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)  # Set to lowest level to capture all messages

        # Avoid duplicate handlers for performance and clean logs
        if logger.handlers:
            return logger

        # Create and configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.console_level)

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
        return self.get_logger().debug(message)

    def info(self, message):
        """Log info message for general operational information."""
        return self.get_logger().info(message)

    def warning(self, message):
        """Log warning message for potential issues that don't stop execution."""
        return self.get_logger().warning(message)

    def error(self, message):
        """Log error message for serious problems that affected execution."""
        return self.get_logger().error(message)

    def critical(self, message):
        """Log critical message for very serious errors that may abort execution."""
        return self.get_logger().critical(message)


def get_logger(name=None, console_level=logging.INFO):
    """Get a logger instance quickly with auto-detection.

    Args:
        name (str, optional): Logger name. If None, uses calling module name.
        console_level (int): Minimum level for console output

    Returns:
        logging.Logger: Configured logger instance with all levels available
    """
    if name is None:
        # Auto-detect calling module for better maintainability
        frame = inspect.currentframe().f_back
        caller_module = frame.f_globals.get("__name__", "test_automation")
        name = caller_module

    logger_instance = Logger(name, console_level)
    return logger_instance.get_logger()
