from alembic.operations import MigrateOperation
from alembic.operations import Operations


class ReplaceableObject:
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


class ReversibleOp(MigrateOperation):
    def __init__(self, target):
        self.target = target

    @classmethod
    def invoke_for_target(cls, operations, target):
        op = cls(target)
        return operations.invoke(op)

    def reverse(self):
        raise NotImplementedError()

    @classmethod
    def _get_object_from_version(cls, operations, ident):
        version, objname = ident.split(".")

        module = operations.get_context().script.get_revision(version).module
        obj = getattr(module, objname)
        return obj

    @classmethod
    def replace(cls, operations, target, replaces=None, replace_with=None):

        if replaces:
            old_obj = cls._get_object_from_version(operations, replaces)
            drop_old = cls(old_obj).reverse()
            create_new = cls(target)
        elif replace_with:
            old_obj = cls._get_object_from_version(operations, replace_with)
            drop_old = cls(target).reverse()
            create_new = cls(old_obj)
        else:
            raise TypeError("replaces or replace_with is required")

        operations.invoke(drop_old)
        operations.invoke(create_new)


@Operations.register_operation("create_view", "invoke_for_target")
@Operations.register_operation("replace_view", "replace")
class CreateViewOp(ReversibleOp):
    def reverse(self):
        return DropViewOp(self.target)


@Operations.register_operation("drop_view", "invoke_for_target")
class DropViewOp(ReversibleOp):
    def reverse(self):
        return CreateViewOp(self.target)


@Operations.register_operation("create_function", "invoke_for_target")
@Operations.register_operation("replace_function", "replace")
class CreateFunctionOp(ReversibleOp):
    def reverse(self):
        return DropFunctionOp(self.target)


@Operations.register_operation("drop_function", "invoke_for_target")
class DropFunctionOp(ReversibleOp):
    def reverse(self):
        return CreateFunctionOp(self.target)


@Operations.register_operation("create_trigger", "invoke_for_target")
@Operations.register_operation("replace_trigger", "replace")
class CreateTriggerOp(ReversibleOp):
    def reverse(self):
        return DropTriggerOp(self.target)


@Operations.register_operation("drop_trigger", "invoke_for_target")
class DropTriggerOp(ReversibleOp):
    def reverse(self):
        return CreateTriggerOp(self.target)


@Operations.register_operation("create_sequence", "invoke_for_target")
@Operations.register_operation("replace_sequence", "replace")
class CreateSequenceOp(ReversibleOp):
    def reverse(self):
        return DropSequenceOp(self.target)


@Operations.register_operation("drop_sequence", "invoke_for_target")
class DropSequenceOp(ReversibleOp):
    def reverse(self):
        return CreateSequenceOp(self.target)


@Operations.implementation_for(CreateViewOp)
def create_view(operations, operation):
    operations.execute(
        "CREATE VIEW %s AS %s" % (operation.target.name, operation.target.sqltext)
    )


@Operations.implementation_for(DropViewOp)
def drop_view(operations, operation):
    operations.execute("DROP VIEW %s" % operation.target.name)


@Operations.implementation_for(CreateFunctionOp)
def create_function(operations, operation):
    operations.execute(
        "CREATE FUNCTION %s %s" % (operation.target.name, operation.target.sqltext)
    )


@Operations.implementation_for(DropFunctionOp)
def drop_function(operations, operation):
    operations.execute("DROP FUNCTION %s" % operation.target.name)


@Operations.implementation_for(CreateTriggerOp)
def create_trigger(operations, operation):
    operations.execute(
        "CREATE TRIGGER %s %s" % (operation.target.name, operation.target.sqltext)
    )


@Operations.implementation_for(DropTriggerOp)
def drop_trigger(operations, operation):
    operations.execute("DROP TRIGGER %s" % operation.target.name)


@Operations.implementation_for(CreateSequenceOp)
def create_sequence(operations, operation):
    operations.execute(
        "CREATE SEQUENCE %s %s" % (operation.target.name, operation.target.sqltext)
    )


@Operations.implementation_for(DropSequenceOp)
def drop_sequence(operations, operation):
    operations.execute("DROP SEQUENCE %s" % operation.target.name)
