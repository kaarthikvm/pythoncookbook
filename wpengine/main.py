import sys
from task.constant import debug_print as DEBUG_PRINT
from task.constant import COMMAND_LEN as COMMAND_LEN
from task.task import task_main as tm

if __name__ == "__main__":
    DEBUG_PRINT("Length of arguments  %d" % (len(sys.argv)));
    DEBUG_PRINT("List of arguments    %s" % (str(sys.argv)));
    if len(sys.argv) != COMMAND_LEN:
        DEBUG_PRINT("Command Usage task.py <input file path> <output file path>");
        sys.exit(1);
    tm(sys.argv[1], sys.argv[2]);
