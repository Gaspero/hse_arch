# -*- coding: utf-8 -*-

from behave import fixture, use_fixture

from hse_arch import create_app

@fixture
def flaskr_client(context, *args, **kwargs):
    context.client = create_app('testing')
    yield context.client


def before_feature(context, feature):
    # -- HINT: Recreate a new flask client before each feature is executed.
    context.config.setup_logging()
    use_fixture(flaskr_client, context)
