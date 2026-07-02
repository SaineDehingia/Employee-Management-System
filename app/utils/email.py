import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def send_leave_email(leave):

    logger.info("=" * 50)
    logger.info("EMAIL NOTIFICATION")
    logger.info("=" * 50)

    logger.info(f"Employee ID : {leave.employee_id}")
    logger.info(f"Leave Type  : {leave.leave_type}")
    logger.info(f"From Date   : {leave.from_date}")
    logger.info(f"To Date     : {leave.to_date}")
    logger.info(f"Reason      : {leave.reason}")
    logger.info(f"Status      : {leave.status}")

    logger.info("=" * 50)
    logger.info("Email notification simulated successfully.")
    logger.info("=" * 50)