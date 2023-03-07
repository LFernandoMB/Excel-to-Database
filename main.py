def upload_tabela():
    banco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='********',
        database='banco',
    )
    cursor = banco.cursor()
    funcionario = getFuncionario()
    df = pd.read_excel('Tabela_Excel.xlsx', engine='openpyxl')

    for i, data in enumerate(df.itertuples()):
        try:
            comando = f'INSERT INTO sql_database (coluna1, coluna2, coluna3, coluna4,coluna5) VALUES ("{data[1]}", "{data[2]}", "{data[3]}", "{data[4]}", "{data[5]}"'
            cursor.execute(comando)
            banco.commit()
        except:
            print('Dados não inseridos! Verificar se a planilha está devidamente preenchida!')
    cursor.close()
    banco.close()
    print('Dados inseridos com sucesso!')
