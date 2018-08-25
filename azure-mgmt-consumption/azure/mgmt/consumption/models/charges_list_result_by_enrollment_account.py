# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargesListResultByEnrollmentAccount(Model):
    """Result of listing charge summary by enrollment account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of charge summary by enrollment account.
    :vartype value:
     list[~azure.mgmt.consumption.models.ChargeSummaryByEnrollmentAccount]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ChargeSummaryByEnrollmentAccount]'},
    }

    def __init__(self, **kwargs):
        super(ChargesListResultByEnrollmentAccount, self).__init__(**kwargs)
        self.value = None
