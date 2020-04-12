import redis
import json

absen = redis.Redis(
            host='127.0.0.1',
            port=6379, bd='1')

#admin
admin_01 = {'nama' : 'Izzat', 'username' : 'admin_01', 'password' : 0101}
admin_02 = {'nama' : 'Gina', 'username' : 'admin_02', 'password' : 0202}
admin_03 = {'nama' : 'Dave', 'username' : 'admin_03', 'password' : 0303}

#pegawai
pegawai_01 = {'nama' : 'Satria', 'id_pegawai' : 'pegawai_01', 'pin' : 0111}
pegawai_02 = {'nama' : 'Luki', 'id_pegawai' : 'pegawai_02', 'pin' : 0222}
pegawai_03 = {'nama' : 'Farhan', 'id_pegawai' : 'pegawai_03', 'pin' : 0333}
pegawai_04 = {'nama' : 'Gaga', 'id_pegawai' : 'pegawai_04', 'pin' : 0444}
pegawai_05 = {'nama' : 'Rizqi', 'id_pegawai' : 'pegawai_05', 'pin' : 0555}
pegawai_06 = {'nama' : 'Aslam', 'id_pegawai' : 'pegawai_06', 'pin' : 0666}

#input database ke server redis
#input admin

absen.hmset('admin_01', admin_01)
absen.hmset('admin_02', admin_02)
absen.hmset('admin_03', admin_03)

#input pegawai

absen.hmset('pegawai_01', pegawai_01)
absen.hmset('pegawai_02', pegawai_02)
absen.hmset('pegawai_03', pegawai_03)
absen.hmset('pegawai_04', pegawai_04)
absen.hmset('pegawai_05', pegawai_05)
absen.hmset('pegawai_06', pegawai_06)
