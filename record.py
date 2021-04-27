import requests

class Record():
    def __init__(self, record_time, record_value, sensor_id, unit):
        self.record_time = record_time
        self.record_value = record_value
        self.sensor_id = sensor_id
        self.unit = unit
        self.obj = self.creat_obj()

    def creat_obj(self):
        obj_json = {"recordDateTime": self.record_time, "recordValue": self.record_value, "sensorId": self.sensor_id, "unit": self.unit}
        return (obj_json)

    def update(self, list_records):
        url = 'http://localhost:53034/api/record'
        headers={'Content-type':'application/json', 'Accept':'application/json'}                    
        x = requests.post(url, json=list_records,headers=headers)        
        if(x.status_code == 200):
            return True
        else:
            return False        

