#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct
import snap7

plc = snap7.client.Client()
plc.connect('10.34.64.220', 0, 2)
result = plc.db_read(301, 0, 102)
print(result)
tar_module, sou_module, tel_type, tel_type_ems, tel_type_plc, equ_id, cargo_num, profile, weight, empty_full, orientation, origin, destination, valid, mode, sc_status, do_unload_permit, etv_location_column, idle, tel_id, write_permit, sign = struct.unpack('!hhhhh2x10s24s4xhihh10s10shhhhiihhh', result)
print(tar_module)
print(sou_module)
print(tel_type)
print(tel_type_ems)
print(tel_type_plc)
print(equ_id.decode('utf-8'))
print(cargo_num.decode('utf-8'))
print(profile)
print(weight)
print(empty_full)
print(orientation)
print(origin.decode('utf-8'))
print(destination.decode('utf-8'))
print(valid)
print(mode)
print(sc_status)
print(do_unload_permit)
print(etv_location_column)
print(idle)
print(tel_id)
print(write_permit)
print(sign)
plc.disconnect()
plc.destroy()


