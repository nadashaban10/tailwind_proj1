from typing import LiteralString
from sympy.assumptions import Predicate
from sympy.multipledispatch import Dispatcher


class PrimePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...


class CompositePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...


class EvenPredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...


class OddPredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...
