
-- Busca dados do cliente-- 

select cli.*, 
ende.rua,
ende.numero,
ende.bairro,
ende.cidade,
ende.cep,
ende.pais,
rede.url, 
tel.numero,
em.endereco
from 
cliente cli, 
endereco ende,
contato cont, 
rede_social rede,
email em,
telefone tel
where 
ende.id_cliente = cli.id and
cont.id_cliente = cli.id and 
rede.id_contato = cont.id and
em.id_contato = cont.id and
tel.id_contato = cont.id;
 