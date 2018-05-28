@echo off
sqlldr userid=douglas/Bases123 control=Control/ctl_datos.ctl LOG=LOG/log_datos.log BAD = BAD/bad_datos.bad DISCARD = DISCARD/dis_datos.dsc ;
echo  ----------------  Datos cargados ---------------- 
