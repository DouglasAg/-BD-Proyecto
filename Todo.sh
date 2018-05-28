#!/bin/bash
echo Douglas Aguilar 201503935
sqlplus Douglas/Bases123 @SQL/Eliminar.sql
echo -------------------- Tablas Eliminadas -----------------
read
sqlplus Douglas/Bases123 @SQL/Crear.sql
echo -------------------- Tablas creadas --------------------
read

sqlldr userid=douglas/Bases123 control=Cargar/Control/ctl_datos.ctl LOG=Cargar/LOG/log_datos.log BAD=Cargar/BAD/bad_datos.bad DISCARD =Cargar/DISCARD/dis_datos.dsc ;
echo  --------------------  Datos cargados  a temporal -------------------- 
read
sqlplus Douglas/Bases123 @SQL/Datos.sql
echo  --------------------  Datos cargados  al modelo -------------------- 


exit