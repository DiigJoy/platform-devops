import logging
import sys

import structlog

DEFAULT_LOG_LEVEL = "INFO"


def configure_logging(service_name: str, env: str, level: str | None = None) -> None:
    level_name = (level or DEFAULT_LOG_LEVEL).upper()
    level_value = getattr(logging, level_name, logging.INFO)

    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=level_value)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level_value),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

    structlog.contextvars.bind_contextvars(service=service_name, env=env)
