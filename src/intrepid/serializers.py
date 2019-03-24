# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .model import *

class NoteSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Note
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'notes',
                   'noted' )


class ResourceSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Resource
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'definition', 'url', 'upload', 'parent', 'resources',
                   'notes', 'attached_to' )


class ProductSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Product
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'definition', 'url', 'parent', 'products', 'notes',
                   'attached_to' )


class GoalSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Goal
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'status',
                   'follows', 'precedes', 'notes' )


class ObjectiveSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Objective
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'status',
                   'precedes', 'follows', 'goal', 'satisfies', 'notes' )


class TargetSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Target
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'status',
                   'objective', 'satisfies', 'requires', 'releases', 'noets' )


class StrategySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Strategy
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'objective', 'notes' )


class PlanSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Plan
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'strategy', 'notes' )


class PhaseSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Phase
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'plan',
                   'notes' )


class StepSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Step
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'phase',
                   'notes' )


class ProjectSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Project
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'objective', 'satisfies', 'strategies', 'targets', 'notes' )


class TaskSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Task
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'parent',
                   'subtasks', 'project', 'step', 'notes' )


class ActionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Action
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'follows',
                   'precedes', 'task', 'notes' )


class CurrencySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Currency
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'rate',
                   'notes' )


class AccountSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Account
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'opened', 'closed', 'currency', 'allotments', 'notes' )


class PoolSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Pool
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'size',
                   'available', 'parent', 'partitions', 'accounts',
                   'allotments', 'notes' )


class AllotmentSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Allotment
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'account', 'pool', 'notes' )


class AllocationSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Allocation
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'opened',
                   'used', 'closed', 'size', 'available', 'pool', 'notes' )


class IncomeSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Income
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'stable',
                   'amount', 'sources', 'notes' )


class ExpenseSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Expense
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'stable',
                   'amount', 'source', 'notes', 'destinations' )

# class ExternalSerializer( serializers.HyperlinkedModelSerializer ):
#     class Meta:
#         model = External
#         fields = ()

# class SinkSerializer( serializers.HyperlinkedModelSerializer ):
#     class Meta:
#         model = Sink
#         fields = ( 'cost', 'expense', 'notes' )


class AssetSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Asset
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'cost',
                   'expense', 'value', 'intended_own', 'actual_own', 'notes' )


class DonationSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Donation
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'cost',
                   'expense', 'notes' )


class ServiceSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Service
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'cost',
                   'expense', 'intended', 'effective', 'notes' )


class RentalSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Rental
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'cost',
                   'expense', 'period', 'notes' )


class SourceSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Source
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'notes' )


class LiabilitySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Liability
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'value', 'notes' )


class ContributionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Contribution
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'notes' )


class CommissionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Commission
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'intended_close', 'effective_close', 'notes' )


class EmploymentSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Employment
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'period', 'notes' )


class InvestmentSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Investment
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'gain',
                   'destination', 'notes' )


class ReceiptSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Receipt
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'intended', 'effective', 'income', 'source', 'destinations',
                   'deposits', 'notes' )


class DepositSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Deposit
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'account', 'receipt', 'notes' )


class PaymentSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Payment
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'intended', 'effective', 'expense', 'destination', 'notes' )


class BudgetSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Budget
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'start',
                   'end', 'master', 'parts', 'follows', 'precedes', 'notes' )


class LineSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Line
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'amount',
                   'intended', 'effective', 'budget', 'notes' )


class TransferSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Transfer
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'source',
                   'destination', 'notes' )


class RelocationSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Relocation
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'source',
                   'destination', 'notes' )


class EarningSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Earning
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'receipt',
                   'notes' )


class PurchaseSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Purchase
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'payment',
                   'notes' )


class TeamSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Team
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'parent',
                   'groups', 'notes' )


class PositionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Position
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'team',
                   'notes' )


class RoleSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Role
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'positions', 'notes' )


class ResponsibilitySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Responsibility
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'roles',
                   'notes' )


class CapacitySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Capacity
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'roles',
                   'notes' )


class UserSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = User
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'positions', 'notes' )


class TaxonomySerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Taxonomy
        fields = ( 'name', 'title', 'description', 'active', 'valid',
                   'hierarhichal', 'exclusive', 'parent', 'children', 'notes' )


class TermSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Term
        fields = ( 'name', 'title', 'description', 'active', 'valid', 'parent',
                   'children', 'data', 'notes' )
