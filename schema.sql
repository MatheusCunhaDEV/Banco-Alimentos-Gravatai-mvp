CREATE DATABASE IF NOT EXISTS banco_alimentos_gravatai;
USE banco_alimentos_gravatai;

CREATE TABLE alimentos (
    id_alimento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL UNIQUE,
    categoria VARCHAR(50) NOT NULL,
    unidade_medida VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ativo'
);

CREATE TABLE lotes_estoque (
    id_lote INT AUTO_INCREMENT PRIMARY KEY,
    id_alimento INT NOT NULL,
    origem_doacao VARCHAR(150) NOT NULL,
    quantidade_inicial DECIMAL(10,2) NOT NULL,
    quantidade_atual DECIMAL(10,2) NOT NULL,
    data_entrada DATE NOT NULL,
    data_validade DATE NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento)
);

CREATE TABLE entidades_beneficiarias (
    id_entidade INT AUTO_INCREMENT PRIMARY KEY,
    nome_instituicao VARCHAR(150) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    responsavel_recebimento VARCHAR(120) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ativa'
);

CREATE TABLE movimentacoes_saida (
    id_saida INT AUTO_INCREMENT PRIMARY KEY,
    id_lote INT NOT NULL,
    id_entidade INT NOT NULL,
    quantidade_retirada DECIMAL(10,2) NOT NULL,
    data_saida DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_lote) REFERENCES lotes_estoque(id_lote),
    FOREIGN KEY (id_entidade) REFERENCES entidades_beneficiarias(id_entidade)
);
