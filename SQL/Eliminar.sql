DROP SEQUENCE departamento_id_departamento;
DROP SEQUENCE eleccion_id_eleccion_seq;
DROP SEQUENCE genero_id_genero_seq;
DROP SEQUENCE municipio_id_municipio_seq;
DROP SEQUENCE pais_id_pais_seq;
DROP SEQUENCE partido_id_partido_seq;
DROP SEQUENCE raza_id_raza_seq;
DROP SEQUENCE region_id_region_seq;




DROP TABLE eleccion CASCADE CONSTRAINTS;
DROP TABLE municipio CASCADE CONSTRAINTS;
DROP TABLE departamento CASCADE CONSTRAINTS;
DROP TABLE region CASCADE CONSTRAINTS;
DROP TABLE pais CASCADE CONSTRAINTS;
DROP TABLE genero CASCADE CONSTRAINTS;
DROP TABLE partido CASCADE CONSTRAINTS;
DROP TABLE raza CASCADE CONSTRAINTS;



QUIT;