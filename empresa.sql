CREATE TABLE IF NOT EXISTS empresas (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    snpj int unsigned,
    PRIMARY KEY (id),
    YNIQUE KEY (snpj)
);

CREATE TABLE IF NOT EXISTS empresas_unidades (
    empresa_id INT UNSIGNED NOT NULL,
    cidade_id INT UNSIGNED NOT NULL,
    sede TINYINT(1) NOT NULL,
    PRIMARY KEY (empresa_id, cidade_id)
);