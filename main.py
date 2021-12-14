import json


class Register:
    
    registered_users = {}

    def __init__(self, input_files):
        for input_file in input_files:
            with open(input_file) as f:
                # For sake of simplicity we use json library
                json_list = json.load(f)

                for item in json_list:
                    # collect data for better readibility
                    name    = item["name"]
                    email   = item["email"]
                    ip      = item["ip"]
                    devices = item["devices"]
                    # merge devices if the email exist in registered user base
                    devices = devices if email not in self.registered_users\
                            else self.merge_devices(self.registered_users[email]["devices"], devices)
                    # update the entry
                    self.registered_users[email]={"name"   : name,\
                                                  "ip"     : ip,\
                                                  "devices": devices}
                    
        print(self.registered_users["janko@jankovic.rs"]["devices"])
        #self.registered_users = json.load(f)
        # parse JSON files
        # create a union of user data
        # implement error checks1
        # optional: run json parsers in parallel
        pass
    
    def merge_devices(self, devices_i1, devices_i2):
        return list(set(devices_i1) | set(devices_i2))

    # overloaded methods
    def __len__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def get_name(self, key):
        pass

    def get_IP(self, key):
        pass

    def get_devices(self, key):
        pass

    def set_name(self, key, name):
        pass

    def set_IP(self, key, IP):
        pass

    def set_devices(self, key, devices):
        pass

if __name__ == "__main__":
    Register1 = Register(["users_1.json"])