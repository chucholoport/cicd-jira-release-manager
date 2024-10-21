from libs import *

@dataclass
class status:
    success: int = 0
    failure: int = 1

@dataclass
class error:
    # data structure: tuple = (id, message)
    missing_argument:   tuple = (2, 'missing required argument')
    invalid_argument:   tuple = (3, 'invalid argument provided')
    argument_not_found: tuple = (4, 'provided argument not found')
    invalid_extension:  tuple = (5, 'invalid argument extension')
    
@dataclass
class application:
    name:      str = 'cicd-jira-release-manager'
    author:    str = 'jesus.loport'
    version:   str = '1.0'
    logger:    str = os.path.join('..', f'{name}.log')
    log_level: str = logging.INFO

@dataclass
class levelname:
    info:    str = ''
    debug:   str = 'debug'
    error:   str = 'error'
    warning: str = 'warning'