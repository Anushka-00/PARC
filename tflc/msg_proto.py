__author__ = 'Zhang Shaojun'
import struct

# tflc message header
TFLCP_HEADER_PACK_STR = '!BBHI'
TFLCP_HEADER_SIZE = 8
assert struct.calcsize(TFLCP_HEADER_PACK_STR) == TFLCP_HEADER_SIZE

# tflc message type
TFLCT_HELLO_UP = 0
TFLCT_HELLO_DOWN = 1
TFLCT_DATAPATH_CONNECTED = 2
TFLCT_ROLE_ASSIGN = 3
TFLCT_GID_REQUEST = 4
TFLCT_GID_REPLY = 5
TFLCT_PACKET_IN = 6
TFLCT_FLOW_MOD = 7
TFLCT_LOAD_REPORT = 8
TFLCT_DATAPATH_MIGRATION = 9
TFLCT_CONTRL_POOL_CHANGE = 10
TFLCT_ROLE_NOTIFY = 11
TFLCT_ECHO_REQUEST = 12
TFLCT_ECHO_REPLY = 13
TFLCT_ERROR = 14
TFLCT_BARRIER_REQUEST = 15
TFLCT_BARRIER_REPLY  =16
TFLCT_HOST_CONNECTED = 17
TFLCT_DATAPATH_LEAVE = 18
TFLCT_HOST_LEAVE = 19

# tflc message pack string
# assigned to 64 bits
TFLCP_HELLO_UP_PACK_STR = ''
TFLCP_HELLO_UP_SIZE = 8
assert struct.calcsize(TFLCP_HELLO_UP_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_HELLO_UP_SIZE

TFLCP_HELLO_DOWN_PACK_STR = '!I4x'
TFLCP_HELLO_DOWN_SIZE = 16
assert struct.calcsize(TFLCP_HELLO_DOWN_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_HELLO_DOWN_SIZE

TFLCP_DATAPATH_CONNECTED_PACK_STR = '!Q?7x'
TFLCP_DATAPATH_CONNECTED_SIZE = 24
assert struct.calcsize(TFLCP_DATAPATH_CONNECTED_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_DATAPATH_CONNECTED_SIZE

TFLCP_ROLE_ASSIGN_PACK_STR = '!QIIQ'
TFLCP_ROLE_ASSIGN_SIZE = 32
assert struct.calcsize(TFLCP_ROLE_ASSIGN_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_ROLE_ASSIGN_SIZE

TFLCP_GID_REQUEST_PACK_STR = '!Q'
TFLCP_GID_REQUEST_SIZE = 16
assert struct.calcsize(TFLCP_GID_REQUEST_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_GID_REQUEST_SIZE

TFLCP_GID_REPLY_PACK_STR = '!QQ'
TFLCP_GID_REPLY_SIZE = 24
assert struct.calcsize(TFLCP_GID_REPLY_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_GID_REPLY_SIZE

TFLCP_PACKET_IN_PACK_STR = '!Q17s7x17s7x'
TFLCP_PACKET_IN_SIZE = 64
assert struct.calcsize(TFLCP_PACKET_IN_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_PACKET_IN_SIZE

TFLCP_FLOW_MOD_PACK_STR = '!QQ17s5xH'
TFLCP_FLOW_MOD_SIZE = 48
assert struct.calcsize(TFLCP_FLOW_MOD_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_FLOW_MOD_SIZE

TFLCP_LOAD_REPORT_PACK_STR = '!QQ'
TFLCP_LOAD_REPORT_SIZE = 24
assert struct.calcsize(TFLCP_LOAD_REPORT_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_LOAD_REPORT_SIZE

TFLCP_DATAPATH_MIGRATION_PACK_STR = '!IIQ'
TFLCP_DATAPATH_MIGRATION_SIZE = 24
assert struct.calcsize(TFLCP_DATAPATH_MIGRATION_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_DATAPATH_MIGRATION_SIZE

TFLCP_CONTRL_POOL_CHANGE_PACK_STR = '!QI4x'
TFLCP_CONTRL_POOL_CHANGE_SIZE = 24
assert struct.calcsize(TFLCP_CONTRL_POOL_CHANGE_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_CONTRL_POOL_CHANGE_SIZE

TFLCP_ROLE_NOTIFY_PACK_STR = '!QII'
TFLCP_ROLE_NOTIFY_SIZE = 24
assert struct.calcsize(TFLCP_ROLE_NOTIFY_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_ROLE_NOTIFY_SIZE

TFLCP_ECHO_REQUEST_PACK_STR = '!Q'
TFLCP_ECHO_REQUEST_SIZE = 16
assert struct.calcsize(TFLCP_ECHO_REQUEST_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_ECHO_REQUEST_SIZE

TFLCP_ECHO_REPLY_PACK_STR = '!Q'
TFLCP_ECHO_REPLY_SIZE = 16
assert struct.calcsize(TFLCP_ECHO_REPLY_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_ECHO_REPLY_SIZE

TFLCP_ERROR_PACK_STR = '!HH4x'
TFLCP_ERROR_SIZE = 16
assert struct.calcsize(TFLCP_ERROR_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_ERROR_SIZE

TFLCP_HOST_CONNECTED_PACK_STR = '!Q17s7x'
TFLCP_HOST_CONNECTED_SIZE = 40
assert struct.calcsize(TFLCP_HOST_CONNECTED_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_HOST_CONNECTED_SIZE

TFLCP_DATAPATH_LEAVE_PACK_STR = '!Q'
TFLCP_DATAPATH_LEAVE_SIZE = 16
assert struct.calcsize(TFLCP_DATAPATH_LEAVE_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_DATAPATH_LEAVE_SIZE

TFLCP_HOST_LEAVE_PACK_STR = '!Q17s7x'
TFLCP_HOST_LEAVE_SIZE = 40
assert struct.calcsize(TFLCP_HOST_LEAVE_PACK_STR) + TFLCP_HEADER_SIZE == TFLCP_HOST_LEAVE_SIZE

# the controller address for controller pool change
TFLCP_LOCAL_CTRL_ADDRESS_PACK_STR = '!HIH'
TFLCP_LOCAL_CTRL_ADDRESS_SIZE = 8

#OpenFlow Controller Role
OFPCR_ROLE_NOCHANGE = 0
OFPCR_ROLE_EQUAL = 1
OFPCR_ROLE_MASTER = 2
OFPCR_ROLE_SLAVE = 3

# tflc packet in reason
TFLCR_PIN_NO_MATCH = 0
TFLCR_PIN_ACTION = 1

# tflc flow match wildcards

# tflc error type
TFLCET_UNKOWN_MSG = 0
# tflc error code




