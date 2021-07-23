
-- Cria a tabela do cliente -- 
 
create table cliente(
id integer auto_increment not null,
nome varchar(255),
data_de_nascimento date,
primary key(id)
);

-- Cria a tabela de indentificação do cliente --
  
create table identificacao(
id integer auto_increment not null,
cpf varchar(14) unique,
identidade varchar(40),
id_cliente integer,
primary key(id),
constraint cliente_identificacao foreign key (id_cliente) references cliente(id)
);

-- Enedereço do cliente -- 

create table endereco(
id integer auto_increment not null,
rua varchar(100),
numero integer,
bairro varchar(50),
cidade varchar(100),
cep varchar(8),
pais varchar(3),
complemento varchar(100),
id_cliente integer,
primary key(id),
constraint cliente_endereco foreign key (id_cliente) references cliente(id)
);

-- Contato do cliente --
 
create table contato(
id integer auto_increment not null,
id_cliente integer,
primary key (id),
constraint cliente_contato foreign key (id_cliente) references cliente(id));

create table rede_social(
id integer auto_increment not null,
url varchar(255),
id_contato integer,
primary key (id),
constraint contato_rede_social foreign key (id_contato) references contato(id)
);

-- Cria tabela para redes sociais do cliente --
 
create table email(
id integer auto_increment not null,
endereco varchar(255),
id_contato integer,
primary key (id),
constraint contato_email foreign key (id_contato) references contato(id)
);

-- Cria tabela para telefones do cliente -- 

create table telefone(
id integer auto_increment not null,
numero varchar(9),
id_contato integer,
primary key (id),
constraint telefone_email foreign key (id_contato) references contato(id)
);
