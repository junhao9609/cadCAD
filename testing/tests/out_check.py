from pprint import pprint

import pandas as pd
from tabulate import tabulate
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

from testing.models import param_sweep
from cadCAD import configs

exec_mode = ExecutionMode()

single_proc_ctx = ExecutionContext(context=exec_mode.local_mode)
run = Executor(exec_context=single_proc_ctx, configs=configs)

raw_result, tensor_fields, sessions = run.execute()
result = pd.DataFrame(raw_result)
print(tabulate(tensor_fields[0], headers='keys', tablefmt='psql'))
pprint(sessions)
print(tabulate(result, headers='keys', tablefmt='psql'))
