import sqlite3

# 1. Cria o arquivo 'empresa.db' e abre a conexão
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# 2. Cria uma tabela de usuários (caso ela não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT EXISTS,
        email TEXT UNIQUE
    )
''')

# 3. Insere um novo usuário (usando interrogação para evitar ataques de SQL Injection)
try:
    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)", 
        ("Ana Souza", "ana@email.com")
    )
    # Salva as alterações de inserção no banco de dados
    conexao.commit()
    print("Usuário cadastrado com sucesso!")
except sqlite3.IntegrityError:
    print("Aviso: Este e-mail já está cadastrado.")

# 4. Busca e exibe todos os usuários cadastrados
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("\n--- Lista de Usuários ---")
for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | E-mail: {usuario[2]}")

# 5. Sempre feche a conexão ao terminar
conexao.close()
