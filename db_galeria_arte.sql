-- Alunos: LUIZA E OTÁVIO

    --  DROP TABELAS CASO EXISTAM   --
    DROP TABLE IF EXISTS PAGAMENTO ;
    DROP TABLE IF EXISTS EXIBICAO ;
    DROP TABLE IF EXISTS ORDENS ;
    DROP TABLE IF EXISTS  OBRA ;
    DROP TABLE IF EXISTS CLIENTE ;
    DROP TABLE IF EXISTS ARTISTA ;
  


    --  CRIANDO TABELAS --

    CREATE TABLE ARTISTA
    (
    NOME_ARTISTA 	varchar(25),
    ID_ARTISTA 	    varchar(20) NOT NULL PRIMARY KEY,
    EMAIL 		    varchar(20),
    PAIS 	        varchar(20)
    );

    CREATE TABLE OBRA
    (
    NOME_OBRA 	    varchar(25),
    ID_OBRA 		varchar(20) NOT NULL PRIMARY KEY,
    NOME_ARTISTA 	varchar(25),
    ID_ARTISTA      varchar(20),
    TIPO_ARTE 	    varchar(20),
    DATA_CRIACAO 	varchar(25),
    PRECO 		    int,
    CONSTRAINT FK_ID_ARTISTA FOREIGN KEY(ID_ARTISTA) REFERENCES ARTISTA(ID_ARTISTA)
    );

    CREATE TABLE CLIENTE
    (
    ID_CLIENTE 			varchar(20) NOT NULL PRIMARY KEY,
    CLIENTE_NOME 		varchar(25),
    TELEFONE 		    int,
    PREFERENCIA_ARTE 	varchar(25),
    CLIENTE_ENDERECO 	varchar(100),
    CLIENTE_PAIS	    varchar(25)
    );

    CREATE TABLE ORDENS 
    (
    ID_OBRA 		varchar(20),
    ID_CLIENTE 	    varchar(20),
    DATA_ORDEM 	    varchar(25),
    DATA_ENVIO 	    varchar(25),
    CONSTRAINT FK_ID_CLIENTE FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE)
    );

    CREATE TABLE PAGAMENTO
    (
    ID_OBRA 	varchar(25),
    ID_CLIENTE	varchar(20),
    VALOR 		int,
    CONSTRAINT FK_CLIENTEID FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE)
    );

    CREATE TABLE EXIBICAO
    (
    ID_OBRA         varchar(20),
    LOCAL_EXIBICAO  varchar(30),
    DATA_EXIBICAO   varchar(25),
    CONSTRAINT FK_ARTSLNO FOREIGN KEY(ID_OBRA) REFERENCES OBRA(ID_OBRA)
    );

    --  POPULANDO TABELA ARTISTA   --

    insert into ARTISTA values('Leonerdo Da Vinci','1','no emailid','Italy');
    insert into ARTISTA values('Pablo Picasso','2','no emailid','Spain');
    insert into ARTISTA values('Wassily Kandinsky','3','no emailid','Russia');
    insert into ARTISTA values('Vincent van Gogh','4','no emailid','Netherlands');
    insert into ARTISTA values('Zaynul Abedin','5','no emailid','Bangladesh');
    insert into ARTISTA values('Kiyokata Kaburagi','6','no emailid','Japan');
    insert into ARTISTA values('Michelangelo','7','no emailid','Italy');
    insert into ARTISTA values('Elisabetta Sirani Bologna','8','no emailid','Italy');

    --  POPULANDO TABELA OBRA   --

    insert into OBRA values('The Mona Lisa','mona002','Leonerdo Da Vinci','1','Portrait','10-jan-1517',200000);
    insert into OBRA values('The Weeping Woman','tww01','Pablo Picasso','2','Cubism','26-oct-1937',100000);
    insert into OBRA values('Composition V','comp05','Wassily Kandinsky','3','Abstract','12-june-1911',80000);
    insert into OBRA values('The Starry Night','str01','Vincent van Gogh','4','Mordern Art','10-june-1889',200000);
    insert into OBRA values('Monpura 70','mon70','Zaynul Abedin','5','Realism','04-jan-1974',90000);
    insert into OBRA values('The Three Faces','ttf01','Zaynul Abedin','5','Mordern Art','26-July-1968',100000);
    insert into OBRA values('Scarlet Peach','sp03','Kiyokata Kaburagi','6','Bijinga','28-Aug-1909',40000);
    insert into OBRA values('Improvisation 10','iv10','Wassily Kandinsky','3','Abstract','14-Nov-1910',20000);
    insert into OBRA values('Creation of Adam','coa1','Michelangelo','7','Cristian Art','28-Jan-1512',140000);
    insert into OBRA values('Virgin And Child','vac10','Elisabetta Sirani Bologna','8','Cristian Art','14-jan-1665',100000);

    --  POPULANDO TABELA CLIENTE   --

    insert into CLIENTE values('C01','Mr.Arif Hossain',01724777840,'Abstract','Gulshan 1','Bangladesh');
    insert into CLIENTE values('C02','Mr.Fzle Rabbi',01814888329,'Unknown','Mirpur 2','Bangladesh');
    insert into CLIENTE values('C03','Anjali Roy',01724878946,'Abstract','Dhanmondi 27','Bangladesh');
    insert into CLIENTE values('C04','Khorshed Alam',01714879234,'Mordern Art','Gulshan 2','Bangladesh');
    insert into CLIENTE values('C05','Mithun',01754543439,'Abstract','Gulshan 2','Bangladesh');
    insert into CLIENTE values('C06','Ahsan Labib',01987456103,'Abstract','Muhammadpur','Bangladesh');
    insert into CLIENTE values('C07','Ashikur Rahman',01645683429,'Mordern Art','Mirpur 10','Bangladesh');
    insert into CLIENTE values('C08','Fabiha Anber',01723298561,'Ancient Art','Baridhara','Bangladesh');
    insert into CLIENTE values('C09','Shafiur Rahman',01685690132,'Mordern Art','Uttara','Bangladesh');
    insert into CLIENTE values('C010','Saiful Ahmmed',01995643789,'Abstract','Rampura','Bangladesh');

    --  POPULANDO TABELA ORDENS   --

    insert into ORDENS values('mona002','C01','28-August-2021','01-September-2021');
    insert into ORDENS values('tww01','C02','28-August-2021','01-September-2021');
    insert into ORDENS values('comp05','C03','28-August-2021','02-September-2021');
    insert into ORDENS values('str01','C04','02-September-2021','08-September-2021');
    insert into ORDENS values('mon70','C05','02-September-2021','08-September-2021');
    insert into ORDENS values('ttf01','C06','28-August-2021','02-September-2021');
    insert into ORDENS values('sp03','C07','28-August-2021','02-September-2021');
    insert into ORDENS values('iv10','C08','02-September-2021','08-September-2021');
    insert into ORDENS values('coa1','C09','02-September-2021','08-September-2021');
    insert into ORDENS values('vac10','C010','02-September-2021','08-September-2021');

    --  POPULANDO TABELA PAGAMENTO   --

    insert into PAGAMENTO values('mona002','C01',200000);
    insert into PAGAMENTO values('tww01','C02',100000);
    insert into PAGAMENTO values('comp05','C03',80000);
    insert into PAGAMENTO values('str01','C04',200000);
    insert into PAGAMENTO values('mon70','C05',90000);
    insert into PAGAMENTO values('ttf01','C06',100000);
    insert into PAGAMENTO values('sp03','C07',40000);
    insert into PAGAMENTO values('iv10','C08',20000);
    insert into PAGAMENTO values('coa1','C09',140000);
    insert into PAGAMENTO values('vac10','C010',100000);

    --  POPULANDO TABELA EXIBICAO   -- 

    insert into EXIBICAO values('mona002','Gulshan Audetorium','28-August-2021');
    insert into EXIBICAO values('tww01','Gulshan Audetorium','28-August-2021');
    insert into EXIBICAO values('comp05','Gulshan Audetorium','28-August-2021');
    insert into EXIBICAO values('str01','Dhanmondi Audetorium','02-September-2021');
    insert into EXIBICAO values('mon70','Dhanmondi Audetorium','02-September-2021');
    insert into EXIBICAO values('ttf01','Gulshan Audetorium','28-August-2021');
    insert into EXIBICAO values('sp03','Gulshan Audetorium','28-August-2021');
    insert into EXIBICAO values('iv10','Dhanmondi Audetorium','02-September-2021');
    insert into EXIBICAO values('sp03','Dhanmondi Audetorium','02-September-2021');
    insert into EXIBICAO values('iv10','Dhanmondi Audetorium','02-September-2021');
