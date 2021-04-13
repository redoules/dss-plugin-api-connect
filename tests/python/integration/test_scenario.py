from dku_plugin_test_utils import dss_scenario

TEST_PROJECT_KEY = "PLUGINTESTAPICONNECT"


def test_run_api_connect_authentication_modes(user_dss_clients):
    dss_scenario.run(user_dss_clients, project_key=TEST_PROJECT_KEY, scenario_id="AuthenticationModes")


def test_run_api_connect_pagination_modes(user_dss_clients):
    dss_scenario.run(user_dss_clients, project_key=TEST_PROJECT_KEY, scenario_id="PAGINATION")