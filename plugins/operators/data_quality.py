from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 checks=[],
                 ignore_fails=True,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.checks = checks
        self.ignore_fails = ignore_fails

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        for check in self.checks:
            sql = check.get("check_sql")
            exp_result = check.get("expected_result")
            self.log.info(
                "Checking: " + "(" + str(sql) + ")" + " is equal " + str(exp_result))
            records = redshift.get_records(sql)[0]
            if records[0] == exp_result:
                self.log.info("Check passed")
            elif not self.ignore_fails and records[0] != exp_result:
                ValueError("Data Quality Check failed.")
            else:
                self.log.info("Check failed")
        self.log.info("Checking Data Quality Done!")