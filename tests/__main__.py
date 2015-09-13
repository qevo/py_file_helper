"""Command line package entry point"""

from sys import argv
from SuiteHandler import SuiteHandler
import manage, operation


if __name__ == "__main__":
    try:
        mod_name  = argv[1]
    except:
        mod_name = "_"

    sh = SuiteHandler({
        "manage": manage.suite,
        "operation": operation.suite
    })

    sh.run_suite(mod_name)
    print sh.result
    for f in sh.result.failures:
        for t in f:
            print t
        print ''
    for e in sh.result.errors:
        for t in e:
            print t
        print ''
