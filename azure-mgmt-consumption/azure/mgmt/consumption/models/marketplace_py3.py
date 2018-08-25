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

from .resource_py3 import Resource


class Marketplace(Resource):
    """An marketplace resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar billing_period_id: The id of the billing period resource that the
     usage belongs to.
    :vartype billing_period_id: str
    :ivar usage_start: The start of the date time range covered by the usage
     detail.
    :vartype usage_start: datetime
    :ivar usage_end: The end of the date time range covered by the usage
     detail.
    :vartype usage_end: datetime
    :ivar resource_rate: The marketplace resource rate.
    :vartype resource_rate: decimal.Decimal
    :ivar offer_name: The type of offer.
    :vartype offer_name: str
    :ivar resource_group: The name of resource group.
    :vartype resource_group: str
    :ivar order_number: The order number.
    :vartype order_number: str
    :ivar instance_name: The name of the resource instance that the usage is
     about.
    :vartype instance_name: str
    :ivar instance_id: The uri of the resource instance that the usage is
     about.
    :vartype instance_id: str
    :ivar currency: The ISO currency in which the meter is charged, for
     example, USD.
    :vartype currency: str
    :ivar consumed_quantity: The quantity of usage.
    :vartype consumed_quantity: decimal.Decimal
    :ivar unit_of_measure: The unit of measure.
    :vartype unit_of_measure: str
    :ivar pretax_cost: The amount of cost before tax.
    :vartype pretax_cost: decimal.Decimal
    :ivar is_estimated: The estimated usage is subject to change.
    :vartype is_estimated: bool
    :ivar meter_id: The meter id (GUID).
    :vartype meter_id: str
    :ivar subscription_guid: Subscription guid.
    :vartype subscription_guid: str
    :ivar subscription_name: Subscription name.
    :vartype subscription_name: str
    :ivar account_name: Account name.
    :vartype account_name: str
    :ivar department_name: Department name.
    :vartype department_name: str
    :ivar consumed_service: Consumed service name.
    :vartype consumed_service: str
    :ivar cost_center: The cost center of this department if it is a
     department and a costcenter exists
    :vartype cost_center: str
    :ivar additional_properties: Additional details of this usage item. By
     default this is not populated, unless it's specified in $expand.
    :vartype additional_properties: str
    :ivar publisher_name: The name of publisher.
    :vartype publisher_name: str
    :ivar plan_name: The name of plan.
    :vartype plan_name: str
    :ivar additional_info: Additional info of this usage item.
    :vartype additional_info: str
    :ivar is_recurring_charge:
    :vartype is_recurring_charge: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'billing_period_id': {'readonly': True},
        'usage_start': {'readonly': True},
        'usage_end': {'readonly': True},
        'resource_rate': {'readonly': True},
        'offer_name': {'readonly': True},
        'resource_group': {'readonly': True},
        'order_number': {'readonly': True},
        'instance_name': {'readonly': True},
        'instance_id': {'readonly': True},
        'currency': {'readonly': True},
        'consumed_quantity': {'readonly': True},
        'unit_of_measure': {'readonly': True},
        'pretax_cost': {'readonly': True},
        'is_estimated': {'readonly': True},
        'meter_id': {'readonly': True},
        'subscription_guid': {'readonly': True},
        'subscription_name': {'readonly': True},
        'account_name': {'readonly': True},
        'department_name': {'readonly': True},
        'consumed_service': {'readonly': True},
        'cost_center': {'readonly': True},
        'additional_properties': {'readonly': True},
        'publisher_name': {'readonly': True},
        'plan_name': {'readonly': True},
        'additional_info': {'readonly': True},
        'is_recurring_charge': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_period_id': {'key': 'properties.billingPeriodId', 'type': 'str'},
        'usage_start': {'key': 'properties.usageStart', 'type': 'iso-8601'},
        'usage_end': {'key': 'properties.usageEnd', 'type': 'iso-8601'},
        'resource_rate': {'key': 'properties.resourceRate', 'type': 'decimal'},
        'offer_name': {'key': 'properties.offerName', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'order_number': {'key': 'properties.orderNumber', 'type': 'str'},
        'instance_name': {'key': 'properties.instanceName', 'type': 'str'},
        'instance_id': {'key': 'properties.instanceId', 'type': 'str'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
        'consumed_quantity': {'key': 'properties.consumedQuantity', 'type': 'decimal'},
        'unit_of_measure': {'key': 'properties.unitOfMeasure', 'type': 'str'},
        'pretax_cost': {'key': 'properties.pretaxCost', 'type': 'decimal'},
        'is_estimated': {'key': 'properties.isEstimated', 'type': 'bool'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'subscription_guid': {'key': 'properties.subscriptionGuid', 'type': 'str'},
        'subscription_name': {'key': 'properties.subscriptionName', 'type': 'str'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'department_name': {'key': 'properties.departmentName', 'type': 'str'},
        'consumed_service': {'key': 'properties.consumedService', 'type': 'str'},
        'cost_center': {'key': 'properties.costCenter', 'type': 'str'},
        'additional_properties': {'key': 'properties.additionalProperties', 'type': 'str'},
        'publisher_name': {'key': 'properties.publisherName', 'type': 'str'},
        'plan_name': {'key': 'properties.planName', 'type': 'str'},
        'additional_info': {'key': 'properties.additionalInfo', 'type': 'str'},
        'is_recurring_charge': {'key': 'properties.isRecurringCharge', 'type': 'bool'},
    }

    def __init__(self, **kwargs) -> None:
        super(Marketplace, self).__init__(**kwargs)
        self.billing_period_id = None
        self.usage_start = None
        self.usage_end = None
        self.resource_rate = None
        self.offer_name = None
        self.resource_group = None
        self.order_number = None
        self.instance_name = None
        self.instance_id = None
        self.currency = None
        self.consumed_quantity = None
        self.unit_of_measure = None
        self.pretax_cost = None
        self.is_estimated = None
        self.meter_id = None
        self.subscription_guid = None
        self.subscription_name = None
        self.account_name = None
        self.department_name = None
        self.consumed_service = None
        self.cost_center = None
        self.additional_properties = None
        self.publisher_name = None
        self.plan_name = None
        self.additional_info = None
        self.is_recurring_charge = None
