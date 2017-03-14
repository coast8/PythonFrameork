CREATE DATABASE `controle_estoque` /*!40100 DEFAULT CHARACTER SET latin1 */;



DROP TABLE IF EXISTS `controle_estoque`.`categoria`;
CREATE TABLE  `controle_estoque`.`categoria` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(45) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `controle_estoque`.`entrada`;
CREATE TABLE  `controle_estoque`.`entrada` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `data` datetime NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `produto` int(10) unsigned NOT NULL,
  `fornecedor` int(10) unsigned NOT NULL,
  `quantidade` int(10) unsigned NOT NULL,
  `obs` text NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `controle_estoque`.`fornecedor`;
CREATE TABLE  `controle_estoque`.`fornecedor` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` text NOT NULL,
  `telefone` text,
  `estado` text,
  `cidade` text,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `controle_estoque`.`produto`;
CREATE TABLE  `controle_estoque`.`produto` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `categoria` text,
  `nome` text NOT NULL,
  `estoque_minimo` int(10) unsigned NOT NULL default '0',
  `estoque_atual` int(10) unsigned NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `controle_estoque`.`retirante`;
CREATE TABLE  `controle_estoque`.`retirante` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` text NOT NULL,
  `empresa` text NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `controle_estoque`.`saida`;
CREATE TABLE  `controle_estoque`.`saida` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `data` datetime NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `produto` int(10) unsigned NOT NULL,
  `retirante` int(10) unsigned NOT NULL,
  `quantidade` int(10) unsigned NOT NULL,
  `obs` text NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;