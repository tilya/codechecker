# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------
"""
Result handler for Clang Static Analyzer.
"""


from codechecker_common.logger import get_logger
from codechecker_report_hash.hash import HashType, replace_report_hash

from ..result_handler_base import ResultHandler

LOG = get_logger('report')


class ResultHandlerClangSA(ResultHandler):
    """
    Use context free hash if enabled.
    """

    def postprocess_result(self):
        """
        Override the context sensitive issue hash in the plist files to
        context insensitive if it is enabled during analysis.
        """
        if self.report_hash_type in ['context-free', 'context-free-v2']:
            replace_report_hash(self.analyzer_result_file,
                                HashType.CONTEXT_FREE)
