"""
This module contains classes which abstract the process of checking an entry's
existence
"""

# Allow postponed evaluation of type annotations
from __future__ import annotations

import requests.models

from .entry_probing_request import ProbingRequest
from .entry_probing_response import ProbingResponse


class EntryProbing():
    """
    General wrapper for both a ProbingRequest and a ProbingResponse. The
    check_entry method uses these handlers to check if a given entry in a
    website has been hit or not
    """

    def __init__(self, req_handler: ProbingRequest):
        """
        Initializes the class with the request handler

        :param req_handler: Handler describing how to execute the request
        """
        if not isinstance(req_handler, ProbingRequest):
            raise TypeError("Request handler must be a subclass of " +
                            "ProbingRequest")

        self.__req_handler = req_handler
        self.__resp_handlers = []
        # Property where the generated response is stored
        self.__response_obj = None


    @property
    def response(self) -> Optional[requests.models.Response]:
        """
        Returns the requests.model.Response object generated by the request, if
        it was already done. Returns None if request wasn't executed yet.
        """
        return self.__response_obj


    def add_response_handler(self, resp_handler: ProbingResponse
                             ) -> EntryProbing:
        """
        Adds a response handler to the probing process

        :param resp_handler: Handler describing how to validate the response

        :returns: Entry probing object, to enable chaining
        """
        if not isinstance(resp_handler, ProbingResponse):
            raise TypeError("Response handler must be a subclass of " +
                            "ProbingResponse")

        self.__resp_handlers.append(resp_handler)
        return self


    def check_entry(self, entry: Optional[Any] = None) -> bool:
        """
        Uses the request and response handlers to check for an entry's existence

        :param entry: entry parameter to be used by the request, if necessary

        :returns: True if entry is valid, False otherwise
        """

        response = self.__req_handler.process(entry)
        self.__response_obj = response
        return all([h.process(response) for h in self.__resp_handlers])
