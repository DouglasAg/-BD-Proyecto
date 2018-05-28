OPTIONS (SKIP=1)
LOAD DATA
CHARACTERSET UTF8
INFILE 'Cargar/Datos/ICE-Fuente.csv'
INTO TABLE temporal
FIELDS TERMINATED BY ','
TRAILING NULLCOLS
(
    nom_elec        "TRIM(:nom_elec)",
    anio            "TRIM(:anio)",
    pais            "TRIM(:pais)",
    region          "TRIM(:region)",
    depto           "TRIM(:depto)",
    mun             "TRIM(:mun)",
    par             "TRIM(:par)",
    nompar          "TRIM(:nompar)",
    sexo            "TRIM(:sexo)",
    raza            "TRIM(:raza)",
    analfavetos     "TRIM(:analfavetos)",
    alfavetos       "TRIM(:alfavetos)",
    sexo2           "TRIM(:sexo2)",
    raza2           "TRIM(:raza2)",
    primaria        "TRIM(:primaria)",
    medio           "TRIM(:medio)",
    univesitarios   "TRIM(:univesitarios)"
)