# This is only a stub for pyslurm.
# The only reason for using this file is to make IDE happier when the real pyslurm is not installed in the current host.
# To use this stub, just make a soft link, e.g 'ln -s pyslurm-stub.py pyslurm.py'

class block:
    def find(self, name: str = '', val='') -> list:
        pass

    def find_id(self, blockID: str = None) -> dict:
        pass

    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def load(self):
        pass

    def print_info_msg(self, oneLiner: int = 0):
        pass

    def update(self, blockID, blockOP: int = 0):
        pass

    def update_error(self, blockID: str):
        pass

    def update_free(self, blockID: str):
        pass

    def update_recreate(self, blockID: str):
        pass

    def update_remove(self, blockID: str):
        pass

    def update_resume(self, blockID: str):
        pass


class config:
    def display_all(self):
        pass

    def find_id(self, keyID: str = '') -> dict:
        pass

    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def key_pairs(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass


class front_end:
    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def load(self):
        pass


class hostlist:
    def count(self):
        pass

    def create(self, hostnames=None):
        pass

    def destroy(self):
        pass

    def find(self, hostname):
        pass

    def get(self):
        pass

    def get_list(self) -> list:
        pass

    def pop(self):
        pass

    def push(self, hosts):
        pass

    def push_host(self, host):
        pass

    def ranged_string(self):
        pass

    def shift(self):
        pass

    def uniq(self):
        pass


class job:
    def find(self, name: str = '', val: str = '') -> list:
        pass

    def find_id(self, jobid: str) -> list:
        pass

    def find_user(self, user: str) -> dict:
        pass

    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def print_job_info_msg(self, oneLiner: int = 0):
        pass


class jobstep:
    def find(self, jobID: int = -1, stepID: int = -1):
        pass

    def get(self) -> dict:
        pass

    def ids(self):
        pass

    def lastUpdate(self) -> int:
        pass

    def layout(self, JobID: int = 0, StepID: int = 0) -> list:
        pass


class node:
    def find_id(self, nodeID: str) -> dict:
        pass

    def get(self) -> dict:
        pass

    def get_node(self, nodeID: str) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def print_node_info_msg(self, oneLiner: int = 0):
        pass

    def update(self, node_dict: dict) -> int:
        pass


class partition:
    def create(self, partition_dict: dict) -> int:
        pass

    def delete(self, PartID: str) -> int:
        pass

    def find(self, name: str = '', val: str = '') -> list:
        pass

    def find_id(self, partID: str) -> dict:
        pass

    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def print_info_msg(self, oneLiner: int = 0):
        pass

    def update(self, partition_dict: dict) -> int:
        pass


class reservation:
    def create(self, reservation_dict: dict = {}):
        pass

    def delete(self, ResID) -> int:
        pass

    def find(self, name: str = '', val: str = '') -> list:
        pass

    def find_id(self, resID: str) -> dict:
        pass

    def get(self) -> dict:
        pass

    def ids(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def load(self):
        pass

    def print_reservation_info_msg(self, oneLiner: int = 0):
        pass

    def update(self, reservation_dict: dict) -> int:
        pass


class statistics:
    def get(self) -> dict:
        pass

    def reset(self) -> int:
        pass


class topology:
    def display(self):
        pass

    def get(self) -> dict:
        pass

    def lastUpdate(self) -> int:
        pass

    def load(self):
        pass


class trigger:
    def clear(self, TriggerID: str, UserID: str, ID: str) -> int:
        pass

    def get(self) -> dict:
        pass

    def set(self, trigger_dict: dict) -> int:
        pass
