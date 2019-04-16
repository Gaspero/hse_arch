# -*- coding: utf-8 -*-

import os
from behave import fixture, use_fixture

from hse_arch import create_app
from config import TestingConfig

@fixture
def flaskr_client(context, *args, **kwargs):
    context.client = create_app(TestingConfig)

    # with APP.app_context():
    #     DB = Database(APP)
    #     init_models(DB)
    #     # pass
    yield context.client

    # -- CLEANUP:
    # os.close(context.db)
    # os.unlink(APP.config['DATABASE'])


def before_feature(context, feature):
    # -- HINT: Recreate a new flask client before each feature is executed.
    context.config.setup_logging()
    use_fixture(flaskr_client, context)
