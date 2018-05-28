CREATE TABLE temporal (
    nom_elec        VARCHAR2(25 CHAR),
    anio            VARCHAR2(5 CHAR),
    pais            VARCHAR2(15 CHAR),
    region          VARCHAR2(10 CHAR),
    depto           VARCHAR2(25 CHAR),
    mun             VARCHAR2(35 CHAR),
    par             VARCHAR2(10 CHAR),
    nompar          VARCHAR2(30 CHAR),
    sexo            VARCHAR2(10 CHAR),
    raza            VARCHAR2(12 CHAR),
    analfavetos     NUMBER,
    alfavetos       NUMBER,
    sexo2           VARCHAR2(10 CHAR),
    raza2           VARCHAR2(12 CHAR),
    primaria        NUMBER,
    medio           NUMBER,
    univesitarios   NUMBER
);


CREATE TABLE departamento (
    id_departamento       NUMBER NOT NULL,
    nombre_departamento   VARCHAR2(25 CHAR) NOT NULL,
    region_id_region      NUMBER NOT NULL
);

ALTER TABLE departamento ADD CONSTRAINT departamento_pk PRIMARY KEY ( id_departamento );

CREATE TABLE eleccion (
    id_eleccion              NUMBER NOT NULL,
    nombre_eleccion          VARCHAR2(25 CHAR) NOT NULL,
    anio                     VARCHAR2(5 CHAR) NOT NULL,
    analfavetos              NUMBER NOT NULL,
    alfavetos                NUMBER NOT NULL,
    primaria                 NUMBER NOT NULL,
    medio                    NUMBER NOT NULL,
    universitario            NUMBER NOT NULL,
    municipio_id_municipio   NUMBER NOT NULL,
    partido_id_partido       NUMBER NOT NULL,
    genero_id_genero         NUMBER NOT NULL,
    raza_id_raza             NUMBER NOT NULL
);

ALTER TABLE eleccion ADD CONSTRAINT eleccion_pk PRIMARY KEY ( id_eleccion );

CREATE TABLE genero (
    id_genero       NUMBER NOT NULL,
    nombre_genero   VARCHAR2(10) NOT NULL
);

ALTER TABLE genero ADD CONSTRAINT genero_pk PRIMARY KEY ( id_genero );

CREATE TABLE municipio (
    id_municipio                   NUMBER NOT NULL,
    nombre_municipio               VARCHAR2(35 CHAR) NOT NULL,
    departamento_id_departamento   NUMBER NOT NULL
);

ALTER TABLE municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( id_municipio );

CREATE TABLE pais (
    id_pais       NUMBER NOT NULL,
    nombre_pais   VARCHAR2(15 CHAR) NOT NULL
);

ALTER TABLE pais ADD CONSTRAINT pais_pk PRIMARY KEY ( id_pais );

CREATE TABLE partido (
    id_partido          NUMBER NOT NULL,
    iniciales_partido   VARCHAR2(10 CHAR) NOT NULL,
    nombre_partido      VARCHAR2(30 CHAR) NOT NULL
);

ALTER TABLE partido ADD CONSTRAINT partido_pk PRIMARY KEY ( id_partido );

CREATE TABLE raza (
    id_raza       NUMBER NOT NULL,
    nombre_raza   VARCHAR2(12 CHAR) NOT NULL
);

ALTER TABLE raza ADD CONSTRAINT raza_pk PRIMARY KEY ( id_raza );

CREATE TABLE region (
    id_region       NUMBER NOT NULL,
    nombre_region   VARCHAR2(10 CHAR) NOT NULL,
    pais_id_pais    NUMBER NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( id_region );

ALTER TABLE departamento
    ADD CONSTRAINT departamento_region_fk FOREIGN KEY ( region_id_region )
        REFERENCES region ( id_region )
            ON DELETE CASCADE;

ALTER TABLE eleccion
    ADD CONSTRAINT eleccion_genero_fk FOREIGN KEY ( genero_id_genero )
        REFERENCES genero ( id_genero )
            ON DELETE CASCADE;

ALTER TABLE eleccion
    ADD CONSTRAINT eleccion_municipio_fk FOREIGN KEY ( municipio_id_municipio )
        REFERENCES municipio ( id_municipio )
            ON DELETE CASCADE;

ALTER TABLE eleccion
    ADD CONSTRAINT eleccion_partido_fk FOREIGN KEY ( partido_id_partido )
        REFERENCES partido ( id_partido )
            ON DELETE CASCADE;

ALTER TABLE eleccion
    ADD CONSTRAINT eleccion_raza_fk FOREIGN KEY ( raza_id_raza )
        REFERENCES raza ( id_raza )
            ON DELETE CASCADE;

ALTER TABLE municipio
    ADD CONSTRAINT municipio_departamento_fk FOREIGN KEY ( departamento_id_departamento )
        REFERENCES departamento ( id_departamento )
            ON DELETE CASCADE;

ALTER TABLE region
    ADD CONSTRAINT region_pais_fk FOREIGN KEY ( pais_id_pais )
        REFERENCES pais ( id_pais )
            ON DELETE CASCADE;

CREATE SEQUENCE departamento_id_departamento START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER departamento_id_departamento BEFORE
    INSERT ON departamento
    FOR EACH ROW
    WHEN ( new.id_departamento IS NULL )
BEGIN
    :new.id_departamento := departamento_id_departamento.nextval;
END;
/

CREATE SEQUENCE eleccion_id_eleccion_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER eleccion_id_eleccion_trg BEFORE
    INSERT ON eleccion
    FOR EACH ROW
    WHEN ( new.id_eleccion IS NULL )
BEGIN
    :new.id_eleccion := eleccion_id_eleccion_seq.nextval;
END;
/

CREATE SEQUENCE genero_id_genero_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER genero_id_genero_trg BEFORE
    INSERT ON genero
    FOR EACH ROW
    WHEN ( new.id_genero IS NULL )
BEGIN
    :new.id_genero := genero_id_genero_seq.nextval;
END;
/

CREATE SEQUENCE municipio_id_municipio_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER municipio_id_municipio_trg BEFORE
    INSERT ON municipio
    FOR EACH ROW
    WHEN ( new.id_municipio IS NULL )
BEGIN
    :new.id_municipio := municipio_id_municipio_seq.nextval;
END;
/

CREATE SEQUENCE pais_id_pais_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER pais_id_pais_trg BEFORE
    INSERT ON pais
    FOR EACH ROW
    WHEN ( new.id_pais IS NULL )
BEGIN
    :new.id_pais := pais_id_pais_seq.nextval;
END;
/

CREATE SEQUENCE partido_id_partido_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER partido_id_partido_trg BEFORE
    INSERT ON partido
    FOR EACH ROW
    WHEN ( new.id_partido IS NULL )
BEGIN
    :new.id_partido := partido_id_partido_seq.nextval;
END;
/

CREATE SEQUENCE raza_id_raza_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER raza_id_raza_trg BEFORE
    INSERT ON raza
    FOR EACH ROW
    WHEN ( new.id_raza IS NULL )
BEGIN
    :new.id_raza := raza_id_raza_seq.nextval;
END;
/

CREATE SEQUENCE region_id_region_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER region_id_region_trg BEFORE
    INSERT ON region
    FOR EACH ROW
    WHEN ( new.id_region IS NULL )
BEGIN
    :new.id_region := region_id_region_seq.nextval;
END;
/

QUIT;