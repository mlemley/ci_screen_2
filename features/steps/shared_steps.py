from behave import *

import features.support.helpers as helpers
import features.support.fake_ci_server as ci
import features.support.config_helper as config_helper

@given(u'I have a CI server with projects')
def i_have_a_ci_server_with_projects(context):
    port = helpers.get_port()
    ci_server = ci.FakeCIServer(port=port)
    ci_server.start()
    for row in context.table:
        ci_server.projects.append(row)
    context.fake_ci_servers.append(ci_server)

    helpers.rebuild_config_file(context)

@given(u'the app is running')
def the_app_is_running(context):
    helpers.launch_ci_screen(context)
