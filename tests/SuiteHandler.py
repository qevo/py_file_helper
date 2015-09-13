import unittest


class SuiteHandler(object):
    """unittest.TestSuite handler"""

    def __init__(self, mod_suites):

        self.mod_suites = mod_suites
        self.mod_suites["_"] = self.combine_suites()
        self.result = unittest.result.TestResult()


    def run_suite(self, name="_", result=None):
        """Run a test suite by name

        Args:
            name (str): (optional) Name of the test suite. Defaults to combined suite.
            result (unittest.TestResult): (optional) Test result holder. Defaults to None, which uses an internal object.

        """
        result = result if result else self.result
        self.mod_suites[name].run(result)


    def get_suite(self, name="_"):
        """Retrieve a test suite by name

        Args:
            name (str): (optional) Name of the test suite. Defaults to combined suite.

        Returns:
            unittest.TestSuite: Test suite comprised of other suites.

        """
        return self.mod_suites[name]


    def combine_suites(self, suites=None):
        """Combine test suites

        Args:
            suites (unittest.TestSuite): (optional) Test suites. Defaults to None, which uses an internal value.

        Returns:
            unittest.TestSuite: Test suite comprised of other suites.

        """
        suites = suites if suites else self.mod_suites.values()
        master_suite = unittest.TestSuite()
        master_suite.addTests(suites)
        return master_suite


    def get_names(self):
        """List the names of test suites in the handler"""

        return self.mod_suites.keys()


    def add_suite(self, name, suite):
        """Add a suite to the handler

        Args:
            name (str): (optional) Name of the test suite. Defaults to combined suite.
            suite (unittest.TestSuite): Test suite

        """
        self.mod_suites[name] = suite
